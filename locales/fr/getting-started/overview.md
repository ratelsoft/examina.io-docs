---
title: Présentation de la plateforme examina.io
description: Comprenez comment Designer, Manager, Proctor, Client, utilisateurs, groupes
  et cercles travaillent ensemble dans le cycle de vie de l'évaluation examina.io.
tags:
- plateforme d'évaluation
- client
- designer
- candidats
- examens
- directeur
- surveillance
translation_source: getting-started/overview.md
translation_source_sha256: 3758552e04cfd298de85e07c2a290dd7c4675706cab28137e1fb9cf0b0dae7ca
---

# Comprendre la plateforme examina.io {#understand-the-examinaio-platform}

Le examina.io divise le travail d'évaluation en applications ciblées. Question
les auteurs peuvent créer du contenu sans accès aux dossiers des candidats, aux administrateurs
peuvent planifier et dispenser des examens, les surveillants ne peuvent superviser que les examens qu'ils
sont attribués et les candidats utilisent une application client dédiée.

![La galerie d'applications examina.io affiche Designer, Manager et Client](../assets/images/dashboard/apps-gallery.png).

## Flux de travail d'évaluation {#assessment-workflow}

1. **Créez** un projet d'examen, des épreuves, des sections et des questions dans Designer.
2. **Exportez** l'examen terminé sous forme de fichier `.smex`.
3. **Importez** ce fichier dans Manager.
4. **Ajoutez des candidats** individuellement ou importez-les depuis Excel, CSV ou texte.
5. **Organiser et attribuer** les candidats avec des groupes, des mappages d'examen et des documents
   cartographies.
6. **Configurer les options de livraison** telles que la visibilité, l'heure de début, le résultat
   affichage, appareils pris en charge, vérification d’identité et surveillance en direct.
7. **Partagez le lien de l'examen** ou envoyez un e-mail depuis Manager.
8. **Surveiller et signaler** pendant que l'examen est actif et une fois qu'il est terminé.

Une même personne peut réaliser plusieurs étapes dans une petite organisation. Plus grand
les organisations peuvent séparer les responsabilités avec [les rôles de compte et
Cercles](roles-and-permissions.md).

## Designer {#designer}

Designer est l'application de création d'examens. Utilisez-le pour créer des projets d'examen,
organiser un ou plusieurs articles, ajouter des sections, rédiger des questions, définir une notation et
règles de timing et importer le contenu des questions existantes.

![La même question dans le volet d'édition et le volet d'aperçu Designer](../assets/images/general/designer-edit-preview.png)

Une fois la création terminée, exportez l'examen sous forme de fichier `.smex` crypté pour
livraison via Manager. Commencez par [Présentation de Designer](../user-guides/designer/introduction.md).

## Manager {#manager}

Manager connecte le contenu de l'examen aux personnes qui le passent. Administrateurs et
le personnel autorisé utilise le Manager pour :

- importer des fichiers d'examen `.smex` ;
- créer ou importer des dossiers de candidats ;
- organiser les candidats en groupes ;
- mapper les candidats ou les groupes à un examen et à ses épreuves ;
- contrôler la visibilité des examens et les paramètres de livraison ;
- ouvrir ou diffuser un lien d'examen ; et
- suivre les progrès et générer des résultats ou des rapports.

![Un examen dans Manager, avec ses candidats mappés](../assets/images/manager/exam-details.png)

Voir la [Présentation de Manager](../user-guides/manager/overview.md) pour les informations principales
navigation et une séquence de fonctionnement recommandée.

## Procureur {#proctor}

Proctor est l'espace de travail de surveillance en direct. Lorsque la surveillance en direct est activée pour
un examen, les surveillants autorisés peuvent examiner l'audio, la webcam et
filtrer les flux, communiquer avec un candidat et approuver le début d'un examen lorsque
le flux de travail configuré l'exige.

![L'espace de travail Proctor, une vignette par candidat](../assets/images/general/proctoring-view.png)

Chaque candidat connecté apparaît sous la forme d'une vignette avec des vues Détails, Webcam et Écran,
commandes d'enregistrement et de sourdine, ainsi qu'une boîte de message direct.

Activez uniquement les fonctionnalités de surveillance que votre organisation est autorisée à utiliser,
et informer les candidats des données qui seront collectées.

## Client {#client}

Le client est l’application destinée aux candidats. Les candidats ouvrent le lien de l'examen, saisissent
leurs informations d'identification attribuées, effectuer tous les contrôles de système ou d'identité requis,
et prenez les papiers cartographiés.

![L'application client destinée aux candidats](../assets/images/client/question.png)

Le client enregistre périodiquement l'état de l'examen lorsqu'une connexion est disponible. Le
[guide du jour du test](../user-guides/client/take-an-exam.md) explique comment les candidats
doit se préparer et que faire si une connexion est interrompue.

## Utilisateurs, groupes et cercles {#users-groups-and-circles}

Ces concepts d’apparence similaire résolvent différents problèmes :

| Concepts | Objectif |
| --- | --- |
| **Utilisateur** | Un compte personnel qui se connecte à examina.io, tel qu'un administrateur, un coordinateur d'examen ou un surveillant. |
| **Candidat** | Un candidat ou un étudiant qui se connecte via un lien d’examen pour passer une évaluation. |
| **Groupe** | Une collection réutilisable de candidats, utilisée pour les examens en masse et les devoirs papier. |
| **Cercle** | Une limite d'autorisation qui connecte les utilisateurs sélectionnés aux examens et aux candidats sélectionnés. |

Utilisez les groupes pour réduire les tâches répétitives. Utilisez les cercles pour restreindre ce qui
le personnel peut voir et gérer. Apprenez-en davantage dans [Groupes et examens
affectations](../user-guides/manager/groups-and-assignments.md) et [Cercles et
autorisations](../user-guides/administration/circles-and-permissions.md).

## Intégrations {#integrations}

Les organisations peuvent connecter le examina.io à d'autres systèmes avec :

- clés publiques et secrètes API ;
- un webhook de complétion ;
- le widget Client intégrable ;
- le REST API ; et
- Intégrations de plateforme d'apprentissage prises en charge affichées dans Paramètres.

Commencez par [API clés et webhooks](../integrations/api-keys-and-webhooks.md) ou
accédez directement à la [référence API](../api/index.md).

## Étape suivante {#next-step}

Suivez le [démarrage rapide](quick-start.md) pour une liste de contrôle pratique pour le premier examen.
