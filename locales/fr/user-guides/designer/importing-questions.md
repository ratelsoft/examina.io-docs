---
title: Réutiliser le contenu dans examina.io Designer
description: Ouvrez les projets Designer enregistrés, dupliquez les articles et les
  questions et créez une copie sécurisée avant d'adapter le contenu de l'évaluation
  existant.
tags:
- designer
- projet d'examen
- réutiliser les questions
- papier en double
translation_source: user-guides/designer/importing-questions.md
translation_source_sha256: ad794a24b9de67ecc26f9ce8f44b4f07e6d27ebf81ecfb8b5b853c0e32ff054c
---

# Réutiliser le contenu du projet {#reuse-project-content}

Designer peut rouvrir un projet `.smexproj` modifiable et dupliquer des documents ou
questions à l’intérieur du projet ouvert. Ce sont les moyens pris en charge pour s'adapter
contenu existant dans la version actuelle.

## Ouvrir un projet enregistré {#open-a-saved-project}

1. Sélectionnez **Fichier → Ouvrir le projet**.
2. Choisissez le fichier `.smexproj` enregistré par Designer.
3. Consultez ses examens, ses épreuves et ses questions dans **Exam Explorer**.
4. Sélectionnez **Fichier → Enregistrer le projet sous** avant d'apporter des modifications substantielles.

Le fichier modifiable `.smexproj` est différent du package de livraison `.smex`
exporté pour Manager. Ouvrez le fichier de projet dans Designer ; importer la livraison
package dans Manager.

## Dupliquer un papier {#duplicate-a-paper}

1. Cliquez avec le bouton droit sur le papier source et sélectionnez **Copier**.
2. Cliquez avec le bouton droit sur l'examen de destination et sélectionnez **Coller le papier**.
3. Renommez la nouvelle épreuve afin que son titre soit unique au sein de l'examen.
4. Révisez la durée, les instructions, les sections, la sélection de questions et la calculatrice
   paramètres.

La copie reste modifiable et n'altère pas le papier source.

## Dupliquer une question {#duplicate-a-question}

1. Cliquez avec le bouton droit sur la question source et sélectionnez **Copier**.
2. Cliquez avec le bouton droit sur le papier de destination et sélectionnez **Coller la question**.
3. Mettez à jour l'invite, la réponse, le score et la section selon vos besoins.
4. Prévisualisez la question copiée avant l'exportation.

Le copier-coller fonctionne dans le projet actuellement ouvert.

## Contenu extérieur à ce projet {#content-from-outside-this-project}

Pour importer des examens d'un autre projet, des copies d'un examen exporté ou
questions saisies dans un document Word, RTF ou texte, utilisez l'assistant d'importation
au lieu de copier-coller. Voir [Importer du contenu existant](import-content.md).

## Valider le contenu réutilisé {#validate-reused-content}

Après avoir copié le contenu :

1. vérifier les titres d'examen ou d'épreuve en double ;
2. vérifier le type de question, la réponse, le score et la section ;
3. prévisualisez le formatage, les équations, les images et l'audio ;
4. revérifier la durée des épreuves et le nombre de questions-réponses ;
5. relire les instructions ; et
6. enregistrez le projet sous un nouveau nom avant l'exportation.
