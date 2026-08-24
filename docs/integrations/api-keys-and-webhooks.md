---
title: Scoped API Keys and Signed Webhooks
description: Secure examina.io integrations with scoped API keys, idempotent requests, signed result webhooks, delivery history, and safe key rotation.
tags: [api authentication, scoped api keys, signed webhooks, webhook replay]
---

# Scoped API keys and signed webhooks

New integrations should use named, scoped API keys. Each key can be revoked
without interrupting other integrations and receives only the permissions it
needs. Legacy organization API Secret Keys remain compatible during migration.

## Create a scoped API key

An Administrator creates keys from the organization's developer settings. The
complete token is displayed only once. Live tokens begin with `exm_live.`;
[developer sandbox](developer-sandbox.md) tokens begin with `exm_test.`. Store
each token in a server-side secret manager.

| Scope | Allows |
| --- | --- |
| `examinees:read` | Read examinee records through existing endpoints |
| `examinees:write` | Create, update, and bulk-upsert examinees |
| `exams:read` | Read exam definitions |
| `exams:write` | Upload, configure, tag, and delete exams |
| `groups:read` | Read groups and their membership |
| `groups:write` | Create groups and change membership |
| `assignments:read` | Read exam assignments |
| `assignments:write` | Create, change, and delete unstarted assignments |
| `results:read` | Read completed results and paper summaries |
| `sessions:write` | Create single-use exam launch URLs |
| `webhooks:read` | List endpoints and delivery history |
| `webhooks:write` | Create endpoints, disable endpoints, and retry deliveries |

Authenticate using the Bearer scheme:

```bash
curl --request GET \
  --header "Authorization: Bearer $EXAMINA_API_KEY" \
  --header "Accept: application/json" \
  "https://www.examina.io/api/v1/results?page=1&pageSize=25"
```

Do not place API keys in browser code, mobile applications, screenshots,
source control, or support logs.

API keys are environment-bound. An `exm_live.` key works only on the live API.
An `exm_test.` key works only at `https://sandbox.examina.io/api/v1`. Legacy
Basic Authentication is accepted only by the live API.

## Make mutations idempotent

Creation and update endpoints require an `Idempotency-Key` header. Generate a
unique value for the logical operation and reuse it only when retrying that
same request:

```bash
curl --request POST \
  --header "Authorization: Bearer $EXAMINA_API_KEY" \
  --header "Content-Type: application/json" \
  --header "Idempotency-Key: candidate-import-2026-08-23-0001" \
  --data '{"code":"CANDIDATE-42","passcode":"temporary-secret","firstName":"Ada","lastName":"Okafor"}' \
  "https://www.examina.io/api/v1/examinees"
```

The key is retained for at least 24 hours. Repeating it with an identical body
returns the original resource. Reusing it with different data returns HTTP 409.

## Configure a signed webhook

Create an endpoint subscribed to `result.completed`:

```bash
curl --request POST \
  --header "Authorization: Bearer $EXAMINA_API_KEY" \
  --header "Content-Type: application/json" \
  --header "Idempotency-Key: webhook-results-v1" \
  --data '{"url":"https://integrator.example/webhooks/examina","events":["result.completed"]}' \
  "https://www.examina.io/api/v1/webhook-endpoints"
```

The response includes a `signingSecret` beginning with `whsec_`. It is shown
only once. Webhook URLs must use public HTTPS and must not resolve to a private,
loopback, link-local, or multicast address.

Every delivery contains a JSON event. The request also includes:

The event envelope includes `livemode` and `environment`. Sandbox deliveries
use `"livemode": false` and `"environment": "test"`; live deliveries use
`true` and `"live"`. Reject an unexpected environment before processing data.

| Header | Meaning |
| --- | --- |
| `X-Examina-Event-Id` | Stable event identifier for deduplication |
| `X-Examina-Timestamp` | Unix timestamp used in the signature |
| `X-Examina-Signature` | `v1=` followed by the hexadecimal HMAC-SHA256 signature |

Concatenate the timestamp, a period, and the exact raw request body. Calculate
HMAC-SHA256 with the signing secret and compare it to the `v1` signature using
a constant-time comparison:

```text
signed_content = timestamp + "." + raw_request_body
expected = hex(HMAC_SHA256(signing_secret, signed_content))
```

Return a 2xx response quickly and queue longer processing. Use the event ID to
deduplicate processing, then retrieve the authoritative result from
`GET /results/{assignmentId}`.

## Inspect and retry deliveries

```bash
curl --header "Authorization: Bearer $EXAMINA_API_KEY" \
  "https://www.examina.io/api/v1/webhook-endpoints/deliveries?page=1&pageSize=25"

curl --request POST \
  --header "Authorization: Bearer $EXAMINA_API_KEY" \
  "https://www.examina.io/api/v1/webhook-endpoints/deliveries/DELIVERY_ID/retry"
```

The earlier organization-level form callback remains available for existing
integrations but is deprecated. New integrations should use signed endpoint
resources because they provide event IDs, signatures, delivery state, and replay.

## Rotate or revoke credentials

Create a replacement key, deploy it to every consumer, verify successful calls,
and then revoke the previous key. Because keys are independent, rotation does
not require a simultaneous cutover. Revoke a key immediately if it may have
been exposed.
