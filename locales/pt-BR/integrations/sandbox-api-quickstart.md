---
title: "Início rápido da API Sandbox"
description: "Execute um teste seguro de ponta a ponta da API do examina.io com uma chave sandbox, um candidato, uma atribuição e uma URL de inicialização de prova."
tags: [examina api quickstart, assessment api tutorial, sandbox api, exam integration]
translation_source: integrations/sandbox-api-quickstart.md
translation_source_sha256: 8091d2d137179887e5a9857221371de160271055c4e2b83b7249be9abfb8416b
---

# Início rápido da API Sandbox

Este início rápido verifica a autenticação, o provisionamento do candidato, a atribuição e a criação de uma sessão de prova sem alterar dados reais ou faturamento.

## Antes de começar

Abra o [developer sandbox](developer-sandbox.md), envie ou crie uma prova de teste em seu painel e crie uma chave de API de teste com estes escopos:

- `examinees:write`
- `assignments:write`
- `sessions:write`
- `exams:read`

Armazene a chave e o ID da prova de teste em seu terminal. Não faça commit de nenhum dos dois valores:

```bash
export EXAMINA_BASE_URL="https://sandbox.examina.io/api/v1"
export EXAMINA_API_KEY="exm_test.REPLACE_WITH_YOUR_KEY"
export EXAMINA_EXAM_ID="REPLACE_WITH_YOUR_TEST_EXAM_ID"
```

## 1. Confirmar autenticação

```bash
curl --fail-with-body \
  --header "Authorization: Bearer $EXAMINA_API_KEY" \
  --header "Accept: application/json" \
  "$EXAMINA_BASE_URL/exams"
```

Uma requisição bem-sucedida retorna HTTP 200. Uma chave de teste é rejeitada no host de produção, e uma chave de produção é rejeitada no host do sandbox.

## 2. Criar o candidato de teste

O sandbox permite um candidato. Use uma chave de idempotência que represente esta requisição lógica de criação:

```bash
curl --fail-with-body \
  --request POST \
  --header "Authorization: Bearer $EXAMINA_API_KEY" \
  --header "Content-Type: application/json" \
  --header "Idempotency-Key: sandbox-quickstart-examinee-v1" \
  --data '{
    "code": "SANDBOX-001",
    "passcode": "replace-with-a-temporary-secret",
    "firstName": "Sandbox",
    "lastName": "Candidate",
    "email": "developer@example.org"
  }' \
  "$EXAMINA_BASE_URL/examinees"
```

Copie o `id` principal da resposta HTTP 201:

```bash
export EXAMINA_EXAMINEE_ID="REPLACE_WITH_RETURNED_ID"
```

Reenviar a requisição idêntica com a mesma chave de idempotência retorna o mesmo recurso. Reutilizá-la com dados diferentes retorna HTTP 409.

## 3. Atribuir o candidato

Omita `papers` para atribuir cada caderno de prova do exame. Se você o incluir, os títulos dos cadernos de prova diferenciam maiúsculas de minúsculas.

```bash
curl --fail-with-body \
  --request POST \
  --header "Authorization: Bearer $EXAMINA_API_KEY" \
  --header "Content-Type: application/json" \
  --header "Idempotency-Key: sandbox-quickstart-assignment-v1" \
  --data "{
    \"examId\": \"$EXAMINA_EXAM_ID\",
    \"examineeId\": \"$EXAMINA_EXAMINEE_ID\",
    \"startsAt\": null,
    \"exemptFromProctoring\": true
  }" \
  "$EXAMINA_BASE_URL/assignments"
```

A resposta HTTP 201 contém o ID da atribuição e seu status atual no ciclo de vida.

## 4. Criar uma URL de inicialização de uso único

```bash
curl --fail-with-body \
  --request POST \
  --header "Authorization: Bearer $EXAMINA_API_KEY" \
  --header "Content-Type: application/json" \
  --header "Idempotency-Key: sandbox-quickstart-session-v1" \
  --data "{
    \"examId\": \"$EXAMINA_EXAM_ID\",
    \"examineeId\": \"$EXAMINA_EXAMINEE_ID\",
    \"expiresInSeconds\": 3600
  }" \
  "$EXAMINA_BASE_URL/exam-sessions"
```

Abra a `launchUrl` retornada somente quando a pessoa que fará o teste estiver pronta. Ela é de uso único e expira no horário retornado em `expiresAt`.

## 5. Testar o tratamento de falhas

Antes de migrar para as credenciais de produção, verifique se a sua integração trata:

- HTTP 401 para chave ausente, revogada ou de ambiente incorreto;
- HTTP 403 para chave sem o escopo necessário;
- HTTP 409 para conflito de idempotência ou de estado de recurso;
- HTTP 422 para entrada inválida ou cota de sandbox atingida;
- HTTP 429 para limites de taxa de requisição; e
- respostas HTTP 5xx temporárias com backoff exponencial limitado.

O sandbox permite 120 requisições de API por chave de teste por minuto. Ele nunca cobra tentativas nem gera registros de faturamento. Quando os testes forem concluídos, um Administrador poderá redefinir os dados do sandbox em Configurações.

Consulte o [fluxo de trabalho de integração do desenvolvedor](developer-workflow.md) para obter os resultados e a entrega de webhooks assinados, e a [referência da API](../api/index.md) para ver todos os contratos de requisição e resposta.
