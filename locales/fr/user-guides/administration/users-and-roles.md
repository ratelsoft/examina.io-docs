---
title: Gérer les utilisateurs et les rôles de compte
description: Ajoutez des membres du personnel, attribuez les rôles examina.io, réinitialisez l'accès et appliquez le principe du moindre privilège.
tags:
- rôles de compte
- administrateurs
- surveillants
- gestion des utilisateurs
translation_source: user-guides/administration/users-and-roles.md
translation_source_sha256: 0de577eb6227a78de5c3212ee769ac9f5df03d7870c962fa0fd9a33b2883d719
---

# Gérer les utilisateurs et les rôles de compte {#manage-users-and-account-roles}

Les utilisateurs sont des comptes de personnel permettant de rédiger, d'administrer ou de surveiller des examens.
Ce ne sont pas des dossiers de candidats.

Les comptes racine et administrateur peuvent ouvrir **Accueil → Utilisateurs**. Le tableau des utilisateurs
affiche le nom, l'adresse e-mail et le type de compte de chaque membre du personnel visible.

![La table Utilisateurs avec un compte coordinateur d'examen régulier](../../assets/images/administration/users-and-roles.png)

## Choisissez un rôle de compte {#choose-an-account-role}

| Rôle | Attribuer à |
| --- | --- |
| **Racine** | Un propriétaire principal d'organisation qui a besoin de facturation et d'administration complète de l'organisation |
| **Administrateur** | Un administrateur de confiance qui gère les utilisateurs, les cercles et les paramètres |
| **Régulier** | Un auteur de questions, un coordinateur d'examen ou un autre membre du personnel ayant besoin de Designer ou Manager |
| **Surveillant** | Une personne qui supervise uniquement les examens éligibles surveillés en direct |

Utilisez le rôle le plus bas qui soutient le travail de la personne. Voir [Rôles utilisateur et
permissions](../../getting-started/roles-and-permissions.md) pour les informations détaillées
modèle d’accès.

## Ajouter un utilisateur {#add-a-user}

1. Ouvrez **Accueil → Utilisateurs**.
2. Sélectionnez **Ajouter un nouvel utilisateur**.
3. Saisissez le nom et l'adresse e-mail professionnelle de la personne.
4. Choisissez le type de compte.
5. Soumettez le formulaire.
6. Confirmez que la personne effectue la vérification de compte requise ou
   processus de configuration du mot de passe.
7. Ajoutez l'utilisateur aux cercles appropriés.

Utilisez un compte professionnel individuel pour chaque personne. Administrateur partagé ou
les qualifications des surveillants affaiblissent la responsabilisation et rendent le départ difficile.

## Réinitialiser ou supprimer l'accès {#reset-or-remove-access}

Les boutons d'action du tableau Utilisateurs permettent à un administrateur de réinitialiser le nom d'un utilisateur.
mot de passe ou supprimer l'utilisateur.

Avant une réinitialisation du mot de passe, vérifiez l'identité du demandeur via un
canal. Avant de supprimer un utilisateur :

1. confirmer le compte exact ;
2. examiner tout transfert opérationnel ;
3. supprimer ou réaffecter les responsabilités du Cercle ;
4. conserver les informations d'audit requises ; et
5. informer le propriétaire du compte conformément à la politique.

La suppression d’un utilisateur du personnel est différente de la suppression d’un candidat.

## Examinez régulièrement l’accès {#review-access-regularly}

Au moins avant chaque évaluation à enjeux élevés :

- supprimer les comptes des personnes qui n'ont plus besoin d'y accéder ;
- réduire les comptes Administrateurs qui n'administrent plus la plateforme ;
- confirmer que les surveillants sont affectés uniquement aux examens requis par l'intermédiaire des cercles ;
- vérifier que les utilisateurs réguliers ne peuvent pas voir les examens ou les candidats sans rapport ; et
- protégez les comptes Root avec des informations d'identification fortes et uniques.

## Résoudre les problèmes d'accès manquant {#troubleshoot-missing-access}

Si un membre du personnel peut se connecter mais ne peut pas voir un examen ou un candidat :

1. confirmer que le rôle du compte prend en charge l'application requise ;
2. confirmer que l'Utilisateur appartient au Cercle concerné ;
3. confirmer que l'examen et les candidats font partie du même cercle ; et
4. Déconnectez-vous et reconnectez-vous après les modifications d'autorisation si nécessaire.

Continuez avec [Cercles et autorisations](circles-and-permissions.md).
