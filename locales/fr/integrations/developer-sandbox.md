---
title: Bac à sable des développeurs
description: Testez l'API examina.io avec des données isolées, des clés de test, des tentatives gratuites, des quotas et une réinitialisation contrôlée.
tags:
- bac à sable de l'API Examina
- tester l'API
- intégration d'examen de test
- environnement de développement
translation_source: integrations/developer-sandbox.md
translation_source_sha256: c718f56012f845a3f038bc8acabc33a951bd510f885f20e027d776fe66f55f1e
---

# Bac à sable du développeur {#developer-sandbox}

Le bac à sable de développeur examina.io est un locataire de test isolé hébergé sur
`https://sandbox.examina.io`. Il utilise l'infrastructure des applications de production
sans partager les examens, les candidats, les résultats, les clés API de votre organisation en direct,
webhooks ou état de facturation.

Utilisez-le pour valider le provisionnement, l'affectation, la session de lancement, les résultats et
intégrations de webhooks avant d'envoyer du trafic en direct.

## Ouvrez votre bac à sable {#open-your-sandbox}

Chaque organisation en direct peut utiliser un bac à sable. Tout utilisateur d'une organisation vérifiée peut
ouvrez-le :

1. Connectez-vous au tableau de bord en direct.
2. Ouvrez **Paramètres → Developer Sandbox**.
3. Sélectionnez **Ouvrir le bac à sable**.

La première visite crée automatiquement le bac à sable isolé. examina.io puis
vous connecte à `sandbox.examina.io` avec un navigateur unique et de courte durée
transfert, il n'y a donc normalement pas de deuxième écran de connexion. Le transfert ne contient aucun
mot de passe ou identifiant de session réutilisable et ne peut pas être relu après utilisation.

La bannière persistante **TEST MODE** et le style de test indiquent que le
le tableau de bord utilise les données du bac à sable. Il n'y a pas de bascule d'environnement : le nom d'hôte
est la limite de l'environnement.

## Créer une clé de test API {#create-a-test-api-key}

Dans le bac à sable **Paramètres**, créez une clé de test étendue. Les jetons de test commencent par
`exm_test.` et ne sont affichés qu’une seule fois. Envoyez-les uniquement à l'URL de base du bac à sable API :

```bash
curl --request GET \
  --header "Authorization: Bearer $EXAMINA_TEST_API_KEY" \
  --header "Accept: application/json" \
  "https://sandbox.examina.io/api/v1/exams"
```

La limite est appliquée dans les deux sens :

- Les touches `exm_test.` fonctionnent uniquement sur `sandbox.examina.io` et uniquement pour les
  locataire du bac à sable.
- Les clés `exm_live.` et l'authentification de base héritée sont rejetées par le bac à sable.
- Les clés de test sont rejetées par le API en direct.

Les événements de webhook sandbox signés incluent `"livemode": false` et
`"environment": "test"`, permettant aux récepteurs de garder les événements de test hors direct
flux de travail en aval.

Utilisez les mêmes chemins v1, corps de requête, étendues et comportement d'idempotence indiqués dans
la [référence API](../api/index.md).

## Limites du bac à sable {#sandbox-limits}

Le bac à sable d'infrastructure partagée est intentionnellement petit et gratuit :

| Ressource | Limite |
| --- | --- : |
| Candidats | 1 |
| Examens actifs | 3 |
| Groupes | 3 |
| Tentatives d'examen | 5 par période de 30 jours |
| Sessions d'examens simultanées | 1 |
| Rétention des résultats terminés | 30 jours |
| API demandes | 120 par clé de test par minute |
| Réinitialisation du bac à sable | 3 par jour |

Les tentatives du bac à sable ne réservent jamais de fonds, ne consomment pas les allocations du plan payant, n'écrivent jamais l'utilisation
grands livres, ou générer des frais de fonctionnalités facturables. Reconnexion à la même tentative
ne consomme pas un autre emplacement d'allocation.

Les fonctionnalités externes payantes telles que la surveillance en direct et la vérification d'identité sont
non disponible dans le bac à sable. La livraison et l'enregistrement des e-mails sont désactivés.

## Réinitialiser les données de test {#reset-test-data}

Un administrateur peut utiliser **Réinitialiser le bac à sable** à partir des paramètres du bac à sable jusqu'à trois
fois par jour. Réinitialiser supprime
examens de test, candidats, groupes, devoirs, résultats, configuration du webhook,
les enregistrements de livraison et les fichiers sandbox téléchargés.

La réinitialisation préserve délibérément :

- le locataire du bac à sable ;
- clés `exm_test.` de portée ; et
- l'utilisation actuelle de l'allocation de tentative de 30 jours.

La préservation de l’allocation évite que la réinitialisation ne devienne un moyen de contourner la gratuité.
limite d'utilisation. Révoquez les clés séparément lorsqu’elles ne sont plus nécessaires.

## Conservation et indexation des données {#data-retention-and-indexing}

Les résultats du bac à sable terminés sont automatiquement supprimés après 30 jours. Bac à sable
les pages envoient `X-Robots-Tag: noindex, nofollow` ; le contenu du locataire de test n'est pas destiné
pour l'indexation de la recherche. La documentation publique du développeur reste indexable sur
`docs.examina.io`.

## Flux de travail d'intégration recommandé {#recommended-integration-workflow}

1. Créez avec `https://sandbox.examina.io/api/v1` avec une clé `exm_test.`.
2. Exercez les chemins de réussite, de validation, d’idempotence, de nouvelle tentative et de signature de webhook.
3. Confirmez que votre intégration gère les réponses aux quotas sandbox sans boucles de nouvelle tentative.
4. Créez une clé `exm_live.` distincte avec les étendues minimales requises.
5. Modifiez à la fois l'URL de base et le secret via un déploiement spécifique à l'environnement
   configuration ; ne transformez jamais un jeton de test en un jeton actif.

Pour les demandes prêtes à copier et un premier test complet, suivez les
[bac à sable API démarrage rapide](sandbox-api-quickstart.md).

## Dépanner l'accès {#troubleshoot-access}

Si le transfert automatique expire ou a déjà été utilisé, revenez au live
Page des paramètres **Developer Sandbox** et sélectionnez à nouveau **Ouvrir sandbox**. Un transfert
expire après 90 secondes. La connexion directe à `sandbox.examina.io` reste
disponible comme solution de secours.

Si les appels API renvoient HTTP 429, attendez la période `Retry-After` avant de réessayer.
Utilisez un intervalle exponentiel limité et ne démarrez pas de boucles de nouvelle tentative parallèles.
