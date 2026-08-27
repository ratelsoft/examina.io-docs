---
title: "Referência da API"
description: "Referência da API REST para integrar sistemas externos com o examina.io."
translation_source: api/index.md
translation_source_sha256: fa5b9458d5dda85f1776c6ff0ae12e0be9377b40effda1b3c259ebc42c9ecae1
---

# Referência da API

A versão de produção substitui esta página pela referência interativa da API gerada a partir de [`reference/examina.io.v1.yaml`](https://github.com/ratelsoft/examina.io-docs/blob/main/reference/examina.io.v1.yaml).

Novas integrações se autenticam com uma chave de API Bearer nomeada e com escopo. A autenticação básica legada permanece suportada durante a migração. Endpoints de desenvolvedor que realizam mutações exigem um `Idempotency-Key`; consulte o [fluxo de trabalho do desenvolvedor](../integrations/developer-workflow.md) e o [guia de segurança](../integrations/api-keys-and-webhooks.md).

Use `https://sandbox.examina.io/api/v1` com uma chave `exm_test.` para testes de integração isolados e sem cobrança no faturamento. Consulte o [guia do sandbox do desenvolvedor](../integrations/developer-sandbox.md) para saber mais sobre cotas, retenção, comportamento de redefinição e regras de isolamento de ambiente.
