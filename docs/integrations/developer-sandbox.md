---
title: Developer Sandbox
description: Test the examina.io API safely with isolated data, test-only API keys, free exam attempts, quotas, retention, and sandbox reset controls.
tags: [examina api sandbox, test api, test exam integration, developer environment]
---

# Developer sandbox

The examina.io developer sandbox is an isolated test tenant hosted at
`https://sandbox.examina.io`. It uses the production application infrastructure
without sharing your live organization's exams, examinees, results, API keys,
webhooks, or billing state.

Use it to validate provisioning, assignment, launch-session, results, and
webhook integrations before sending live traffic.

## Open your sandbox

Every live organization can use one sandbox. Any verified organization user can
open it:

1. Sign in to the live dashboard.
2. Open **Settings → Developer Sandbox**.
3. Select **Open sandbox**.

The first visit creates the isolated sandbox automatically. examina.io then
signs you in at `sandbox.examina.io` with a short-lived, one-time browser
handoff, so there is normally no second login screen. The handoff contains no
password or reusable session credential and cannot be replayed after use.

The persistent **TEST MODE** banner and test styling indicate that the current
dashboard is using sandbox data. There is no environment toggle: the hostname
is the environment boundary.

## Create a test API key

From sandbox **Settings**, create a scoped test key. Test tokens begin with
`exm_test.` and are shown only once. Send them only to the sandbox API base URL:

```bash
curl --request GET \
  --header "Authorization: Bearer $EXAMINA_TEST_API_KEY" \
  --header "Accept: application/json" \
  "https://sandbox.examina.io/api/v1/exams"
```

The boundary is enforced in both directions:

- `exm_test.` keys work only at `sandbox.examina.io` and only for the linked
  sandbox tenant.
- `exm_live.` keys and legacy Basic Authentication are rejected by the sandbox.
- Test keys are rejected by the live API.

Signed sandbox webhook events include `"livemode": false` and
`"environment": "test"`, allowing receivers to keep test events out of live
downstream workflows.

Use the same v1 paths, request bodies, scopes, and idempotency behavior shown in
the [API reference](../api/index.md).

## Sandbox limits

The shared-infrastructure sandbox is intentionally small and free:

| Resource | Limit |
| --- | ---: |
| Examinees | 1 |
| Active exams | 3 |
| Groups | 3 |
| Exam attempts | 5 per 30-day period |
| Concurrent exam sessions | 1 |
| Completed-result retention | 30 days |
| API requests | 120 per test key per minute |
| Sandbox resets | 3 per day |

Sandbox attempts never reserve funds, consume paid-plan allowances, write usage
ledgers, or generate billable feature charges. Reconnecting to the same attempt
does not consume another allowance slot.

Paid external features such as live proctoring and identity verification are
not available in the sandbox. Email delivery and recording are disabled.

## Reset test data

An Administrator can use **Reset sandbox** from sandbox Settings up to three
times per day. Reset removes
test exams, examinees, groups, assignments, results, webhook configuration,
delivery records, and uploaded sandbox files.

Reset deliberately preserves:

- the sandbox tenant;
- scoped `exm_test.` keys; and
- the current 30-day attempt allowance usage.

Preserving the allowance prevents reset from becoming a way to bypass the free
usage limit. Revoke keys separately when they are no longer needed.

## Data retention and indexing

Completed sandbox results are automatically removed after 30 days. Sandbox
pages send `X-Robots-Tag: noindex, nofollow`; test tenant content is not intended
for search indexing. Public developer documentation remains indexable at
`docs.examina.io`.

## Recommended integration workflow

1. Build against `https://sandbox.examina.io/api/v1` with an `exm_test.` key.
2. Exercise success, validation, idempotency, retry, and webhook-signature paths.
3. Confirm your integration handles sandbox quota responses without retry loops.
4. Create a separate `exm_live.` key with the minimum required scopes.
5. Change both the base URL and secret through environment-specific deployment
   configuration; never transform a test token into a live token.

For copy-ready requests and a complete first test, follow the
[sandbox API quickstart](sandbox-api-quickstart.md).

## Troubleshoot access

If the automatic handoff expires or has already been used, return to the live
**Developer Sandbox** settings page and select **Open sandbox** again. A handoff
expires after 90 seconds. Direct sign-in at `sandbox.examina.io` remains
available as a fallback.

If API calls return HTTP 429, wait for the `Retry-After` period before retrying.
Use bounded exponential backoff and do not start parallel retry loops.
