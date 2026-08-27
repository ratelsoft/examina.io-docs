---
title: "Referencia de la API"
description: "Referencia de la API REST para integrar sistemas externos con examina.io."
translation_source: api/index.md
translation_source_sha256: fa5b9458d5dda85f1776c6ff0ae12e0be9377b40effda1b3c259ebc42c9ecae1
---

# Referencia de la API

La versión de producción reemplaza esta página con la referencia interactiva de la API generada a partir de [`reference/examina.io.v1.yaml`](https://github.com/ratelsoft/examina.io-docs/blob/main/reference/examina.io.v1.yaml).

Las nuevas integraciones se autentican con una clave de API Bearer con nombre y alcance asignado. La autenticación básica heredada sigue siendo compatible durante la migración. Los endpoints de desarrollo que modifican datos requieren un encabezado `Idempotency-Key`; consulta el [flujo de trabajo del desarrollador](../integrations/developer-workflow.md) y la [guía de seguridad](../integrations/api-keys-and-webhooks.md).

Usa `https://sandbox.examina.io/api/v1` con una clave `exm_test.` para realizar pruebas de integración aisladas y no facturables. Consulta la [guía del entorno de pruebas para desarrolladores](../integrations/developer-sandbox.md) para conocer las cuotas, la retención, el comportamiento de restablecimiento y las reglas de aislamiento del entorno.
