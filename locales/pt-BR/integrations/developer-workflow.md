---
title: "Fluxo de trabalho de integração para desenvolvedores"
description: "Cadastre candidatos, atribua exames, emita URLs de uso único, recupere resultados e sincronize eventos de conclusão com o examina.io."
tags: [assessment api, exam integration, lms api, results api]
translation_source: integrations/developer-workflow.md
translation_source_sha256: 95077cae1f14eaa9e4e46b5ab7917c976de504830eee6acddd0104191b7acb9c
---

# Fluxo de trabalho de integração para desenvolvedores

A API v1 dá suporte a toda a jornada servidor a servidor, desde o cadastramento de candidatos até a sincronização de resultados.

Para testes de integração em pré-produção, use o [sandbox para desenvolvedores](developer-sandbox.md) com sua URL base exclusiva para testes e credenciais `exm_test.`. Os caminhos dos endpoints e os contratos de requisição são os mesmos da API v1 em produção.

## 1. Cadastrar um candidato

Crie um candidato com `POST /examinees` ou sincronize até 500 registros com `POST /examinees/bulk-upsert`. O upsert em lote faz a correspondência dos registros por organização e código do candidato. Os códigos são normalizados para letras maiúsculas.

Para um novo registro, informe `firstName`, `lastName` e `passcode`. Você pode omitir `code` para que o examina.io gere um. As datas de nascimento usam `YYYY-MM-DD`.

```json
{
  "code": "APPLICANT-1042",
  "passcode": "temporary-secret",
  "firstName": "Ada",
  "middleName": "N.",
  "lastName": "Okafor",
  "dateOfBirth": "2001-04-19",
  "gender": 0,
  "email": "ada@example.org"
}
```

Os passcodes são apenas de escrita no novo contrato de resposta.

## 2. Criar uma atribuição

O `POST /assignments` conecta um candidato a um exame. Especifique os títulos das provas selecionadas ou omita `papers` para atribuir todas as provas. Os títulos das provas diferenciam maiúsculas de minúsculas.

```json
{
  "examId": "EXAM_ID",
  "examineeId": "EXAMINEE_ID",
  "papers": ["Quantitative Reasoning", "English"],
  "startsAt": "2026-09-01T09:00:00-04:00[America/Toronto]",
  "exemptFromProctoring": false
}
```

Uma atribuição só pode ser atualizada ou excluída enquanto seu status for `DISCONNECTED`. As identidades do exame e do candidato não podem ser alteradas.

## 3. Emitir uma URL de inicialização

Crie uma URL de curta duração com `POST /exam-sessions`:

```json
{
  "examId": "EXAM_ID",
  "examineeId": "EXAMINEE_ID",
  "expiresInSeconds": 3600
}
```

O candidato já deve estar atribuído ao exame. A `launchUrl` retornada é de uso único e expira em um período de 60 segundos a 24 horas. Envie-a apenas para o candidato pretendido por meio de um canal confiável.

## 4. Receber a conclusão

Inscreva um endpoint de webhook em `result.completed`. Verifique sua assinatura antes de processá-lo. O evento inclui o ID do resultado/atribuição necessário para a recuperação.

## 5. Recuperar o resultado definitivo

```bash
curl --header "Authorization: Bearer $EXAMINA_API_KEY" \
  "https://www.examina.io/api/v1/results?examId=EXAM_ID&page=1&pageSize=100"
```

Os resultados incluem pontuação geral, pontuação máxima, porcentagem, carimbo de data/hora de conclusão e contagens e pontuações por prova. Apenas tentativas concluídas são retornadas.

## Tentar novamente com segurança

Use uma `Idempotency-Key` distinta para cada operação lógica de criação ou atualização. Após um tempo limite de rede, reenvie o mesmo corpo e a mesma chave. Trate o HTTP 409 como um conflito de estado ou idempotência, o HTTP 422 como entrada inválida ou limite de recurso, o HTTP 429 como limite de taxa de requisições e o HTTP 5xx com backoff exponencial limitado.
