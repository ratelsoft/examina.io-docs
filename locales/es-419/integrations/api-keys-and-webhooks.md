---
title: "Claves de API acotadas y webhooks firmados"
description: "Protege las integraciones de examina.io con claves de API acotadas, solicitudes idempotentes, webhooks firmados, historial de envíos y rotación segura."
tags: [api authentication, scoped api keys, signed webhooks, webhook replay]
translation_source: integrations/api-keys-and-webhooks.md
translation_source_sha256: 880a25fd36e3e26421e05743011286753915471d7ffe9b5722b21c91e7fe7001
---

# Claves de API acotadas y webhooks firmados

Las nuevas integraciones deben usar claves de API con nombre y permisos acotados. Cada clave se puede revocar sin interrumpir otras integraciones y recibe únicamente los permisos que necesita. Las claves secretas de API heredadas de la organización siguen siendo compatibles durante la migración.

## Crea una clave de API acotada

Un Administrador crea las claves desde la configuración de desarrollador de la organización. El token completo se muestra una sola vez. Los tokens de producción comienzan con `exm_live.`; los tokens del [entorno de pruebas para desarrolladores](developer-sandbox.md) comienzan con `exm_test.`. Guarda cada token en un gestor de secretos en el servidor.

| Permiso | Permite |
| --- | --- |
| `examinees:read` | Leer registros de candidatos a través de los endpoints existentes |
| `examinees:write` | Crear, actualizar y registrar candidatos de forma masiva |
| `exams:read` | Leer definiciones de exámenes |
| `exams:write` | Cargar, configurar, etiquetar y eliminar exámenes |
| `groups:read` | Leer grupos y sus miembros |
| `groups:write` | Crear grupos y cambiar sus miembros |
| `assignments:read` | Leer asignaciones de exámenes |
| `assignments:write` | Crear, cambiar y eliminar asignaciones no iniciadas |
| `results:read` | Leer resultados completados y resúmenes en papel |
| `sessions:write` | Crear URL de inicio de examen de un solo uso |
| `webhooks:read` | Listar endpoints e historial de envíos |
| `webhooks:write` | Crear endpoints, desactivar endpoints y reintentar envíos |

Autentícate mediante el esquema Bearer:

```bash
curl --request GET \
  --header "Authorization: Bearer $EXAMINA_API_KEY" \
  --header "Accept: application/json" \
  "https://www.examina.io/api/v1/results?page=1&pageSize=25"
```

No coloques claves de API en código de navegador, aplicaciones móviles, capturas de pantalla, control de versiones o registros de soporte.

Las claves de API están vinculadas al entorno. Una clave `exm_live.` funciona solo en la API de producción. Una clave `exm_test.` funciona solo en `https://sandbox.examina.io/api/v1`. La autenticación básica heredada solo se acepta en la API de producción.

## Haz que las mutaciones sean idempotentes

Los endpoints de creación y actualización requieren el encabezado `Idempotency-Key`. Genera un valor único para la operación lógica y reutilízalo solo cuando reintentes esa misma solicitud:

```bash
curl --request POST \
  --header "Authorization: Bearer $EXAMINA_API_KEY" \
  --header "Content-Type: application/json" \
  --header "Idempotency-Key: candidate-import-2026-08-23-0001" \
  --data '{"code":"CANDIDATE-42","passcode":"temporary-secret","firstName":"Ada","lastName":"Okafor"}' \
  "https://www.examina.io/api/v1/examinees"
```

La clave se conserva durante al menos 24 horas. Repetirla con un cuerpo idéntico devuelve el recurso original. Reutilizarla con datos diferentes devuelve un error HTTP 409.

## Configura un webhook firmado

Crea un endpoint suscrito a `result.completed`:

```bash
curl --request POST \
  --header "Authorization: Bearer $EXAMINA_API_KEY" \
  --header "Content-Type: application/json" \
  --header "Idempotency-Key: webhook-results-v1" \
  --data '{"url":"https://integrator.example/webhooks/examina","events":["result.completed"]}' \
  "https://www.examina.io/api/v1/webhook-endpoints"
```

La respuesta incluye un `signingSecret` que comienza con `whsec_`. Se muestra una sola vez. Las URL de los webhooks deben usar HTTPS público y no deben resolverse en una dirección privada, de bucle de retorno (loopback), de enlace local (link-local) o de multidifusión (multicast).

Cada envío contiene un evento JSON. La solicitud también incluye:

La envoltura del evento incluye `livemode` y `environment`. Los envíos del entorno de pruebas usan `"livemode": false` y `"environment": "test"`; los envíos de producción usan `true` y `"live"`. Rechaza cualquier entorno no esperado antes de procesar los datos.

| Encabezado | Significado |
| --- | --- |
| `X-Examina-Event-Id` | Identificador de evento estable para desduplicación |
| `X-Examina-Timestamp` | Marca de tiempo de Unix utilizada en la firma |
| `X-Examina-Signature` | `v1=` seguido de la firma hexadecimal HMAC-SHA256 |

Concatena la marca de tiempo, un punto y el cuerpo exacto sin procesar de la solicitud. Calcula HMAC-SHA256 con el secreto de firma y compáralo con la firma `v1` mediante una comparación de tiempo constante:

```text
signed_content = timestamp + "." + raw_request_body
expected = hex(HMAC_SHA256(signing_secret, signed_content))
```

Devuelve una respuesta 2xx rápidamente y pon en cola los procesamientos más largos. Usa el ID del evento para desduplicar el procesamiento y luego recupera el resultado definitivo desde `GET /results/{assignmentId}`.

## Inspecciona y reintenta envíos

```bash
curl --header "Authorization: Bearer $EXAMINA_API_KEY" \
  "https://www.examina.io/api/v1/webhook-endpoints/deliveries?page=1&pageSize=25"

curl --request POST \
  --header "Authorization: Bearer $EXAMINA_API_KEY" \
  "https://www.examina.io/api/v1/webhook-endpoints/deliveries/DELIVERY_ID/retry"
```

La devolución de llamada de formulario previa a nivel de organización sigue estando disponible para las integraciones existentes, pero está en desuso. Las nuevas integraciones deben usar recursos de endpoint firmados porque proporcionan ID de eventos, firmas, estado del envío y reintento.

## Rota o revoca credenciales

Crea una clave de reemplazo, despliégala en cada consumidor, verifica que las llamadas sean exitosas y luego revoca la clave anterior. Dado que las claves son independientes, la rotación no requiere un cambio simultáneo. Revoca una clave de inmediato si existe la posibilidad de que haya quedado expuesta.
