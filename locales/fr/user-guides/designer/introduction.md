---
title: Présentation de examina.io Designer
description: Découvrez l'espace de travail Designer et créez un projet d'examen, des
  épreuves, des sections et des questions à transmettre via examina.io.
tags:
- rédaction d'évaluations
- designer
- projet d'examen
- des questions
translation_source: user-guides/designer/introduction.md
translation_source_sha256: 00ffb0a122c3a4edb7cc94fbec1d25afdddeaa592ab5240604581e63c4551fbb
---

# Présentation du Designer {#introducing-designer}

Designer est l'endroit où les examens sont rédigés. Vous construisez un **projet**, mettez un ou plusieurs
**examens** à l'intérieur, divisez chaque examen en **épreuves** et remplissez les épreuves avec
**questions**. Lorsque l'examen est prêt, vous l'envoyez à Manager, où il
est attribué aux personnes et livré.

Designer s’exécute dans le navigateur et ne nécessite aucune installation.

![L'espace de travail Designer sans projet open](../../assets/images/designer/workspace-empty.png)

## L'espace de travail {#the-workspace}

Quatre zones, et elles restent partout au même endroit.

| Zone | Ce qu'il contient |
|---|---|
| **Explorateur d'examens** (en haut à gauche) | L'arborescence du projet : examens, puis épreuves, puis questions |
| **Propriétés** (en bas à gauche) | Paramètres pour tout ce qui est sélectionné dans l'arborescence |
| **Indice** (en bas à gauche) | Explication en anglais simple de la propriété sélectionnée |
| **Volet d'édition** (à droite) | L'examen, l'épreuve ou la question sur laquelle vous travaillez |

Le panneau Indice mérite d'être connu. Sélectionnez n'importe quelle ligne dans Propriétés et elle
explique ce que fait ce paramètre, ce qui est généralement plus rapide que de le rechercher.

## Deux types de fichiers {#two-kinds-of-file}

Cette distinction provoque plus de confusion qu'autre chose dans Designer.
cela vaut la peine d'être clair avant de commencer.

| Fichier | Rallonge | Qu'est-ce que c'est |
|---|---|---|
| **Projet** | `.smexproj` | Votre source modifiable. Contient tous les examens, épreuves et questions, et peut être rouvert et modifié |
| **Examen** | `.smex` | Un seul examen emballé pour la livraison. C'est ce que consomme Manager |

Gardez le projet. Si vous le perdez et ne conservez que l'examen exporté, vous perdez le
possibilité d'éditer confortablement.

## Créer un projet {#create-a-project}

1. Choisissez **Fichier → Nouveau projet d'examen**.
2. Designer crée un **examen sans titre** à l'intérieur.
3. Sélectionnez cet examen dans Exam Explorer pour renseigner ses détails.
4. Choisissez **Fichier → Enregistrer le projet** et conservez le `.smexproj` dans un endroit sûr.

![Le menu Fichier](../../assets/images/designer/file-menu.png)

Notez quels éléments sont grisés et qu'ils se réveillent en deux étapes.
**Enregistrer le projet**, **Enregistrer le projet sous...** et **Nouvel examen** seront disponibles une seule fois.
un projet est ouvert. Les deux actions d'exportation restent désactivées jusqu'à ce que vous
**sélectionnez un examen** dans Exam Explorer, car Designer exporte un examen à la fois.
le temps et a besoin de savoir lequel. Un menu Fichier plein de texte gris n'est pas un défaut - c'est
signifie généralement que rien n'est encore sélectionné.

## Ouvrir un projet existant {#open-an-existing-project}

**Fichier → Ouvrir le projet**, puis choisissez un fichier `.smexproj`.

!!! warning "Les projets d'une version plus récente ne s'ouvriront pas"
    Designer refuse un projet enregistré par une version de l'application ultérieure à celle
    celui que vous dirigez, car il ne peut pas être sûr de comprendre
    tout à l'intérieur. Vous verrez *"La version du fichier est supérieure à la
    version de l'application"*.

    Exportez l'examen à partir de la version qui l'a créé ou demandez à celui qui l'a envoyé
    enregistrer à partir d'une version correspondante.

![L'exemple de projet ouvert, avec son examen dans Exam Explorer](../../assets/images/designer/project-loaded.png)

Les captures d'écran de ces pages utilisent un exemple : un projet nommé
**Examen d'entrée Northgate 2026** avec un seul examen, *entrée Northgate
Examen*, divisé en six épreuves.

## La forme d'un examen {#the-shape-of-an-exam}

Tout dans Designer s'emboîte de la même manière :

```
Project
└── Exam                     one or more
    └── Paper                one or more
        └── Question         one or more
            └── Section      optional grouping within a paper
```

Un **article** correspond généralement à un sujet, un cours ou un module. Un examen avec six épreuves
pourrait être une séance unique couvrant six sujets, avec sa propre durée et
questions posées pour chacun.

## Ajouter un papier {#add-a-paper}

Cliquez avec le bouton droit sur l'examen dans Exam Explorer et choisissez **Nouvelle épreuve d'examen**, puis sélectionnez
le nouveau document pour définir son titre, sa durée et ses instructions. Voir
[Le paper](paper.md) pour ce que fait chaque paramètre.

## Ajouter une question {#add-a-question}

Cliquez avec le bouton droit sur un article et choisissez l'action de nouvelle question, ou utilisez le bouton ci-dessous
Explorateur d'examens. Designer prend en charge :

- Choix multiple, sélection unique
- Choix multiple, sélection multiple
- Remplissez le blanc

Définissez la réponse, le score et la section, puis utilisez **Aperçu** pour voir le
question exactement comme le fera un candidat. Voir [Création de questions](questions.md).

## Un ordre de marche {#a-working-order}

1. Configurez le [exam](exam.md) — titre, code, description, instructions
2. Créez chaque [paper](paper.md) et définissez sa durée
3. Ajoutez des sections si le journal en a besoin
4. Écrivez les [questions](questions.md) ou [importez-les](import-content.md)
5. Aperçu et relecture
6. **Enregistrez le projet**
7. Exportez un examen vers [Manager](../manager/import-exams.md)

Vous pouvez également [réutiliser des documents et des questions](importing-questions.md) d'ailleurs
dans le projet ouvert, [importer le contenu existant](import-content.md) depuis un autre
projet ou un document, ou créez des brouillons à partir de vos propres sources avec
[Création IA](ai-question-authoring.md).
