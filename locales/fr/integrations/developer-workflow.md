---
title: Flux de travail d'intégration des développeurs
description: Provisionnez les candidats, créez des affectations, émettez des URL de lancement uniques et synchronisez les résultats avec examina.io.
tags:
- API d'évaluation
- intégration des examens
- API LMS
- API de résultats
translation_source: integrations/developer-workflow.md
translation_source_sha256: 95077cae1f14eaa9e4e46b5ab7917c976de504830eee6acddd0104191b7acb9c
---

# Flux de travail d'intégration des développeurs {#developer-integration-workflow}

La v1 API prend en charge le parcours complet de serveur à serveur depuis le candidat
provisionnement via la synchronisation des résultats.

Pour les tests d'intégration de pré-production, utilisez le [developer sandbox](developer-sandbox.md)
avec son URL de base de test uniquement et ses informations d'identification `exm_test.`. Les chemins des points de terminaison et
Les contrats de demande sont les mêmes que ceux du live v1 API.

## 1. Fournir un candidat {#1-provision-an-examinee}

Créez un candidat avec `POST /examinees` ou synchronisez jusqu'à 500 enregistrements
avec `POST /examinees/bulk-upsert`. L'insertion groupée correspond aux enregistrements par organisation
et le code du candidat. Les codes sont normalisés en majuscules.

Pour un nouvel enregistrement, indiquez `firstName`, `lastName` et `passcode`. Vous pouvez omettre
`code` pour que examina.io en génère un. Les dates de naissance utilisent `YYYY-MM-DD`.

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

Les codes d'accès sont en écriture seule dans le nouveau contrat de réponse.

## 2. Créez une mission {#2-create-an-assignment}

`POST /assignments` connecte un candidat à un examen. Spécifier le papier sélectionné
titres ou omettre `papers` pour attribuer chaque article. Les titres papier sont sensibles à la casse.

```json
{
  "examId": "EXAM_ID",
  "examineeId": "EXAMINEE_ID",
  "papers": ["Quantitative Reasoning", "English"],
  "startsAt": "2026-09-01T09:00:00-04:00[America/Toronto]",
  "exemptFromProctoring": false
}
```

Une affectation peut être mise à jour ou supprimée uniquement lorsque son statut est
`DISCONNECTED`. L’identité des examens et des candidats ne peut pas être modifiée.

## 3. Émettez une URL de lancement {#3-issue-a-launch-url}

Créez une URL éphémère avec `POST /exam-sessions` :

```json
{
  "examId": "EXAM_ID",
  "examineeId": "EXAMINEE_ID",
  "expiresInSeconds": 3600
}
```

Le candidat doit déjà être affecté à l'examen. Le `launchUrl` renvoyé est
à usage unique et expire après 60 secondes à 24 heures. Envoyez-le uniquement au destinataire
candidat via un canal fiable.

## 4. Recevoir l'achèvement {#4-receive-completion}

Abonnez un point de terminaison webhook à `result.completed`. Vérifiez sa signature avant
le traiter. L'événement inclut l'ID de résultat/d'affectation nécessaire à la récupération.

## 5. Récupérer le résultat faisant autorité {#5-retrieve-the-authoritative-result}

```bash
curl --header "Authorization: Bearer $EXAMINA_API_KEY" \
  "https://www.examina.io/api/v1/results?examId=EXAM_ID&page=1&pageSize=100"
```

Les résultats incluent le score global, le score maximum, le pourcentage, l'horodatage d'achèvement,
et les comptes et scores par article. Seules les tentatives terminées sont renvoyées.

## Réessayez en toute sécurité {#retry-safely}

Utilisez un `Idempotency-Key` distinct pour chaque opération logique de création ou de mise à jour.
Après un délai d'attente du réseau, renvoyez le même corps et la même clé. Gérer HTTP 409 en tant qu'état
ou conflit d'idempotence, HTTP 422 comme entrée invalide ou limite de ressources, HTTP 429
comme limite de taux de requête et HTTP 5xx avec un recul exponentiel limité.
