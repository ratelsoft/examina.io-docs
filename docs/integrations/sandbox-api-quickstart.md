---
title: Sandbox API Quickstart
description: Run a safe end-to-end examina.io API test with a sandbox key, one examinee, an assignment, and a single-use exam launch URL.
tags: [examina api quickstart, assessment api tutorial, sandbox api, exam integration]
---

# Sandbox API quickstart

This quickstart verifies authentication, examinee provisioning, assignment,
and exam-session creation without touching live data or billing.

## Before you begin

Open the [developer sandbox](developer-sandbox.md), upload or create a test exam
in its dashboard, and create a test API key with these scopes:

- `examinees:write`
- `assignments:write`
- `sessions:write`
- `exams:read`

Store the key and the test exam ID in your shell. Do not commit either value:

```bash
export EXAMINA_BASE_URL="https://sandbox.examina.io/api/v1"
export EXAMINA_API_KEY="exm_test.REPLACE_WITH_YOUR_KEY"
export EXAMINA_EXAM_ID="REPLACE_WITH_YOUR_TEST_EXAM_ID"
```

## 1. Confirm authentication

```bash
curl --fail-with-body \
  --header "Authorization: Bearer $EXAMINA_API_KEY" \
  --header "Accept: application/json" \
  "$EXAMINA_BASE_URL/exams"
```

A successful request returns HTTP 200. A test key is rejected on the live host,
and a live key is rejected on the sandbox host.

## 2. Create the test examinee

The sandbox permits one examinee. Use an idempotency key that represents this
logical creation request:

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

Copy the top-level `id` from the HTTP 201 response:

```bash
export EXAMINA_EXAMINEE_ID="REPLACE_WITH_RETURNED_ID"
```

Resending the identical request with the same idempotency key returns the same
resource. Reusing it with different data returns HTTP 409.

## 3. Assign the examinee

Omit `papers` to assign every paper in the exam. If you include it, paper titles
are case-sensitive.

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

The HTTP 201 response contains the assignment ID and its current lifecycle
status.

## 4. Create a single-use launch URL

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

Open the returned `launchUrl` only when the intended tester is ready. It is
single-use and expires at the returned `expiresAt` time.

## 5. Test failure handling

Before moving to live credentials, verify that your integration handles:

- HTTP 401 for a missing, revoked, or wrong-environment key;
- HTTP 403 for a key missing a required scope;
- HTTP 409 for an idempotency or resource-state conflict;
- HTTP 422 for invalid input or a sandbox quota;
- HTTP 429 for request-rate limits; and
- transient HTTP 5xx responses with bounded exponential backoff.

The sandbox allows 120 API requests per test key per minute. It never charges
attempts or creates billing state. When testing is complete, an Administrator
can reset sandbox data from Settings.

See the [developer integration workflow](developer-workflow.md) for results and
signed webhook delivery, and the [API reference](../api/index.md) for every
request and response contract.
