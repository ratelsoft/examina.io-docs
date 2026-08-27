---
title: examina.io Manager Aperçu
description: Découvrez l'espace de travail Manager pour importer des examens, ajouter
  des candidats, créer des groupes, attribuer des épreuves et fournir des évaluations
  en ligne.
tags:
- administration des examens
- candidats
- groupes
- directeur
- examens en ligne
translation_source: user-guides/manager/overview.md
translation_source_sha256: 064981fbf11037a6fd4873c66300be0a0d1d535abaeb14cb85ec1fa1d960b9c3
---

# Aperçu du Manager {#manager-overview}

Manager est l’espace de travail d’administration des examens. Il connecte un examen exporté avec
dossiers des candidats, devoirs des papiers, paramètres de livraison, suivi et
résultats.

## Ouvrir Manager {#open-manager}

Connectez-vous, ouvrez **Accueil** et sélectionnez **Manager** dans la galerie d'applications. Régulier,
Les utilisateurs administrateur et root peuvent ouvrir Manager, mais les examens et les candidats
ils peuvent accéder peut être limité par [Circles](../administration/circles-and-permissions.md).

## Espace de travail principal {#main-workspace}

![L'espace de travail Manager avec l'onglet Examens sélectionné](../../assets/images/manager/exams-tab.png)

Manager comporte trois onglets de ressources :

- **Exams** répertorie les évaluations importées.
- **Les candidats** répertorient les candidats qui peuvent être mappés aux examens.
- **Groupes** répertorie les collections réutilisables de candidats.

Sélectionnez un élément dans le panneau de gauche pour ouvrir ses détails et les actions disponibles. Le
la petite barre d'outils au-dessus de chaque liste ajoute un nouvel enregistrement, passe à une vue tabulaire et
s'actualise depuis le serveur. Actualisez chaque fois qu'un autre utilisateur a modifié les données.

Le menu **Fichier** contient les quatre commandes de création, et ce sont les mêmes
quel que soit l'onglet sur lequel vous vous trouvez :

![Le menu Fichier Manager](../../assets/images/manager/file-menu.png)

- **Ajouter un nouvel examen**
- **Ajouter un nouveau candidat**
- **Importer les candidats depuis un fichier/Excel**
- **Créer un nouveau groupe**

## Séquence opératoire recommandée {#recommended-operating-sequence}

1. [Importez l'examen ](import-exams.md).
2. [Ajouter ou importer des candidats](examinees.md).
3. Créez éventuellement des groupes.
4. [Attribuez des candidats ou des groupes](groups-and-assignments.md) à l'examen et à ses
   papiers.
5. Examinez la visibilité, l'affichage des résultats, la surveillance, l'identité, l'appareil et
   paramètres de déconnexion.
6. Testez le lien d'examen avec un candidat désigné.
7. Publier et communiquer l'examen.
8. [Surveiller la session et générer les résultats](deliver-monitor-report.md).

## Examens {#exams}

![Un examen sélectionné, avec ses paramètres et les candidats cartographiés](../../assets/images/manager/exam-details.png)

Un dossier d'examen indique son titre, son code et sa version, le lien utilisé par les candidats,
visibilité, si les résultats sont affichés après l'examen, si la surveillance en direct
et la prévérification de l'eFace ID sont activés, l'heure à laquelle il a été ajouté, le numéro importé
la taille du fichier et le flux de papier. Les actions d'examen peuvent inclure :

- cartographier les candidats ou les groupes ;
- ouvrir le lien de l'examen ;
- envoyer un e-mail aux candidats cartographiés ;
- basculer la visibilité ou l'affichage des résultats ;
- configurer la surveillance en direct et la vérification d'identité ;
- démarrer, arrêter ou surveiller un examen éligible ;
- gérer les autorisations et les paramètres de livraison ; et
- afficher les résultats ou générer des rapports.

Les actions disponibles dépendent du type d'examen, du rôle du compte, du plan et de l'examen en cours.
état.

## Candidats {#examinees}

![Un candidat sélectionné, avec des examens cartographiés et une appartenance à un groupe](../../assets/images/manager/examinee-details.png)

Un dossier de candidat stocke un code ou identifiant unique, un mot de passe, un nom, un sexe et
détails facultatifs tels que l’e-mail, le numéro de téléphone, la date de naissance et la photographie.
Sous les détails se trouvent deux panneaux : les examens auxquels cette personne est associée et le
Groupes auxquels ils appartiennent. De là, vous pouvez gérer l'adhésion au groupe, planifier un examen
et des articles, examinez les détails du mappage et affichez un résultat final.

## Groupes {#groups}

![Un groupe sélectionné, listant ses membres](../../assets/images/manager/group-details.png)

Un groupe est un ensemble opérationnel de candidats, tel qu'une classe, une cohorte ou
séance d'examen. Mapper un groupe à un examen applique l'affectation au groupe.
membres actuels qui ne sont pas déjà cartographiés.

Les groupes sont différents des cercles : les groupes facilitent le travail groupé des candidats ;
Des cercles contrôlent l’accès du personnel.

## Pratiques de préparation sécuritaires {#safe-preparation-practices}

- Gardez un examen invisible jusqu'à ce que le contenu, les devoirs et les paramètres soient vérifiés.
- Utilisez des codes de candidat uniques et un canal sécurisé pour les codes d'accès.
- Vérifiez le fuseau horaire chaque fois qu'une mission comprend une heure de début.
- Test avec des données de test fictives ou approuvées.
- Actualisez avant d'agir sur l'état de la connexion ou les résultats.
- Considérez les actions **Effacer le résultat**, la suppression et la régénération des clés comme sensibles.

## Prochaines étapes {#next-steps}

Si vous disposez déjà d'une exportation Designer, continuez avec [Importer
examens](import-exams.md). Si l'examen est présent, allez dans [Ajouter et importer
candidats](examinees.md).
