---
title: Créez des questions d'examen basées sur la source avec l'IA
description: Auteur cité, questions d'examen modifiables de PDF, DOCX, PPTX, TXT,
  Markdown, HTML et passages existants avec examina.io Designer.
tags:
- création de questions d'IA basées sur la source
- rédaction d'évaluations
- questions d'examen
- Designer
- questions citées
translation_source: user-guides/designer/ai-question-authoring.md
translation_source_sha256: f2eee7ab06512f6877e0dc625ad4ff119520e39668d030b899bc4d144b41b991
---

# Créez et révisez des questions avec l'IA {#create-and-review-questions-with-ai}

Designer peut transformer le matériel source en brouillons de questions modifiables sans quitter
le papier actuel. Il n'insère ni ne publie jamais automatiquement la sortie de l'IA : un
l'auteur autorisé examine chaque candidat et choisit ce qui entre dans l'article.

## Ce que comprend votre forfait et combien coûtent les questions supplémentaires {#what-your-plan-includes-and-what-extra-questions-cost}

La création de questions d'IA basées sur la source est incluse dans chaque plan. Votre mensualité
l'allocation compte les candidats valides, étayés par la source et sans double emploi qui atteignent
**Révision** : pas de demandes, de pages téléchargées ou de nouvelles tentatives du fournisseur.

| Planifier | Questions basées sur la source par mois | Stockage de la bibliothèque source | Sources enregistrées | Taille maximale du fichier |
| --- | --- : | --- : | --- : | --- : |
| Démarreur | 10 | 250 Mo | 25 | 50 Mo |
| De base | 100 | 2 Go | 250 | 250 Mo |
| Professionnel | 500 | 10 Go | 1 000 | 500 Mo |
| Flexible | 100 | 5 Go | 500 | 500 Mo |
| Entreprise | Personnalisé | Personnalisé | Personnalisé | Personnalisé |

L'allocation incluse est réinitialisée au début de chaque mois civil UTC et est
partagé par l’organisation. L'allocation actuelle est indiquée dans la création AI
fenêtre. Une question textuelle ou une question qui réutilise une image de la source
utilise une question incluse. Une question avec un visuel nouvellement généré utilise quatre
questions incluses. Par exemple, une allocation de 100 peut produire jusqu'à 100
des questions de texte ou d'image source, jusqu'à 25 questions visuelles nouvellement générées, ou un
mélange des deux.

Une fois l'allocation incluse utilisée, le prix actuel de chaque supplément
La question valide qui parvient à l'examen est :

| Résultat atteignant l'examen | USD | CAO | NGN |
| --- | --- : | --- : | --- : |
| Question texte uniquement ou image source | 0,15 $ | 0,20 $CAN | 200 ₦ |
| Question avec un visuel nouvellement généré | 0,60 $ | 0,80 $CAN | 800 ₦ |

Il n’existe pas de produit de crédit IA ou de portefeuille IA distinct. Le prix est réservé et
déduit du solde prépayé normal de votre organisation. Chaque plan peut ajouter
fonds de **Facturation → Solde prépayé** en utilisant le fournisseur de paiement disponible.
La fenêtre AI affiche le prix applicable et le solde prépayé disponible avant
vous générez. Si le solde ne peut couvrir la partie de la demande au-delà de votre
allocation, la génération ne démarre pas et vous indique combien ajouter.

Par exemple, s'il reste deux questions incluses et que vous en demandez cinq, Designer
se réserve le prix de trois questions. Si quatre candidats valides parviennent à l'examen,
les deux questions incluses comptent en premier, seules deux questions prépayées sont facturées,
et la réservation d'une question non utilisée est reversée sur le solde prépayé.

!!! info "Seuls les candidats valides et étayés par la source atteignent le nombre d'avis"
    Demandes échouées, candidats invalides, candidats sans source vérifiable
    les preuves et les duplicata rejetés avant l'examen n'utilisent pas l'allocation ou
    solde prépayé.

## Sources prises en charge {#supported-sources}

Vous pouvez générer à partir du passage ou de l'étude de cas en cours, sélectionner jusqu'à 10 enregistrements enregistrés
ressources de l'organisation, ou téléchargez l'un de ces types de fichiers :

- PDF (`.pdf`)
-Microsoft Word (`.docx`)
-Microsoft PowerPoint (`.pptx`)
- texte UTF-8 brut (`.txt`)
- Markdown (`.md` ou `.markdown`)
- HTML (`.html` ou `.htm`)
- Images PNG, JPEG, GIF ou WebP

Les sources PDF doivent contenir du texte sélectionnable. Exécutez l'OCR avant de télécharger un document numérisé
ou image uniquement PDF. Les fichiers Office prenant en charge les macros et chiffrés ne sont pas pris en charge.
Designer lit HTML comme un texte inerte : il n'exécute pas de scripts, ne soumet pas de formulaires, ne charge pas
objets intégrés ou récupérer des ressources distantes.

Les ressources téléchargées restent dans la bibliothèque source privée de votre organisation jusqu'à ce qu'une
l'utilisateur les supprime. Le téléchargement à nouveau du même fichier réutilise la ressource existante
au lieu de stocker une autre copie.

## Générer des questions candidates {#generate-question-candidates}

1. Ouvrez un projet d'examen et sélectionnez l'épreuve qui doit recevoir les questions.
2. Choisissez **Rédiger des questions à partir de vos sources** dans la barre d'outils Exam Explorer.
3. Sur **Source**, choisissez le passage actuel, sélectionnez les ressources enregistrées ou téléchargez
   un fichier pris en charge. Attendez que chaque ressource sélectionnée soit prête.
4. Dans **Questions**, ajoutez une ou plusieurs lignes de plan.
5. Pour chaque ligne, choisissez un nombre exact, un type de question, une difficulté, des notes et
   sujet facultatif ou résultat d’apprentissage.
6. Choisissez **Générer des candidats**.

Designer prend en charge ces types de questions générées :

- Choix multiple - sélection unique
- Choix multiple - sélection multiple
- Remplissez le blanc

Les grandes sources utilisent une sélection ciblée de sections de sources originales plutôt que
un résumé de l'IA. Pour que les demandes à l'échelle du livre restent économiques, Designer nécessite au
au moins trois questions posées lorsque les sources sélectionnées contiennent entre 100 000 et 499 999
jetons estimés, et au moins cinq à 500 000 jetons ou plus. Sources plus courtes
peut générer une question.

## Vérifier avant d'insérer {#review-before-inserting}

Dans **Réviser**, vérifiez et modifiez les éléments suivants :

- le texte des questions ;
- choix de réponses ou réponses à compléter acceptées ;
- sélection de la bonne réponse ;
- explication;
- difficulté et notes ; et
- citation de la source.

Décochez **Accepter** ou choisissez **Rejeter** pour tout candidat que vous ne souhaitez pas. Choisissez
**Insérer la sélection** uniquement une fois que les questions restantes sont prêtes pour la normale
Édition et aperçu Designer.

!!! important
    Les résultats de l’IA peuvent être incomplets, ambigus ou incorrects, même lorsqu’ils citent un
    source. Un expert en la matière doit vérifier le libellé, le corrigé,
    explication, difficulté, accessibilité et note avant la livraison.

## Preuves et contrôles en double {#evidence-and-duplicate-checks}

Les candidats doivent citer le texte trouvé sur la page PDF indiquée, section Word,
Diapositive PowerPoint, plage de lignes de texte, en-tête Markdown ou en-tête HTML avant
peut accéder à Review.

La détection des doublons compare les candidats avec :

- d'autres candidats de la génération actuelle ; et
- des questions déjà dans le document actuellement ouvert.

Designer ne compare délibérément pas les questions d'autres épreuves, examens ou
contenu de l’organisation.

## Si la génération ne se termine pas {#if-generation-does-not-complete}

- Confirmez que le fichier est d'un type pris en charge et contient suffisamment de texte lisible.
- Pour le texte, Markdown et HTML, enregistrez le fichier au format UTF-8.
- Pour PDF, exécutez OCR si vous ne pouvez pas sélectionner et copier son texte.
- Confirmez que le nombre de questions demandées correspond au minimum requis pour les grandes sources.
- Sélectionnez moins ou plus de sources ciblées et réessayez.
- Vérifiez l'allocation incluse restante de l'organisation et le solde prépayé.
- Si l'allocation est épuisée, ouvrez **Facturation → Solde prépayé** et ajoutez à
  au moins le manque à gagner affiché dans la fenêtre de création de l'IA.

Après l'insertion, utilisez l'aperçu et la qualité normaux de la question
check](questions.md#preview-and-quality-check) avant d'enregistrer et d'exporter le
projet.

## Créer des questions qui utilisent des visuels {#create-questions-that-use-visuals}

Lorsqu'une source sélectionnée contient une image prise en charge, chaque ligne de plan propose
ces choix visuels :

| Choix | Que fait le Designer | Utilisation des questions incluses |
| --- | --- | --- : |
| Aucun visuel | Génère une question textuelle uniquement. | 1 |
| Réutiliser l'image source | Utilise une image pertinente extraite de l’emplacement source cité. | 1 |
| Générer un nouveau visuel | Crée un visuel 1K distinct qui teste un concept similaire. | 4 |
| Automobile | Choisit le texte, la réutilisation de la source ou un nouveau visuel en fonction de la source et renvoie les questions réservées inutilisées après règlement. | 1 ou 4 |

Une question visuelle doit citer un texte source lisible de la même page PDF,
Diapositive PowerPoint, section de document ou autre emplacement source comme référence
image. Designer évite les pochettes, les logos, les images décoratives et autres
première question. Les visuels nouvellement générés conservent leur source, leur modèle et leur tâche
lignée et restent en attente d’un examen humain.

Avant d'insérer un visuel candidat, vérifiez que l'image est pertinente,
ne révèle pas la réponse, et dispose d'un texte alternatif précis et d'un long texte utile
descriptif. Une image échouée ou rejetée n'utilise pas les droits de l'organisation.
allocation ou solde prépayé.
