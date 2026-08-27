---
title: Importer un examen dans examina.io Manager
description: Exportez une évaluation .smex depuis Designer, importez-la dans Manager
  et vérifiez l'examen avant d'attribuer des candidats.
tags:
- exportation de créateurs
- importation d'examen
- directeur
- sexe
translation_source: user-guides/manager/import-exams.md
translation_source_sha256: cdd0384f56afe40f416a9be4f57bf31c41f1b3b32098cafb860f785f7f9aa421
---

# Importer un examen dans Manager {#import-an-exam-into-manager}

Manager accepte les packages d'examen exportés par Designer sous forme de fichiers `.smex`. Importer
le package avant d’ajouter des devoirs ou de partager un lien d’examen.

## Avant d'importer {#before-you-import}

Dans Designer, confirmez :

- le titre et le code de l'examen sont corrects ;
- chaque article contient les questions prévues ;
- la durée du papier et les paramètres de questions-réponses sont corrects ;
- la notation et les bonnes réponses ont été revues ;
- les instructions et règles de navigation sont complètes ; et
- le projet a été sauvegardé avant l'export.

Conservez le projet source comme maître modifiable. Le fichier `.smex` exporté est
le colis de livraison.

## Importer le fichier {#import-the-file}

![Fichier → Ajouter un nouvel examen](../../assets/images/manager/file-menu.png)

1. Ouvrez **Manager**.
2. Sélectionnez **Fichier → Ajouter un nouvel examen**.
3. Faites glisser le fichier `.smex` dans la zone de téléchargement ou sélectionnez-le avec le fichier
   sélecteur.
4. Soumettez le téléchargement.
5. Attendez le message de réussite contenant le code et le titre de l'examen importé.

Si Manager signale que le type de fichier n'est pas pris en charge, revenez à Designer et
exportez l’examen au format `.smex` pris en charge. Si le fichier dépasse la
taille autorisée pour votre environnement ou plan, réduisez les ressources multimédias volumineuses et exportez
encore une fois.

## Vérifier l'examen importé {#verify-the-imported-exam}

Sélectionnez l'examen et consultez son panneau de détails :

![Détails de l'examen importé](../../assets/images/manager/exam-details.png)

- titre, code et version de l'examen ;
- le flux des copies d'examen ;
- visibilité ;
- taille du fichier importé ; et
- l'heure à laquelle il a été ajouté.

**Taille du fichier d'examen** est le contrôle d'intégrité le plus rapide que le bon package
arrivé — un chiffre beaucoup plus petit que prévu signifie généralement une exportation qui est
il lui manque ses médias.

Ouvrez les informations papier et comparez-les avec le projet Designer. Ne pas cartographier
de vrais candidats jusqu'à ce que le contenu et le timing soient corrects.

## Mettre à jour un examen en toute sécurité {#update-an-exam-safely}

Si le contenu change après l'importation :

1. Mettez à jour et validez le projet source dans Designer.
2. Exportez un nouveau fichier de livraison.
3. Importez-le selon le processus de changement de votre organisation.
4. Revérifiez les mappages, la visibilité, la surveillance et la communication avant la publication.

Ne présumez pas qu'un fichier nouvellement exporté conservera tous les éléments côté livraison.
réglage. Vérifiez l'enregistrement Manager et testez le parcours client après tout
remplacement ou changement de version.

## Continuer la configuration {#continue-setup}

Ensuite, [ajoutez ou importez les candidats](examinees.md), puis [cartographiez les personnes et
papiers](groups-and-assignments.md).
