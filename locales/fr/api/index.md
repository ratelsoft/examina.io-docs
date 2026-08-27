---
title: Référence API
description: Référence REST API pour l'intégration de systèmes externes avec examina.io.
hide:
- navigation
- toc
translation_source: api/index.md
translation_source_sha256: fa5b9458d5dda85f1776c6ff0ae12e0be9377b40effda1b3c259ebc42c9ecae1
---

# Référence API {#api-reference}

La version de production remplace cette page par la référence interactive API
généré à partir de [`reference/examina.io.v1.yaml`](https://github.com/ratelsoft/examina.io-docs/blob/main/reference/examina.io.v1.yaml).

Les nouvelles intégrations s’authentifient avec une clé Bearer API nommée et étendue. Héritage de base
L'authentification reste prise en charge pendant la migration. Mutation des points de terminaison des développeurs
nécessite un `Idempotency-Key` ; voir le [workflow du développeur](../integrations/developer-workflow.md)
et [guide de sécurité](../integrations/api-keys-and-webhooks.md).

Utilisez `https://sandbox.examina.io/api/v1` avec une clé `exm_test.` pour des applications isolées,
tests d'intégration non facturables. Consultez le [guide du bac à sable du développeur](../integrations/developer-sandbox.md)
pour les quotas, la rétention, le comportement de réinitialisation et les règles d’isolation de l’environnement.
