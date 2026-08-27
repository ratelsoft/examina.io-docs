---
title: Paramètres de l'organisation, image de marque et intégrations
description: Configurez les domaines approuvés, la page de connexion, le logo, les clés API, les webhooks et les intégrations LMS dans examina.io.
tags:
- paramètres de l'API
- image de marque
- intégrer des domaines
- paramètres de l'organisation
- webhook
translation_source: user-guides/administration/organization-settings.md
translation_source_sha256: 551087143ecc0eaf4a63a442e2ff2f2373d7c666d9cd232732c011d7788432d4
---

# Paramètres de l'organisation et image de marque {#organization-settings-and-branding}

Les comptes racine et administrateur peuvent ouvrir **Accueil → Paramètres** pour gérer
image de marque à l'échelle de l'organisation, domaines intégrés, informations d'identification API, livraison de webhooks,
et prise en charge des connexions avec la plateforme d'apprentissage.

![Paramètres de l'organisation pour les domaines, la marque, les clés API et le webhook](../../assets/images/administration/organization-settings.png)

## Domaines d'intégration approuvés {#approved-embed-domains}

La liste d'autorisation du domaine contrôle quels sites peuvent charger le widget Client.

1. Entrez uniquement le nom d'hôte, sans **http://** ou **https://**.
2. Sélectionnez **Ajouter un domaine**.
3. Supprimez les domaines qui ne sont plus utilisés.

Par exemple, saisissez **assessment.example.edu**, et non
**https://assessment.example.edu/exams**.

Évitez **Autoriser tous les domaines** en production. Si vous ajoutez
**localhost** ou un autre hôte de développement, supprimez-le après le test car il
n'est pas exclusif à votre organisation.

Voir [Intégrer l'application client](../../integrations/embedding-client-app.md).

## Logo de l'organisation {#organization-logo}

Le panneau **Personnalisation du logo** contrôle le logo affiché dans les formats pris en charge.
points de vue orientés vers l’organisation et vers les candidats. Sélectionnez **Télécharger un nouveau logo** et
choisissez un fichier JPG, GIF ou PNG jusqu'à 512 Ko.

Utilisez un logo très contrasté avec un rembourrage transparent ou neutre, puis vérifiez-le sur
écrans de bureau et de taille mobile.

## Page de connexion à l'examen {#exam-login-page}

Dans le panneau **Expérience client**, définissez **Vue de connexion à l'examen** sur **Par défaut**,
**Moderne** ou **Classique**.
Moderne et Classique peuvent utiliser une image d’arrière-plan d’organisation. Si aucun n'est
fourni, le client peut afficher un arrière-plan fourni.

1. Choisissez une vue de connexion et sélectionnez **Enregistrer le style**.
2. Sélectionnez **Modifier l'image** pour télécharger un arrière-plan JPG, GIF ou PNG.
3. Utilisez une image de 1920 × 1280 pixels lorsque cela est possible et conservez-la dans les limites affichées.
   limite de taille.
4. Sélectionnez **Page de connexion à l'examen de test** et vérifiez la lisibilité, l'emplacement du logo et
   comportement mobile.

Voir [Personnaliser la page de connexion à l'examen](../client/custom-login-page.md).

## Clés API {#api-keys}

La **clé publique API** peut identifier les intégrations de navigateur approuvées telles que
Widget client. La **clé secrète API** authentifie les requêtes de serveur à serveur
et ne doit jamais être inclus dans le JavaScript du navigateur, le code source public, un mobile
des captures d'écran de l'application ou de la documentation.

Le secret n'est affiché qu'une seule fois lors de sa création. Conservez-le immédiatement dans
un gestionnaire secret agréé. La régénération d'une clé peut casser les intégrations existantes
jusqu'à ce que chaque consommateur soit mis à jour.

Voir [Clés API et webhooks](../../integrations/api-keys-and-webhooks.md).

## Webhook d'achèvement {#completion-webhook}

Saisissez une URL de rappel HTTPS pour recevoir une notification lorsqu'un examen est terminé.
terminé. Le point de terminaison doit valider les demandes conformément au API actuel
contrat, renvoyer une réponse positive rapidement et traiter un travail long
de manière asynchrone.

N'utilisez pas de page d'administration privée ou d'URL contenant des informations d'identification comme
URL du webhook.

## Intégrations de plateformes d'apprentissage {#learning-platform-integrations}

Les paramètres peuvent afficher les connecteurs de plateforme d’apprentissage et les inscriptions LTI 1.3.
Les exigences de disponibilité et de configuration dépendent de votre forfait et du réseau externe.
configuration de la plateforme. Pour connaître les flux complets de configuration et de validation, voir
[Intégrez examina.io avec Moodle](../../integrations/moodle-lms.md) et
[Intégrez examina.io avec Canvas](../../integrations/canvas-lms.md), ou
[Intégrez examina.io avec Blackboard Apprenez Ultra](../../integrations/blackboard-lms.md).

Utilisez un compte d'intégration dédié le cas échéant, subvention uniquement requise
autorisations, documenter le propriétaire et déconnecter les intégrations qui ne sont plus
utilisé.

## Liste de contrôle pour le contrôle des changements {#change-control-checklist}

Après avoir modifié les paramètres de l'organisation :

1. tester la page de connexion avec un examen désigné ;
2. tester chaque domaine d'intégration de production ;
3. Vérifiez les consommateurs API si une clé a été modifiée ;
4. envoyez un événement de test via votre flux de travail webhook lorsqu'il est disponible ; et
5. Enregistrez le plan de changement et de restauration pour les environnements à enjeux élevés.
