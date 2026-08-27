---
title: Clés API étendues et webhooks signés
description: Sécurisez vos intégrations examina.io avec des clés API limitées, des requêtes idempotentes, des webhooks signés et une rotation sûre des clés.
tags:
- authentification API
- Clés API étendues
- webhooks signés
- relecture du webhook
translation_source: integrations/api-keys-and-webhooks.md
translation_source_sha256: 880a25fd36e3e26421e05743011286753915471d7ffe9b5722b21c91e7fe7001
---

# Clés API étendues et webhooks signés {#scoped-api-keys-and-signed-webhooks}

Les nouvelles intégrations doivent utiliser des clés API nommées et étendues. Chaque clé peut être révoquée
sans interrompre les autres intégrations et reçoit uniquement les autorisations nécessaires
besoins. Les clés secrètes API de l’organisation héritée restent compatibles pendant la migration.

## Créer une clé API étendue {#create-a-scoped-api-key}

Un administrateur crée des clés à partir des paramètres de développement de l'organisation. Le
le jeton complet n’est affiché qu’une seule fois. Les jetons actifs commencent par `exm_live.` ;
[Les jetons du développeur sandbox](developer-sandbox.md) commencent par `exm_test.`. Magasin
chaque jeton dans un gestionnaire de secrets côté serveur.

| Portée | Permet |
| --- | --- |
| `examinees:read` | Lire les dossiers des candidats via les points de terminaison existants |
| `examinees:write` | Créer, mettre à jour et insérer des candidats en masse |
| `exams:read` | Lire les définitions des examens |
| `exams:write` | Télécharger, configurer, marquer et supprimer des examens |
| `groups:read` | Lire les groupes et leurs membres |
| `groups:write` | Créer des groupes et modifier l'adhésion |
| `assignments:read` | Lire les devoirs d'examen |
| `assignments:write` | Créer, modifier et supprimer des affectations non commencées |
| `results:read` | Lire les résultats finalisés et les résumés des articles |
| `sessions:write` | Créer des URL de lancement d'examen à usage unique |
| `webhooks:read` | Répertorier les points de terminaison et l'historique de livraison |
| `webhooks:write` | Créer des points de terminaison, désactiver les points de terminaison et réessayer les diffusions |

Authentifiez-vous à l'aide du schéma Bearer :

```bash
curl --request GET \
  --header "Authorization: Bearer $EXAMINA_API_KEY" \
  --header "Accept: application/json" \
  "https://www.examina.io/api/v1/results?page=1&pageSize=25"
```

Ne placez pas les clés API dans le code du navigateur, les applications mobiles, les captures d'écran,
contrôle de source ou journaux de support.

Les clés API sont liées à l'environnement. Une clé `exm_live.` fonctionne uniquement sur le API en direct.
Une clé `exm_test.` fonctionne uniquement sur `https://sandbox.examina.io/api/v1`. Héritage
L'authentification de base est acceptée uniquement par le API en direct.

## Rendre les mutations idempotentes {#make-mutations-idempotent}

Les points de terminaison de création et de mise à jour nécessitent un en-tête `Idempotency-Key`. Générer un
valeur unique pour l'opération logique et réutilisez-la uniquement lorsque vous réessayez.
même demande :

```bash
curl --request POST \
  --header "Authorization: Bearer $EXAMINA_API_KEY" \
  --header "Content-Type: application/json" \
  --header "Idempotency-Key: candidate-import-2026-08-23-0001" \
  --data '{"code":"CANDIDATE-42","passcode":"temporary-secret","firstName":"Ada","lastName":"Okafor"}' \
  "https://www.examina.io/api/v1/examinees"
```

La clé est conservée pendant au moins 24 heures. Le répéter avec un corps identique
renvoie la ressource d'origine. Le réutiliser avec différentes données renvoie HTTP 409.

## Configurer un webhook signé {#configure-a-signed-webhook}

Créez un point de terminaison abonné à `result.completed` :

```bash
curl --request POST \
  --header "Authorization: Bearer $EXAMINA_API_KEY" \
  --header "Content-Type: application/json" \
  --header "Idempotency-Key: webhook-results-v1" \
  --data '{"url":"https://integrator.example/webhooks/examina","events":["result.completed"]}' \
  "https://www.examina.io/api/v1/webhook-endpoints"
```

La réponse inclut un `signingSecret` commençant par `whsec_`. Il est montré
une seule fois. Les URL de webhook doivent utiliser le HTTPS public et ne doivent pas être résolues en un HTTPS privé.
adresse de bouclage, de lien local ou de multidiffusion.

Chaque diffusion contient un événement JSON. La demande comprend également :

L'enveloppe d'événement comprend `livemode` et `environment`. Livraisons sandbox
utilisez `"livemode": false` et `"environment": "test"` ; utilisation des livraisons en direct
`true` et `"live"`. Rejetez un environnement inattendu avant de traiter les données.

| En-tête | Signification |
| --- | --- |
| `X-Examina-Event-Id` | Identificateur d'événement stable pour la déduplication |
| `X-Examina-Timestamp` | Horodatage Unix utilisé dans la signature |
| `X-Examina-Signature` | `v1=` suivi de la signature hexadécimale HMAC-SHA256 |

Concaténez l'horodatage, un point et le corps brut exact de la requête. Calculer
HMAC-SHA256 avec le secret de signature et comparez-le à la signature `v1` à l'aide de
une comparaison en temps constant :

```text
signed_content = timestamp + "." + raw_request_body
expected = hex(HMAC_SHA256(signing_secret, signed_content))
```

Renvoyez rapidement une réponse 2xx et mettez en file d'attente un traitement plus long. Utilisez l'ID d'événement pour
traitement de déduplication, puis récupérez le résultat faisant autorité à partir de
`GET /results/{assignmentId}`.

## Inspecter et réessayer les livraisons {#inspect-and-retry-deliveries}

```bash
curl --header "Authorization: Bearer $EXAMINA_API_KEY" \
  "https://www.examina.io/api/v1/webhook-endpoints/deliveries?page=1&pageSize=25"

curl --request POST \
  --header "Authorization: Bearer $EXAMINA_API_KEY" \
  "https://www.examina.io/api/v1/webhook-endpoints/deliveries/DELIVERY_ID/retry"
```

Le rappel de formulaire antérieur au niveau de l'organisation reste disponible pour les formulaires existants.
intégrations mais est obsolète. Les nouvelles intégrations doivent utiliser un point de terminaison signé
ressources car elles fournissent des ID d’événement, des signatures, l’état de livraison et la relecture.

## Rotation ou révocation des informations d'identification {#rotate-or-revoke-credentials}

Créez une clé de remplacement, déployez-la auprès de chaque consommateur, vérifiez les appels réussis,
puis révoquer la clé précédente. Parce que les clés sont indépendantes, la rotation
ne nécessitent pas de basculement simultané. Révoquer immédiatement une clé si elle peut avoir
été exposé.
