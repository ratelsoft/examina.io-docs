---
title: API Keys and Completion Webhooks
description: Create examina.io public and secret API keys, authenticate REST requests, rotate credentials safely, and receive exam-completion webhooks.
tags: [api authentication, api keys, exam webhook, integration security]
---

# API keys and completion webhooks

Root and Administrator accounts manage integration credentials in **Home →
Settings → API Keys & Webhook**.

## Public key and secret key

The two keys have different purposes:

| Credential | Intended use | May appear in browser code? |
| --- | --- | --- |
| **API Public Key** | Identifies an approved Client widget integration | Yes, when used with the domain allowlist |
| **API Secret Key** | Authenticates server-to-server REST API requests | No |

The public key is not a substitute for the secret key. Domain approval remains
required for the embedded Client widget.

## Create and store credentials

1. Open **Home → Settings**.
2. In **API Keys & Webhook**, create the public key if you need the Client
   widget.
3. Create the secret key if you need the REST API or completion webhook.
4. Copy the secret immediately; it is displayed only once.
5. Store it in a server-side secret manager or encrypted deployment setting.

Never commit the secret to Git, paste it into client-side JavaScript, embed it
in a mobile application, or include it in support screenshots.

## Authenticate an API request

The API uses HTTPS Basic Authentication:

- username: **api**
- password: your API Secret Key

Example:

\`\`\`bash
curl --user "api:$EXAMINA_API_SECRET" \
  --header "Accept: application/json" \
  "https://www.examina.io/api/v1/exams/1"
\`\`\`

The variable must be set only in the server or terminal environment running the
request. Do not expose it in a public shell history, build log, or repository.

Success responses can use HTTP 200 or 201 depending on the operation. Error
responses remain JSON and include a false \`status\` value. Use the HTTP status
and documented response body together.

See the [interactive API reference](../api/index.md) for available operations
and schemas.

## Rotate a key

Regenerating a public or secret key invalidates consumers that still use the
old value. Plan a rotation:

1. inventory every widget, backend, scheduled job, and deployment that uses the
   key;
2. choose a maintenance window if simultaneous dual-key operation is not
   available;
3. generate and securely distribute the replacement;
4. update all consumers;
5. test a low-risk request or exam;
6. monitor for authentication failures; and
7. record completion in the organization's secret inventory.

Rotate immediately if a secret may have been exposed.

## Configure the completion webhook

The organization webhook receives an asynchronous HTTP POST when an examinee
finishes an exam. Enter a public HTTPS endpoint in the **Webhook URL** field and
select **Save**.

The current callback sends form fields:

| Field | Meaning |
| --- | --- |
| \`examineeId\` | Internal examinee identifier |
| \`examineeCode\` | Organization-assigned examinee code |
| \`examId\` | Internal exam identifier |
| \`examCode\` | Organization-assigned exam code |
| \`email\` | Examinee email when available; otherwise empty |

The callback is a completion notification, not the full result. Retrieve
authoritative details through the authenticated API.

## Build a resilient receiver

- Require HTTPS.
- Accept the form fields and validate expected identifier formats.
- Return a 2xx response quickly, then queue longer work.
- Make processing idempotent using the exam and examinee identifiers.
- Reconcile results through the API rather than trusting the callback alone.
- Log a correlation ID and status without logging credentials or excessive
  personal data.
- Monitor missed or failed processing and provide a replay or reconciliation
  process in your system.

The current public webhook contract does not document a request signature. Do
not treat possession of the callback fields as proof of authenticity; verify
the referenced state through the authenticated API before making consequential
changes.

## Test without real candidate data

Use a fictional examinee and test exam. Verify:

1. your endpoint receives the POST;
2. field parsing works when email is empty;
3. a duplicate event does not duplicate downstream work;
4. API reconciliation finds the completed attempt; and
5. logs and alerts contain no secret key or passcode.
