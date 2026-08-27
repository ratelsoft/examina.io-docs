---
title: Intégrer l'application client examina.io
description: Ajoutez un examen examina.io à votre site Web avec le widget Client,
  les domaines approuvés, le dimensionnement réactif et la connexion automatique sécurisée
  en option.
tags:
- widget client
- intégrer l'examen
- intégration des examens
- iframe
- javascript
translation_source: integrations/embedding-client-app.md
translation_source_sha256: 6f480dd668adcac7c3052eb0cb74773a0e6581bfcdc08141f994a2c9e426827a
---

# Intégrez l'application Client sur votre site Web {#embed-the-client-app-on-your-website}

Le widget Client remplace un lien d'examen par une iframe afin que les candidats puissent passer un
évaluation sur un site Web approuvé.

Il vous faut :

- un compte et un forfait examina.io prenant en charge l'intégration ;
- accès à **Accueil → Paramètres** ;
- un examen importé dans Manager ;
- autorisation de modifier le site Web hébergeur ; et
- connaissances de base du HTML.

## 1. Créez une clé publique API {#1-create-a-public-api-key}

Ouvrez **Accueil → Paramètres → Clés et webhook API** et créez une **Clé publique API**.

![La zone clé API dans Paramètres de l'organisation](../assets/images/embedding-client-app/api_section_1.jpg)

L'intégration simple utilise uniquement la clé publique. Ne placez pas la clé secrète API dans
code du navigateur.

La régénération de la clé publique nécessite que chaque installation de widget soit mise à jour.

## 2. Approuver le domaine du site Web {#2-approve-the-website-domain}

Dans **Domaines et sous-domaines approuvés pour l'intégration du widget client** :

1. Entrez le nom d'hôte sans protocole ni chemin.
2. Sélectionnez **Ajouter un domaine**.

Par exemple, saisissez `assessment.example.edu`, et non
`https://assessment.example.edu/exams`.

![La liste des domaines approuvés pour le widget Client](../assets/images/embedding-client-app/domain_section.jpg)

Pour les tests locaux, ajoutez le nom d'hôte que vous utilisez réellement, tel que `localhost` ou
`127.0.0.1` ; N'inclut pas le port. Supprimez les hôtes de développement après les tests.
Évitez d'autoriser tous les domaines en production.

## 3. Chargez le script du widget {#3-load-the-widget-script}

Ajoutez le script du widget à la page et remplacez `YOUR_PUBLIC_API_KEY` :

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Take the assessment</title>
  <script
    src="https://www.examina.io/client/widget.js?apiKey=YOUR_PUBLIC_API_KEY">
  </script>
</head>
<body>
  <h1>Readiness assessment</h1>
</body>
</html>
```

Si la clé est manquante ou invalide, le script du widget ne se chargera pas correctement.

## 4. Ajoutez le lien de l'examen {#4-add-the-exam-link}

Dans Manager, sélectionnez l'examen et choisissez **Ouvrir le lien d'examen**. Copiez l'URL.

![Trouvez le lien de l'examen dans Manager](../assets/images/embedding-client-app/manager_exam_details.jpg)

Ajoutez le lien avec la classe `examina-io-client-widget` :

```html
<a
  class="examina-io-client-widget"
  href="https://www.examina.io/client/YOUR_EXAM_ID">
  Open the exam
</a>
```

Lorsque JavaScript est disponible, le widget remplace l'ancre par le
Cliente. Le texte d'ancrage reste une solution de secours utile si le script ne peut pas s'exécuter.
Placez une seule ancre de widget sur une page.

## Contrôler les dimensions du widget {#control-the-widget-dimensions}

Le widget utilise ces attributs facultatifs :

- `data-examina-io-height`
- `data-examina-io-width`

Si un attribut est omis, le widget gère cette dimension par rapport au
fenêtre du navigateur et peut l'ajuster lorsque la fenêtre est redimensionnée.

Utilisation :

- un nombre positif pour une dimension de pixel fixe ;
- un nombre négatif pour utiliser la taille de la fenêtre moins ce nombre de pixels ; ou
- `auto` pour laisser cette dimension aux paramètres par défaut de votre CSS ou de votre navigateur.

Cet exemple réserve 64 pixels pour un en-tête de page et laisse CSS gérer la largeur :

```html
<header class="exam-header">Readiness assessment</header>
<a
  class="examina-io-client-widget"
  href="https://www.examina.io/client/YOUR_EXAM_ID"
  data-examina-io-height="-64"
  data-examina-io-width="auto">
  Open the exam
</a>
```

Testez dans la plus petite fenêtre prise en charge. Lorsque vous utilisez `auto`, appliquez un
Taille CSS à la mise en page résultante afin que la taille iframe par défaut du navigateur ne soit pas
utilisé accidentellement.

## Exemple réactif complet {#complete-responsive-example}

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Readiness assessment</title>
  <script
    src="https://www.examina.io/client/widget.js?apiKey=YOUR_PUBLIC_API_KEY">
  </script>
  <style>
    html, body { margin: 0; }
    .exam-header { box-sizing: border-box; height: 64px; padding: 20px; }
  </style>
</head>
<body>
  <header class="exam-header">Readiness assessment</header>
  <a
    class="examina-io-client-widget"
    href="https://www.examina.io/client/YOUR_EXAM_ID"
    data-examina-io-height="-64"
    data-examina-io-width="auto">
    Open the exam
  </a>
</body>
</html>
```

## Connexion automatique facultative {#optional-autologin}

Si votre propre site a déjà authentifié le candidat, votre backend peut
demandez un jeton de connexion à l'examen de courte durée et ajoutez-le au lien client. Le API
La clé secrète doit rester sur votre serveur.

Flux back-end :

1. Authentifiez la personne dans votre candidature.
2. Résolvez leur code ou identifiant de candidat examina.io sur le serveur.
3. Depuis votre serveur, appelez l'un des points de terminaison de jeton documentés avec HTTPS.
   Authentification de base :
   - `/login/exam/{examId}/code/{examineeCode}/token`
   - `/login/exam/{examId}/id/{examineeId}/token`
4. Créez l'URL du client avec des valeurs de requête codées en URL.
5. Renvoyez la clé publique et l'URL de connexion limitée dans le temps sur la page approuvée.

Exemple de forme de lien :

```html
<a
  class="examina-io-client-widget"
  href="https://www.examina.io/client/YOUR_EXAM_ID?autologin=true&amp;examineeCode=URL_ENCODED_CODE&amp;token=URL_ENCODED_TOKEN"
  data-examina-io-height="-64"
  data-examina-io-width="auto">
  Open the exam
</a>
```

`autologin` doit être `true`. Fournissez soit `examineeCode` ou `examineeId` ;
lorsque les deux sont présents, le Client utilise le code du candidat.

Ne générez jamais de jetons dans le navigateur JavaScript, exposez la clé secrète au
candidat, ou enregistrez une URL de connexion automatique complète.

## Liste de contrôle de production {#production-checklist}

- Le nom d'hôte de production exact est approuvé.
- La page et toutes les ressources intégrées utilisent HTTPS.
- La clé secrète API est absente des requêtes réseau de la source de la page et du navigateur.
- Le lien de secours est compréhensible.
- Un widget est présent sur la page.
- Le comportement du bureau, du mobile, du clavier et du redimensionnement a été testé.
- Un candidat cartographié fictif peut se connecter ou se connecter automatiquement et terminer l'examen.
- Les domaines de développement temporaires ont été supprimés.

Pour la configuration et la rotation des informations d'identification, voir [Clés API et
webhooks](api-keys-and-webhooks.md). Pour les schémas de point de terminaison, utilisez le fichier [API
référence](../api/index.md).
