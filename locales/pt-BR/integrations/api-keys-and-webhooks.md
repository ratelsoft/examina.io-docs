---
title: "Chaves de API com escopo e webhooks assinados"
description: "Proteja as integrações do examina.io com chaves de API com escopo, requisições idempotentes, webhooks de resultados assinados, histórico de entregas e rotação segura."
tags: [api authentication, scoped api keys, signed webhooks, webhook replay]
translation_source: integrations/api-keys-and-webhooks.md
translation_source_sha256: 880a25fd36e3e26421e05743011286753915471d7ffe9b5722b21c91e7fe7001
---

# Chaves de API com escopo e webhooks assinados

Novas integrações devem usar chaves de API nomeadas e com escopo. Cada chave pode ser revogada sem interromper outras integrações e recebe apenas as permissões de que precisa. Chaves secretas de API legadas da organização permanecem compatíveis durante a migração.

## Criar uma chave de API com escopo

Um Administrador cria chaves a partir das configurações de desenvolvedor da organização. O token completo é exibido apenas uma vez. Tokens de produção começam com `exm_live.`; tokens do [ambiente de testes de desenvolvedor](developer-sandbox.md) começam com `exm_test.`. Armazene cada token em um gerenciador de segredos no servidor.

| Escopo | Permite |
| --- | --- |
| `examinees:read` | Ler registros de candidatos por meio dos endpoints existentes |
| `examinees:write` | Criar, atualizar e fazer upsert em lote de candidatos |
| `exams:read` | Ler definições de exames |
| `exams:write` | Enviar, configurar, etiquetar e excluir exames |
| `groups:read` | Ler grupos e seus membros |
| `groups:write` | Criar grupos e alterar membros |
| `assignments:read` | Ler atribuições de exames |
| `assignments:write` | Criar, alterar e excluir atribuições não iniciadas |
| `results:read` | Ler resultados concluídos e resumos em papel |
| `sessions:write` | Criar URLs de inicialização de exame de uso único |
| `webhooks:read` | Listar endpoints e histórico de entregas |
| `webhooks:write` | Criar endpoints, desativar endpoints e tentar entregas novamente |

Autentique-se usando o esquema Bearer:

```bash
curl --request GET \
  --header "Authorization: Bearer $EXAMINA_API_KEY" \
  --header "Accept: application/json" \
  "https://www.examina.io/api/v1/results?page=1&pageSize=25"
```

Não coloque chaves de API em código do navegador, aplicativos para celular, capturas de tela, controle de versão ou logs de suporte.

As chaves de API são vinculadas ao ambiente. Uma chave `exm_live.` funciona apenas na API de produção. Uma chave `exm_test.` funciona apenas em `https://sandbox.examina.io/api/v1`. A autenticação básica legada é aceita apenas pela API de produção.

## Torne as mutações idempotentes

Endpoints de criação e atualização exigem o cabeçalho `Idempotency-Key`. Gere um valor exclusivo para a operação lógica e reutilize-o apenas ao tentar novamente essa mesma requisição:

```bash
curl --request POST \
  --header "Authorization: Bearer $EXAMINA_API_KEY" \
  --header "Content-Type: application/json" \
  --header "Idempotency-Key: candidate-import-2026-08-23-0001" \
  --data '{"code":"CANDIDATE-42","passcode":"temporary-secret","firstName":"Ada","lastName":"Okafor"}' \
  "https://www.examina.io/api/v1/examinees"
```

A chave é mantida por pelo menos 24 horas. Repeti-la com um corpo idêntico retorna o recurso original. Reutilizá-la com dados diferentes retorna HTTP 409.

## Configurar um webhook assinado

Crie um endpoint inscrito em `result.completed`:

```bash
curl --request POST \
  --header "Authorization: Bearer $EXAMINA_API_KEY" \
  --header "Content-Type: application/json" \
  --header "Idempotency-Key: webhook-results-v1" \
  --data '{"url":"https://integrator.example/webhooks/examina","events":["result.completed"]}' \
  "https://www.examina.io/api/v1/webhook-endpoints"
```

A resposta inclui um `signingSecret` que começa com `whsec_`. Ele é exibido apenas uma vez. As URLs de webhook devem usar HTTPS público e não devem ser resolvidas para um endereço privado, de loopback, link-local ou multicast.

Cada entrega contém um evento JSON. A requisição também inclui:

O envelope do evento inclui `livemode` e `environment`. Entregas do ambiente de testes usam `"livemode": false` e `"environment": "test"`; entregas de produção usam `true` e `"live"`. Rejeite um ambiente inesperado antes de processar os dados.

| Cabeçalho | Significado |
| --- | --- |
| `X-Examina-Event-Id` | Identificador estável de evento para desduplicação |
| `X-Examina-Timestamp` | Timestamp Unix usado na assinatura |
| `X-Examina-Signature` | `v1=` seguido pela assinatura hexadecimal HMAC-SHA256 |

Concatene o timestamp, um ponto e o corpo bruto exato da requisição. Calcule o HMAC-SHA256 com o segredo de assinatura e compare-o com a assinatura `v1` usando uma comparação de tempo constante:

```text
signed_content = timestamp + "." + raw_request_body
expected = hex(HMAC_SHA256(signing_secret, signed_content))
```

Retorne uma resposta 2xx rapidamente e coloque em fila o processamento mais longo. Use o ID do evento para desduplicar o processamento e, em seguida, recupere o resultado definitivo de `GET /results/{assignmentId}`.

## Inspecionar e tentar entregas novamente

```bash
curl --header "Authorization: Bearer $EXAMINA_API_KEY" \
  "https://www.examina.io/api/v1/webhook-endpoints/deliveries?page=1&pageSize=25"

curl --request POST \
  --header "Authorization: Bearer $EXAMINA_API_KEY" \
  "https://www.examina.io/api/v1/webhook-endpoints/deliveries/DELIVERY_ID/retry"
```

O callback de formulário em nível de organização antigo permanece disponível para integrações existentes, mas está obsoleto. Novas integrações devem usar recursos de endpoint assinados porque eles fornecem IDs de eventos, assinaturas, estado de entrega e retransmissão.

## Rotacionar ou revogar credenciais

Crie uma chave de substituição, implante-a em cada consumidor, verifique as chamadas bem-sucedidas e, em seguida, revogue a chave anterior. Como as chaves são independentes, a rotação não exige uma transição simultânea. Revogue uma chave imediatamente se ela puder ter sido exposta.
