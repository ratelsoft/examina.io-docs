---
title: Developer Integration Workflow
description: Provision examinees, create exam assignments, issue single-use launch URLs, retrieve results, and synchronize completion events with examina.io.
tags: [assessment api, exam integration, lms api, results api]
---

# Developer integration workflow

The v1 API supports the complete server-to-server journey from candidate
provisioning through result synchronization.

## 1. Provision an examinee

Create one examinee with `POST /examinees`, or synchronize up to 500 records
with `POST /examinees/bulk-upsert`. Bulk upsert matches records by organization
and examinee code. Codes are normalized to uppercase.

For a new record, provide `firstName`, `lastName`, and `passcode`. You may omit
`code` to have examina.io generate one. Dates of birth use `YYYY-MM-DD`.

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

Passcodes are write-only in the new response contract.

## 2. Create an assignment

`POST /assignments` connects one examinee to one exam. Specify selected paper
titles or omit `papers` to assign every paper. Paper titles are case-sensitive.

```json
{
  "examId": "EXAM_ID",
  "examineeId": "EXAMINEE_ID",
  "papers": ["Quantitative Reasoning", "English"],
  "startsAt": "2026-09-01T09:00:00-04:00[America/Toronto]",
  "exemptFromProctoring": false
}
```

An assignment can be updated or deleted only while its status is
`DISCONNECTED`. Exam and examinee identities cannot be changed.

## 3. Issue a launch URL

Create a short-lived URL with `POST /exam-sessions`:

```json
{
  "examId": "EXAM_ID",
  "examineeId": "EXAMINEE_ID",
  "expiresInSeconds": 3600
}
```

The examinee must already be assigned to the exam. The returned `launchUrl` is
single-use and expires after 60 seconds to 24 hours. Send it only to the intended
examinee over a trusted channel.

## 4. Receive completion

Subscribe a webhook endpoint to `result.completed`. Verify its signature before
processing it. The event includes the result/assignment ID needed for retrieval.

## 5. Retrieve the authoritative result

```bash
curl --header "Authorization: Bearer $EXAMINA_API_KEY" \
  "https://www.examina.io/api/v1/results?examId=EXAM_ID&page=1&pageSize=100"
```

Results include overall score, maximum score, percentage, completion timestamp,
and per-paper counts and scores. Only completed attempts are returned.

## Retry safely

Use a distinct `Idempotency-Key` for each logical create or update operation.
After a network timeout, resend the same body and key. Handle HTTP 409 as a state
or idempotency conflict, HTTP 422 as invalid input, HTTP 429 as an organization
plan limit, and HTTP 5xx with bounded exponential backoff.
