---
title: Importer du contenu existant dans examina.io Designer
description: Importez des examens d'un autre projet Designer, des articles et des
  questions d'un examen exporté, ainsi que des questions rédigées dans un document
  Word, RTF ou texte.
tags:
- designer
- questions d'importation
- importer des examens
- importation docx
- marqueurs d'interrogation
translation_source: user-guides/designer/import-content.md
translation_source_sha256: c9b2db78d897346026145e29d1812f83ea750b4e7119666b47bf640ca03d94df
---

# Importer du contenu existant {#import-existing-content}

Designer peut reprendre le contenu d'un autre projet Designer, d'un examen déjà
exportés pour livraison, ou à partir d'un document de traitement de texte dans lequel les questions
sont tapés. Tous les trois exécutent le même assistant : choisissez un fichier, dites-le
Designer comment le document est présenté, puis cochez ce que vous voulez. Où tu
commencé décide de ce que vous êtes autorisé à apporter.

## Ce que Designer accepte {#what-designer-accepts}

Un fichier de projet `.smexproj` et un examen exporté `.smex` sont lus directement, car
leur contenu est déjà structuré. Un document `.txt`, `.rtf` ou `.docx` est
lu sous forme de texte, donc Designer a besoin du marqueur et des balises ci-dessous pour trouver où chaque
la question commence. `.doc` n'est pas pris en charge : ouvrez-le dans Word et enregistrez un `.docx`.

!!! warning "Les fichiers d'une version plus récente ne seront pas importés"
    Un projet ou un examen exporté enregistré par une version ultérieure de l'application à celle
    celui que vous exécutez est refusé, avec le même message l'ouvrirait
    donner : *"La version du fichier est supérieure à la version de l'application"*. Demander
    celui qui l'a envoyé pour le sauvegarder à partir d'une version correspondante.

## Démarrer une importation {#start-an-import}

1. Choisissez **Fichier → Importer des examens à partir d'un autre projet** pour importer des examens entiers.
   dans le projet ouvert.
2. Cliquez avec le bouton droit sur un examen dans **Exam Explorer** et choisissez **Import Papers From
   Fichier** pour ajouter des épreuves à cet examen.
3. Cliquez avec le bouton droit sur un document et choisissez **Importer des questions à partir d'un fichier** pour l'ajouter.
   questions à ce document.

L'étape 1 demande le fichier. Les documents passent ensuite à l'étape 2 ; autre chose à l'étape 3.

![Étape 1 de l'assistant d'import, avec le sélecteur de fichiers et les types de fichiers acceptés](../../assets/images/designer/import-choose-file.png)

## Dites à Designer où commence chaque question {#tell-designer-where-each-question-starts}

L'étape 2 apparaît uniquement pour les documents. Choisissez le marqueur qui commence chaque question
dans votre fichier : `1.`, `Q1.`, `Q1` sur une ligne qui lui est propre, ou `Q.`. Rien n'est
présélectionné, alors choisissez celui qui correspond à votre document. Ouvrir **Que peut-on faire d'autre
J'ai mis dans mon document ?** pour une référence aux balises, chacune en début de ligne.

![Étape 2 avec les options du marqueur de question et le panneau de balises open](../../assets/images/designer/import-question-markers.png)

### Balises {#tags}

**Question :**

: Le texte de la question, nécessaire uniquement lorsqu'il ne suit pas le marqueur.

**Instruction :**

: L'instruction pour cette question.

**Section :**

: Place la question dans une section nommée.

**Étude de cas :**, **Passage :**, **Compréhension :**, **Exemple :**

: Un passage attaché à la question. La balise que vous choisissez est celle affichée.

**A.**, **A)**, **A :**

: Une option. Les lettres A à J sont reconnues.

**Réponse :**, **Réponse :**, **Option correcte :**

: La lettre de l'option correcte.

**Réf :**, **Exp :**, **Explication :**, **Référence :**

: L'explication affichée avec la réponse.

### Les cas qui surprennent les gens {#the-cases-that-catch-people-out}

Une question n'est terminée qu'une fois qu'une ligne de réponse a été vue. C'est ce que
permet à une liste numérotée à l'intérieur d'une étude de cas, `1. First point` et `2. Second
point`, de rester dans le passage au lieu que chaque ligne commence par une question sur son
propre. Une question sans réponse ne se ferme jamais et avale celles qui suivent
donc une question importée contenant le texte de plusieurs signifie généralement un
ligne **Réponse:** manquante. Une deuxième réponse remplace la première ; cela n’en ajoute pas.

Une ligne ne portant aucune balise continue la ligne qui la précède, c'est ainsi qu'une ligne multiligne
l'étude de cas reste en un seul morceau, et pourquoi une note parasite entre les questions est
ajouté à la ligne ci-dessus. Le texte non balisé avant qu'une balise ne devienne la question
texte, et une balise **Question:** ultérieure le remplace. Un nom **Section :** sous
trois caractères sont ignorés et la question atterrit dans la valeur par défaut du journal
rubrique. L'importation de documents produit toujours des éléments à choix multiples et à sélection unique,
alors remplissez le vide et la sélection multiple doit toujours être [rédigé par
main](questions.md).

## Choisissez quoi importer {#choose-what-to-import}

L'étape 3 montre ce que Designer a trouvé sous la forme d'un arbre Examen → Papier → Question.

1. Cochez les examens, épreuves ou questions que vous souhaitez.
2. Sélectionnez chacun d'eux pour le lire dans le volet d'aperçu à droite.
3. Choisissez **Importer**.

Seuls les niveaux autorisés par votre point d'entrée sont cochables : l'importation de papiers vous permet
cochez les épreuves et les questions mais pas les examens ; importer des questions, uniquement des questions.

![Étape 3 avec l'arborescence de contenu cochée à gauche et une question prévisualisée à droite](../../assets/images/designer/import-select-content.png)

Les images à l'intérieur d'un `.docx` sont importées avec leurs questions ; toute image trop grande
ou dans un format que Designer ne peut pas afficher est ignoré, compté et signalé lorsque
l'importation se termine. Ce qui arrive est du contenu Designer ordinaire, alors prévisualisez-le,
définissez les partitions et les sections et enregistrez le projet.

## Télécharger les questions {#download-questions}

**Télécharger les questions** est une fonctionnalité distincte qui ne fait pas partie de l'assistant d'importation.
Cliquez avec le bouton droit sur un article et choisissez-le pour extraire les questions des SmartQuestions.

1. Connectez-vous avec votre compte Ratelsoft.
2. Choisissez un programme, puis jusqu'à cinq matières.
3. Définissez le nombre de questions à répondre sur chaque sujet, entre 1 et 100.
4. Choisissez un ordre séquentiel ou aléatoire, puis téléchargez.

La connexion n’est pas stockée. Designer le demande à nouveau dans une nouvelle session.

![La boîte de dialogue Questions de téléchargement demandant une connexion au compte Ratelsoft](../../assets/images/designer/import-download-questions.png)

Pour copier du contenu dans le projet ouvert, voir [Réutiliser le projet
contenu](importing-questions.md).
