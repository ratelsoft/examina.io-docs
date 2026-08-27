---
title: "Flujo de trabajo de integración para desarrolladores"
description: "Aprovisiona candidatos, crea asignaciones de exámenes, emite URL de inicio de un solo uso, obtén resultados y sincroniza eventos con examina.io."
tags: [assessment api, exam integration, lms api, results api]
translation_source: integrations/developer-workflow.md
translation_source_sha256: 95077cae1f14eaa9e4e46b5ab7917c976de504830eee6acddd0104191b7acb9c
---

# Flujo de trabajo de integración para desarrolladores

La API v1 admite todo el proceso servidor a servidor, desde el aprovisionamiento de candidatos hasta la sincronización de resultados.

Para pruebas de integración en entorno previo a producción, usa el [sandbox para desarrolladores](developer-sandbox.md) con su URL base exclusiva para pruebas y credenciales `exm_test.`. Las rutas de los endpoints y los contratos de las solicitudes son idénticos a los de la API v1 en producción.

## 1. Aprovisiona a un candidato

Crea un candidato con `POST /examinees` o sincroniza hasta 500 registros con `POST /examinees/bulk-upsert`. La actualización masiva (bulk-upsert) coincide con los registros por organización y código de candidato. Los códigos se normalizan a mayúsculas.

Para un nuevo registro, proporciona `firstName`, `lastName` y `passcode`. Puedes omitir `code` para que examina.io genere uno. Las fechas de nacimiento usan el formato `YYYY-MM-DD`.

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

Los passcodes son de solo escritura en el nuevo contrato de respuesta.

## 2. Crea una asignación

`POST /assignments` conecta a un candidato con un examen. Especifica los títulos de las pruebas seleccionadas u omite `papers` para asignar todas las pruebas. Los títulos de las pruebas distinguen entre mayúsculas y minúsculas.

```json
{
  "examId": "EXAM_ID",
  "examineeId": "EXAMINEE_ID",
  "papers": ["Quantitative Reasoning", "English"],
  "startsAt": "2026-09-01T09:00:00-04:00[America/Toronto]",
  "exemptFromProctoring": false
}
```

Una asignación solo se puede actualizar o eliminar mientras su estado sea `DISCONNECTED`. Las identidades del examen y del candidato no se pueden cambiar.

## 3. Emite una URL de inicio

Crea una URL de corta duración con `POST /exam-sessions`:

```json
{
  "examId": "EXAM_ID",
  "examineeId": "EXAMINEE_ID",
  "expiresInSeconds": 3600
}
```

El candidato ya debe estar asignado al examen. La `launchUrl` devuelta es de un solo uso y expira entre 60 segundos y 24 horas. Envíala únicamente al candidato correspondiente a través de un canal seguro.

## 4. Recibe la finalización

Suscribe un endpoint de webhook a `result.completed`. Verifica su firma antes de procesarlo. El evento incluye el ID del resultado o asignación necesario para la obtención del mismo.

## 5. Obtén el resultado definitivo

```bash
curl --header "Authorization: Bearer $EXAMINA_API_KEY" \
  "https://www.examina.io/api/v1/results?examId=EXAM_ID&page=1&pageSize=100"
```

Los resultados incluyen la puntuación general, la puntuación máxima, el porcentaje, la marca de tiempo de finalización y los recuentos y puntuaciones por prueba. Solo se devuelven los intentos completados.

## Reintenta de forma segura

Usa una `Idempotency-Key` distinta para cada operación lógica de creación o actualización. Tras un tiempo de espera agotado de la red, vuelve a enviar el mismo cuerpo y clave. Maneja HTTP 409 como un conflicto de estado o idempotencia, HTTP 422 como una entrada no válida o un límite de recursos, HTTP 429 como un límite de tasa de solicitudes y HTTP 5xx con un tiempo de espera exponencial limitado (exponential backoff).
