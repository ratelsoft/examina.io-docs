---
title: Configurer les cercles et les autorisations d'examen
description: Créez des cercles examina.io qui connectent les utilisateurs, les examens
  et les candidats pour imposer un accès limité au personnel.
tags:
- contrôle d'accès
- cercles
- autorisations d'examen
- autorisations utilisateur
translation_source: user-guides/administration/circles-and-permissions.md
translation_source_sha256: b9c946628f9fcca401d26f0faab24b32e0a5ed14d358638d8aa3202c40724276
---

# Configurer les cercles et les autorisations {#configure-circles-and-permissions}

Un cercle est une limite d'autorisation composée d'**utilisateurs**, d'**examens** et
**Candidats**. Un utilisateur peut travailler avec les ressources mises à disposition via le
Circle, sous réserve du rôle de compte de l'Utilisateur.

![Un Cercle résume ses candidats, ses utilisateurs et ses examens](../../assets/images/administration/circles-permissions.png)

## Planifier le cercle {#plan-the-circle}

Utilisez un Cercle pour un domaine de responsabilité stable, tel que :

- un cours ou un département ;
- un programme d'examens ;
- un client ou un locataire ;
- un emplacement scolaire ; ou
- un projet d'évaluation restreint.

Choisissez un nom clair et une balise courte, par exemple **Biologie 201** et
**BIO-201**. Évitez de mettre des informations confidentielles sur les candidats dans le Cercle
nom.

## Créer un cercle {#create-a-circle}

1. Ouvrez **Accueil → Cercles**.
2. Sélectionnez **Ajouter un nouveau cercle**.
3. Entrez un nom unique et une balise facultative.
4. Sélectionnez les utilisateurs qui ont besoin d'un accès.
5. Sélectionnez les examens qu'ils administreront ou surveilleront.
6. Sélectionnez les candidats qu'ils doivent afficher ou gérer.
7. Enregistrez le cercle.

Les comptes racine et administrateur peuvent créer et modifier des cercles. Autre autorisé
Les utilisateurs peuvent voir les cercles qui les concernent.

## Vérifier la limite {#verify-the-boundary}

Le tableau Cercles affiche le nombre de candidats, d'utilisateurs et d'examens dans chaque cercle.
Après avoir enregistré :

1. comparez chaque décompte avec votre adhésion prévue ;
2. modifiez les noms du cercle et vérifiez de manière ponctuelle dans les trois listes ;
3. testez avec un compte régulier ou surveillant ;
4. vérifier qu'un examen et un candidat sans rapport ne sont pas visibles ; et
5. Vérifiez que les espaces de travail Proctor requis apparaissent pour les surveillants.

## Cercles comparés aux groupes {#circles-compared-with-groups}

| Cercle | Groupe |
| --- | --- |
| Contrôle l'accès du personnel | Organise les candidats pour les opérations groupées |
| Contient des utilisateurs, des examens et des candidats | Contient des candidats |
| Utilisé dans les contrôles d'autorisation Accueil, Manager et Proctor | Utilisé dans Manager pour le travail d'affectation |

Il est courant d'utiliser les deux. Un cercle de cours peut restreindre l'équipe de cours, tandis qu'un
Le groupe peut contenir les étudiants mappés à une séance particulière.

## Maintenir les cercles en toute sécurité {#maintain-circles-safely}

- Mettre à jour l'adhésion lorsque les responsabilités du personnel changent.
- Supprimez les examens terminés et l'accès des candidats périmés conformément à la politique.
- Gardez les ressources réservées aux administrateurs hors des grands cercles.
- Vérifiez l'adhésion au Cercle avant d'activer la surveillance en direct.
- Testez les modifications d'autorisation avec un compte non-administrateur.

La suppression d'un cercle supprime le groupe d'autorisations. Confirmer l’impact sur le personnel
accès avant de le supprimer.
