---
title: "Guía de inicio rápido de la API de Sandbox"
description: "Ejecuta una prueba integral y segura de la API de examina.io con una clave de Sandbox, un candidato, una asignación y una URL de inicio de examen de un solo uso."
tags: [examina api quickstart, assessment api tutorial, sandbox api, exam integration]
translation_source: integrations/sandbox-api-quickstart.md
translation_source_sha256: 8091d2d137179887e5a9857221371de160271055c4e2b83b7249be9abfb8416b
---

# Guía de inicio rápido de la API de Sandbox

Esta guía de inicio rápido verifica la autenticación, el aprovisionamiento de candidatos, la asignación y la creación de sesiones de examen sin modificar datos reales ni afectar la facturación.

## Antes de comenzar

Abre el [entorno de prueba para desarrolladores](developer-sandbox.md), carga o crea un examen de prueba en su panel de control y crea una clave de API de prueba con estos alcances:

- `examinees:write`
- `assignments:write`
- `sessions:write`
- `exams:read`

Guarda la clave y el ID del examen de prueba en tu shell. No incluyas ningún valor en tus commits:

```bash
export EXAMINA_BASE_URL="https://sandbox.examina.io/api/v1"
export EXAMINA_API_KEY="exm_test.REPLACE_WITH_YOUR_KEY"
export EXAMINA_EXAM_ID="REPLACE_WITH_YOUR_TEST_EXAM_ID"
```

## 1. Confirma la autenticación

```bash
curl --fail-with-body \
  --header "Authorization: Bearer $EXAMINA_API_KEY" \
  --header "Accept: application/json" \
  "$EXAMINA_BASE_URL/exams"
```

Una solicitud exitosa devuelve HTTP 200. Se rechazará una clave de prueba en el host de producción y una clave de producción en el host de Sandbox.

## 2. Crea el candidato de prueba

El entorno de Sandbox permite un candidato. Usa una clave de idempotencia que represente esta solicitud lógica de creación:

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

Copia el `id` de nivel superior de la respuesta HTTP 201:

```bash
export EXAMINA_EXAMINEE_ID="REPLACE_WITH_RETURNED_ID"
```

Volver a enviar exactamente la misma solicitud con la misma clave de idempotencia devuelve el mismo recurso. Reutilizarla con datos diferentes devuelve HTTP 409.

## 3. Asigna al candidato

Omite `papers` para asignar todas las evaluaciones del examen. Si lo incluyes, los títulos de las evaluaciones distinguen entre mayúsculas y minúsculas.

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

La respuesta HTTP 201 contiene el ID de la asignación y su estado actual dentro del ciclo de vida.

## 4. Crea una URL de inicio de un solo uso

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

Abre la `launchUrl` devuelta únicamente cuando la persona encargada de la prueba esté lista. Es de un solo uso y expira en la hora indicada en `expiresAt`.

## 5. Prueba el manejo de errores

Antes de pasar a las credenciales de producción, verifica que tu integración maneje:

- HTTP 401 para una clave faltante, revocada o de un entorno incorrecto;
- HTTP 403 para una clave a la que le falta un alcance requerido;
- HTTP 409 para un conflicto de idempotencia o del estado del recurso;
- HTTP 422 para entradas no válidas o un límite de cuota de Sandbox;
- HTTP 429 para límites de frecuencia de solicitudes; y
- respuestas HTTP 5xx temporales con un reintento exponencial limitado.

El entorno de Sandbox permite 120 solicitudes de API por clave de prueba por minuto. Nunca cobra intentos ni genera estados de facturación. Cuando termines las pruebas, un Administrador puede restablecer los datos de Sandbox desde Configuración.

Consulta el [flujo de trabajo de integración para desarrolladores](developer-workflow.md) para ver los resultados y la entrega de webhooks firmados, y la [referencia de la API](../api/index.md) para conocer todos los contratos de solicitud y respuesta.
