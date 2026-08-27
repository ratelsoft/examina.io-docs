---
title: Bac à sable API Démarrage rapide
description: Exécutez un test examina.io API sécurisé de bout en bout avec une clé
  sandbox, un candidat, un devoir et une URL de lancement d'examen à usage unique.
tags:
- Démarrage rapide de l'API Examina
- tutoriel sur l'API d'évaluation
- API du bac à sable
- intégration des examens
translation_source: integrations/sandbox-api-quickstart.md
translation_source_sha256: 8091d2d137179887e5a9857221371de160271055c4e2b83b7249be9abfb8416b
---

# Démarrage rapide du bac à sable API {#sandbox-api-quickstart}

Ce démarrage rapide vérifie l'authentification, le provisionnement des candidats, l'affectation,
et la création de sessions d'examen sans toucher aux données en direct ni à la facturation.

## Avant de commencer {#before-you-begin}

Ouvrez le [bac à sable du développeur](developer-sandbox.md), téléchargez ou créez un examen test
dans son tableau de bord et créez une clé de test API avec ces étendues :

- `examinees:write`
- `assignments:write`
- `sessions:write`
- `exams:read`

Stockez la clé et l’ID de l’examen de test dans votre shell. Ne validez aucune des deux valeurs :

```bash
export EXAMINA_BASE_URL="https://sandbox.examina.io/api/v1"
export EXAMINA_API_KEY="exm_test.REPLACE_WITH_YOUR_KEY"
export EXAMINA_EXAM_ID="REPLACE_WITH_YOUR_TEST_EXAM_ID"
```

## 1. Confirmez l'authentification {#1-confirm-authentication}

```bash
curl --fail-with-body \
  --header "Authorization: Bearer $EXAMINA_API_KEY" \
  --header "Accept: application/json" \
  "$EXAMINA_BASE_URL/exams"
```

Une requête réussie renvoie HTTP 200. Une clé de test est rejetée sur l'hôte live,
et une clé active est rejetée sur l'hôte sandbox.

## 2. Créez le candidat au test {#2-create-the-test-examinee}

Le bac à sable autorise un seul candidat. Utilisez une clé d'idempotence qui représente cela
demande de création logique :

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

Copiez le `id` de niveau supérieur à partir de la réponse HTTP 201 :

```bash
export EXAMINA_EXAMINEE_ID="REPLACE_WITH_RETURNED_ID"
```

Renvoyer la demande identique avec la même clé d'idempotence renvoie la même chose
ressource. Le réutiliser avec différentes données renvoie HTTP 409.

## 3. Attribuer le candidat {#3-assign-the-examinee}

Omettez `papers` pour attribuer chaque épreuve de l'examen. Si vous l'incluez, les titres papier
sont sensibles à la casse.

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

La réponse HTTP 201 contient l'ID d'affectation et son cycle de vie actuel
statut.

## 4. Créez une URL de lancement à usage unique {#4-create-a-single-use-launch-url}

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

Ouvrez le `launchUrl` renvoyé uniquement lorsque le testeur prévu est prêt. C'est
à usage unique et expire à l’heure `expiresAt` renvoyée.

## 5. Gestion des échecs de test {#5-test-failure-handling}

Avant de passer aux informations d'identification en direct, vérifiez que votre intégration gère :

- HTTP 401 pour une clé manquante, révoquée ou avec un mauvais environnement ;
- HTTP 403 pour une clé manquant d'une portée requise ;
- HTTP 409 pour une idempotence ou un conflit ressource-état ;
- HTTP 422 pour une entrée invalide ou un quota sandbox ;
- HTTP 429 pour les limites de taux de requête ; et
- Réponses HTTP 5xx transitoires avec un recul exponentiel limité.

Le bac à sable autorise 120 requêtes API par clé de test et par minute. Il ne charge jamais
tente ou crée un état de facturation. Une fois les tests terminés, un administrateur
peut réinitialiser les données du bac à sable à partir des paramètres.

Consultez le [workflow d'intégration des développeurs](developer-workflow.md) pour les résultats et
livraison de webhook signée et la [référence API](../api/index.md) pour chaque
contrat de demande et de réponse.
