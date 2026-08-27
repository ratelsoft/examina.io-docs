---
title: "Sandbox do desenvolvedor"
description: "Teste a API do examina.io com segurança usando dados isolados, chaves de API de teste, tentativas gratuitas, cotas e redefinição do sandbox."
tags: [examina api sandbox, test api, test exam integration, developer environment]
translation_source: integrations/developer-sandbox.md
translation_source_sha256: c718f56012f845a3f038bc8acabc33a951bd510f885f20e027d776fe66f55f1e
---

# Sandbox do desenvolvedor

O sandbox do desenvolvedor do examina.io é um tenant de teste isolado hospedado em `https://sandbox.examina.io`. Ele usa a infraestrutura de aplicação de produção sem compartilhar as provas, candidatos, resultados, chaves de API, webhooks ou status de faturamento da sua organização em produção.

Use-o para validar integrações de provisionamento, atribuição, sessão de inicialização, resultados e webhooks antes de enviar tráfego em produção.

## Abra seu sandbox

Toda organização em produção pode usar um sandbox. Qualquer usuário verificado da organização pode abri-lo:

1. Faça login no painel principal em produção.
2. Abra **Configurações → Developer Sandbox**.
3. Selecione **Abrir sandbox**.

A primeira visita cria o sandbox isolado automaticamente. O examina.io então faz seu login em `sandbox.examina.io` com uma transferência de navegador temporária e de uso único, portanto, normalmente não há uma segunda tela de login. A transferência não contém senha nem credencial de sessão reutilizável e não pode ser reutilizada após o uso.

O banner persistente de **MODO DE TESTE** e o estilo visual de teste indicam que o painel atual está usando dados do sandbox. Não há alternância de ambiente: o nome do host é o limite do ambiente.

## Crie uma chave de API de teste

Em **Configurações** do sandbox, crie uma chave de teste com escopo restrito. Os tokens de teste começam com `exm_test.` e são exibidos apenas uma vez. Envie-os apenas para a URL base da API do sandbox:

```bash
curl --request GET \
  --header "Authorization: Bearer $EXAMINA_TEST_API_KEY" \
  --header "Accept: application/json" \
  "https://sandbox.examina.io/api/v1/exams"
```

O limite é imposto em ambas as direções:

- Chaves `exm_test.` funcionam apenas em `sandbox.examina.io` e somente para o tenant de sandbox vinculado.
- Chaves `exm_live.` e a Autenticação Básica legada são rejeitadas pelo sandbox.
- Chaves de teste são rejeitadas pela API em produção.

Eventos de webhook do sandbox assinados incluem `"livemode": false` e `"environment": "test"`, permitindo que os receptores mantenham os eventos de teste fora dos fluxos de trabalho secundários em produção.

Use os mesmos caminhos v1, corpos de requisição, escopos e comportamento de idempotência mostrados na [referência da API](../api/index.md).

## Limites do sandbox

O sandbox de infraestrutura compartilhada é intencionalmente pequeno e gratuito:

| Recurso | Limite |
| --- | ---: |
| Candidatos | 1 |
| Provas ativas | 3 |
| Grupos | 3 |
| Tentativas de prova | 5 por período de 30 dias |
| Sessões de prova simultâneas | 1 |
| Retenção de resultados concluídos | 30 dias |
| Requisições de API | 120 por chave de teste por minuto |
| Redefinições de sandbox | 3 por dia |

As tentativas no sandbox nunca reservam fundos, consomem cotas de planos pagos, registram histórico de uso nem geram cobranças por recursos faturáveis. Reconectar-se à mesma tentativa não consome outro slot da cota.

Recursos externos pagos, como fiscalização de provas ao vivo e verificação de identidade, não estão disponíveis no sandbox. A entrega de e-mails e a gravação estão desativadas.

## Redefinir dados de teste

Um Administrador pode usar **Redefinir sandbox** nas Configurações do sandbox até três vezes por dia. A redefinição remove provas de teste, candidatos, grupos, atribuições, resultados, configurações de webhook, registros de entrega e arquivos de sandbox enviados.

A redefinição preserva intencionalmente:

- o tenant do sandbox;
- chaves `exm_test.` com escopo; e
- o uso atual da cota de tentativas do período de 30 dias.

Preservar a cota evita que a redefinição se torne uma forma de burlar o limite de uso gratuito. Revogue as chaves separadamente quando elas não forem mais necessárias.

## Retenção de dados e indexação

Resultados de sandbox concluídos são removidos automaticamente após 30 dias. As páginas do sandbox enviam `X-Robots-Tag: noindex, nofollow`; o conteúdo do tenant de teste não destina-se à indexação de busca. A documentação pública do desenvolvedor permanece indexável em `docs.examina.io`.

## Fluxo de trabalho de integração recomendado

1. Desenvolva em relação a `https://sandbox.examina.io/api/v1` com uma chave `exm_test.`.
2. Teste fluxos de sucesso, validação, idempotência, nova tentativa e assinatura de webhook.
3. Confirme se sua integração manipula respostas de cota do sandbox sem loops de repetição.
4. Crie uma chave `exm_live.` separada com os escopos mínimos necessários.
5. Altere a URL base e o segredo por meio de configurações de implantação específicas do ambiente; nunca transforme um token de teste em um token de produção.

Para requisições prontas para copiar e um primeiro teste completo, siga o [início rápido da API do sandbox](sandbox-api-quickstart.md).

## Solução de problemas de acesso

Se a transferência automática expirar ou já tiver sido usada, retorne à página de configurações do **Developer Sandbox** em produção e selecione **Abrir sandbox** novamente. A transferência expira após 90 segundos. O login direto em `sandbox.examina.io` continua disponível como alternativa.

Se as chamadas de API retornarem HTTP 429, aguarde o período de `Retry-After` antes de tentar novamente. Use um algoritmo de recuo exponencial limitado e não inicie loops de repetição paralelos.
