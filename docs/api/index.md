---
title: API Reference
description: REST API reference for integrating external systems with examina.io.
hide:
  - navigation
  - toc
---

# API reference

The production build replaces this page with the interactive API reference
generated from [`reference/examina.io.v1.yaml`](https://github.com/ratelsoft/examina.io-docs/blob/main/reference/examina.io.v1.yaml).

New integrations authenticate with a named, scoped Bearer API key. Legacy Basic
Authentication remains supported during migration. Mutating developer endpoints
require an `Idempotency-Key`; see the [developer workflow](../integrations/developer-workflow.md)
and [security guide](../integrations/api-keys-and-webhooks.md).

Use `https://sandbox.examina.io/api/v1` with an `exm_test.` key for isolated,
non-billable integration testing. See the [developer sandbox guide](../integrations/developer-sandbox.md)
for quotas, retention, reset behavior, and environment isolation rules.
