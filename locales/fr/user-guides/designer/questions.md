---
title: Créer des questions dans examina.io Designer
description: Créez des QCM et des textes à trous, définissez les réponses, ajoutez des passages et des médias, puis prévisualisez dans Designer.
tags:
- designer
- questions d'examen
- remplis le vide
- choix multiple
- rédaction de questions
translation_source: user-guides/designer/questions.md
translation_source_sha256: 71aabc22c0127ffc08edfbcaf9305cadb7e175e8b8f56eedc47405e4faf982f9
---

# Créer des questions dans Designer {#create-questions-in-designer}

Les questions appartiennent à un article et, lorsqu'il existe des sections, à une section de celui-ci.
papier.

## Ajouter une question {#add-a-question}

1. Ouvrez un projet d'examen et créez une épreuve.
2. Cliquez avec le bouton droit sur le document et choisissez l'action de nouvelle question, ou sélectionnez **Nouveau
   Question** sous l'Explorateur d'examens.
3. Choisissez un type de question.
4. Entrez l'invite, les choix de réponse ou les réponses acceptées, et facultatif
   explication.
5. Définissez les propriétés de la question.
6. Ouvrez **Aperçu** et vérifiez le résultat.
7. Enregistrez le projet.

## Types de questions {#question-types}

Designer prend en charge :

- **Choix multiple — sélection unique :** une option est correcte.
- **Choix multiple — sélection multiple :** plusieurs options peuvent être correctes.
- **Remplissez le blanc :** le candidat saisit un texte qui est évalué par rapport au
  règles de réponse configurées.

Choisissez le type qui mesure la compétence souhaitée. Ne transformez pas une réponse multiple
élément en sélection unique simplement pour simplifier le marquage.

## Propriétés principales {#core-properties}

**Nombre d'options**

: Définit le nombre d'options à choix multiples. La plage prise en charge est de 2 à 10.

**Option correcte**

: Identifie la bonne réponse pour un élément à sélection unique. Éléments à sélection multiple
  permettre les bons choix applicables.

**Autoriser les choix aléatoires**

: Randomise l'ordre des options dans le client tout en préservant quelle option est correcte.
  Évitez de mélanger les choix tels que « tout ce qui précède » qui dépendent de la position.

**Section des questions**

: affecte la question à une section. Créer les sections papier requises
  avant de poser des questions.

**Score/Valeur de la question**

: Définit la note attribuée pour la question. Les valeurs décimales telles que 0,5 sont
  pris en charge.

## Études de cas et passages {#case-studies-and-passages}

Activer **Ajouter une étude de cas/un passage** lorsqu'une invite dépend d'une lecture partagée
matériel, une exposition, un scénario ou un énoncé de problème. Utiliser **Étude de cas
Étiquette** pour remplacer l'étiquette par défaut par un nom plus clair tel que
**Passage de compréhension**.

Si plusieurs questions utilisent le même passage, conservez la formulation et la mise en forme
cohérent et prévisualisez chaque question.

## Modifier et prévisualiser le contenu {#edit-and-preview-content}

Le volet Modifier prend en charge le formatage du texte, les titres, la couleur, les listes, l'alignement,
exposant, indice, symboles, expressions, images, audio et tableaux.

![L'éditeur de questions, avec instructions, questions, options et explication](../../assets/images/designer/question-editor.png)

Utilisez le formatage pour améliorer la structure, pas la décoration. Confirmez que c'est important
le sens n’est pas communiqué uniquement par la couleur.

### Images {#images}

Conservez une image importée dans les limites indiquées par Designer. L'éditeur existant
les conseils recommandent de ne pas dépasser 650 pixels de large et 500 Ko pour que l'image
rendu fiable sur les ordinateurs de bureau et les appareils mobiles.

Redimensionnez et compressez les grandes images avant l'importation. Ajoutez suffisamment de mots dans le
question pour que le but de l'image reste compréhensible.

### Audio {#audio}

Les éléments audio peuvent prendre en charge les questions d’écoute. Configurer le volume disponible,
faites une pause, arrêtez-vous et recherchez des contrôles correspondant aux règles d’évaluation.

Testez avec des écouteurs et la bande passante la plus faible attendue le jour de l'examen. Fournir un
parcours d'hébergement approuvé lorsque cela est nécessaire.

### Tableaux {#tables}

Utilisez l'outil Tableau pour ajouter des lignes et des colonnes.

Pour modifier ou supprimer un tableau, cliquez dessus avec le bouton droit et ouvrez les **Propriétés du tableau**.

Gardez les tableaux suffisamment petits pour s'adapter aux écrans pris en charge sans défilement horizontal.

## Aperçu et contrôle qualité {#preview-and-quality-check}

Sélectionnez **Aperçu** pour inspecter l'invite et les options affichées.

![L'aperçu montre la question telle que le candidat la verra](../../assets/images/designer/question-preview.png)

Avant l'exportation, vérifiez :

- l'invite a une interprétation défendable ;
- la bonne réponse et le score sont définis ;
- les éléments de distraction sont plausibles et ne sont pas révélés accidentellement ;
- l'affectation des sections est correcte ;
- les options mélangées restent significatives ;
- le média se charge et est lisible ou audible ;
- l'orthographe, la grammaire et la notation mathématique sont correctes ; et
- la question fonctionne avec la plus petite taille d'écran autorisée.

Pour réutiliser le contenu existant, voir [Réutiliser le contenu du projet](importing-questions.md).
Pour importer des questions à partir d'un document ou d'un autre projet, voir [Importer des questions existantes
contenu](import-content.md).
