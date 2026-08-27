---
title: Ajouter et importer des candidats dans examina.io
description: Créez des dossiers de candidats individuellement ou importez des candidats
  à partir d'Excel, CSV ou de fichiers texte dans examina.io Manager.
tags:
- importation de candidats
- importation CSV
- candidats
- importation Excel
- directeur
translation_source: user-guides/manager/examinees.md
translation_source_sha256: 173ab50c30199eb9a9667889688609598592bbab3972eab3326f03082ffd9b90
---

# Ajouter et importer des candidats {#add-and-import-examinees}

Un **examiné** est un candidat qui passe un examen via le client.
demande. Les candidats sont distincts du personnel **Utilisateurs**.

![L'onglet Candidats](../../assets/images/manager/examinees-tab.png)

## Ajouter un candidat {#add-one-examinee}

1. Ouvrez **Manager**.
2. Sélectionnez **Fichier → Ajouter un nouveau candidat**.
3. Saisissez le nom et le sexe du candidat.
4. Saisissez un code de candidat unique ou choisissez l'attribution automatique du code.
5. Entrez un code d'accès ou choisissez la génération de code d'accès.
6. Ajoutez des détails facultatifs tels que l'adresse e-mail, le numéro de téléphone, la date de naissance,
   titre ou photographie.
7. Enregistrez l'enregistrement.

Le code identifie le candidat lors de la connexion et doit être unique. Un carré
une photo d'environ 256 × 256 pixels fonctionne mieux lorsque votre flux de travail utilise le candidat
images ou vérification d’identité.

![Un dossier de candidat enregistré](../../assets/images/manager/examinee-details.png)

## Préparer un fichier d'importation {#prepare-an-import-file}

Manager prend en charge :

- Classeurs Excel : `.xls` et `.xlsx`
- texte délimité : `.csv` et `.txt`

Placez un candidat sur chaque rangée. Les champs obligatoires sont :

- prénom ;
- nom de famille; et
- le sexe.

Des codes et des mots de passe peuvent être générés lorsqu'ils sont omis. Si vous incluez
numéros de téléphone, utilisez le format international tel que `+14165550100`. Si vous incluez
dates de naissance, utilisez le format indiqué par l'importateur, tel que `8/7/1900`.

Pour une importation fiable, utilisez une ligne d'en-tête avec des noms de colonnes clairs et enregistrez une copie
du fichier source d'origine.

Exemple CSV :

```csv
student_id,first_name,last_name,gender,email
STU-1001,Avery,Okafor,F,avery@example.edu
STU-1002,Noah,Martin,M,noah@example.edu
```

## Importer un fichier {#import-a-file}

1. Sélectionnez **Fichier → Importer les candidats à partir d'un fichier/Excel**.
2. Choisissez le fichier.
3. Pour un fichier texte, choisissez ou détectez automatiquement le séparateur, tel que virgule, tabulation,
   barre verticale, point-virgule ou deux-points.
4. Vérifiez l'aperçu des données.
5. Choisissez si la deuxième ligne d'aperçu doit être affichée et si la première
   row est un en-tête à ignorer.
6. Mappez chaque colonne source au champ du candidat approprié.
7. Choisissez éventuellement un groupe pour les enregistrements importés.
8. Choisissez si le processus doit s'arrêter à la première erreur.
9. Démarrez l'importation et examinez chaque ligne ajoutée, ignorée ou ayant échoué.

Si **Mettre à jour les candidats existants si le code/ID du candidat correspond** est disponible et
sélectionnés, les codes correspondants peuvent mettre à jour les enregistrements existants. Utilisez cette option uniquement lorsque
le fichier source est fiable et le mappage du code a été vérifié.

## Valider le résultat {#validate-the-result}

Après l'importation :

- comparer le nombre ajouté avec le fichier source ;
- rechercher plusieurs codes de candidats ;
- vérifier les noms, les adresses e-mail et les mappages de genre ;
- vérifiez tous les codes ou mots de passe générés automatiquement ;
- confirmer l'adhésion facultative au groupe ; et
- exporter ou enregistrer le journal d'importation selon votre mode opératoire.

Les lignes manquant des champs obligatoires sont ignorées ou entraînent une résiliation selon les
paramètre d’erreur choisi.

## Protéger les données des candidats {#protect-examinee-data}

- Importez uniquement les données nécessaires à l'administration de l'évaluation.
- Ne placez pas de codes d'accès dans une feuille de calcul largement partagée.
- Utilisez un canal sécurisé approuvé pour distribuer les informations d'identification.
- Supprimez les enregistrements de test obsolètes et les copies locales conformément à votre politique de conservation.
- Confirmez que votre organisation dispose d'une base légale pour toute photo, biométrie ou
  surveiller les données qu’il collecte.

## Étape suivante {#next-step}

Créez des groupes ou attribuez directement des candidats en suivant [Groupes et examens
affectations](groups-and-assignments.md).
