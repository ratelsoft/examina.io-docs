---
title: Groupes et devoirs d'examen dans examina.io
description: Organisez les candidats en groupes et mappez les personnes, les groupes,
  les examens, les épreuves, les heures de début et les fuseaux horaires dans examina.io
  Manager.
tags:
- devoir d'examen
- cartographie des examens
- groupes de candidats
- directeur
- cartographie papier
translation_source: user-guides/manager/groups-and-assignments.md
translation_source_sha256: 4c6bbfaf4fda4dda6ae0d94a03fd399b97cb5b7665f17fbe98f789618efe5c4d
---

# Groupes et devoirs d'examen {#groups-and-exam-assignments}

Manager utilise **Groupes** pour les collections réutilisables de candidats et les **mappings**
décider quelles épreuves d'examen chaque candidat peut passer.

## Quand utiliser un groupe {#when-to-use-a-group}

Créez un groupe pour un ensemble de personnes que vous manipulez régulièrement ensemble, telles que :

- un cours ou une classe ;
- une promotion ou une cohorte ;
- un centre d'évaluation ;
- un département ; ou
- une séance programmée.

Un groupe n'accorde pas d'autorisations au personnel. Utilisez un [Circle](../administration/circles-and-permissions.md)
pour le contrôle d'accès.

## Créer un groupe {#create-a-group}

1. Ouvrez **Manager**.
2. Sélectionnez **Fichier → Créer un nouveau groupe**.
3. Entrez un nom unique et une description utile.
4. Enregistrez le groupe.
5. Sélectionnez le groupe, puis ajoutez des candidats dans la liste consultable.

![Un Groupe et ses membres](../../assets/images/manager/group-details.png)

Les boutons à côté de la liste des membres couvrent toutes les manières de remplir un groupe : ajouter
candidats un à la fois, ajoutez-en plusieurs à la fois, ajoutez les candidats correspondant à un
fichier téléchargé ou copiez l'appartenance à un autre groupe.

Vous pouvez également ajouter une appartenance à un groupe à partir d'un dossier de candidat ou attribuer un
candidats à un groupe lors de l’importation du fichier.

## Associer un candidat à un examen {#map-one-examinee-to-an-exam}

1. Ouvrez l'onglet **Candidats** et sélectionnez la personne.
2. Choisissez l'action pour mapper le candidat à un examen.
3. Recherchez et sélectionnez un examen.
4. Continuez avec la cartographie papier.
5. Sélectionnez les épreuves que le candidat peut passer.
6. Vous pouvez éventuellement attribuer l'heure d'examen la plus précoce et choisir le fuseau horaire correct.
7. Enregistrez le mappage.

Un seul examen est sélectionné en une seule opération de mappage, mais vous pouvez mapper les
même candidat à des examens supplémentaires lors d'opérations ultérieures.

## Cartographier plusieurs candidats d'un examen {#map-several-examinees-from-an-exam}

1. Ouvrez l'onglet **Examens** et sélectionnez l'examen.
2. Choisissez **Map des candidats**.
3. Recherchez les candidats par nom, code ou un champ supplémentaire disponible.
4. Déplacez les candidats prévus vers la liste sélectionnée.
5. Continuez avec la cartographie papier.
6. Choisissez les papiers et l'heure de début facultative.
7. Enregistrez les mappages.

## Cartographier un groupe {#map-a-group}

Vous pouvez commencer soit par l'examen, soit par le groupe :

- Sélectionnez un examen et choisissez **Map Groups** ; ou
- sélectionnez un groupe et choisissez **Mapper le groupe à l'examen**.

Lors du mappage d'un groupe, Manager applique l'affectation aux membres actuels du groupe
qui ne sont pas déjà affectés à cet examen. Ajouter quelqu'un au groupe plus tard
n'implique pas que chaque opération de mappage passée soit automatiquement répétée, donc
examiner les candidats cartographiés de l'examen après les changements d'adhésion.

## Choisissez soigneusement les papiers et le temps {#choose-papers-and-time-carefully}

Les épreuves sélectionnées sont les épreuves que le candidat peut passer chez le client. Si un examen
contient plusieurs épreuves, confirmez que chaque candidat a le bon
combinaison.

L'heure de début cartographiée facultative correspond à l'heure la plus rapprochée pour laquelle l'examen est disponible.
cette mission. Vérifiez toujours :

- date du calendrier ;
- l'heure locale ;
- le fuseau horaire ;
- implications pour l'heure d'été ; et
- si les candidats de différentes régions ont besoin d'affectations distinctes.

## Vérifier les mappages {#verify-mappings}

Avant de publier un examen :

![La liste des candidats mappés pour un examen](../../assets/images/manager/exam-details.png)

1. Ouvrez la liste des candidats mappés de l'examen.
2. Comparez son décompte avec la liste prévue.
3. Vérifiez les devoirs sur papier.
4. Vérifiez les heures de début et les fuseaux horaires.
5. Confirmez qu'aucun candidat retiré ou en double n'est présent.
6. Testez avec un compte de candidat qui a le même modèle de papier.

La suppression d'un mappage supprime l'affectation ; il ne supprime pas le sous-jacent
candidat ou groupe.

## Étape suivante {#next-step}

Continuez avec [Livrer, surveiller et signaler](deliver-monitor-report.md).
