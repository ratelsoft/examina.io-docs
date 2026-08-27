---
title: Envoyez un e-mail à vos candidats
description: Envoyez des invitations et des résultats depuis Manager avec des champs personnalisés et des liens de connexion propres à chaque candidat.
tags:
- invitation à l'examen
- email du candidat
- lien magique
- directeur
- espaces réservés
translation_source: user-guides/manager/email-examinees.md
translation_source_sha256: 5fc7cb4dd93fe7848375d20f62bf4c1a125a37385e6efd89d174ef4a5460b211
---

# Envoyez un e-mail à vos candidats {#email-your-examinees}

Manager peut envoyer un e-mail aux personnes affectées à un examen : une invitation avant le
assis, ou leur résultat après. Vous écrivez le message une fois, et Manager
le personnalise pour chaque destinataire avant l'envoi.

Sélectionnez l'examen, puis utilisez **Envoyer un e-mail aux candidats** à partir du candidat mappé.
panneau. Seuls les candidats ayant une adresse e-mail dans leur dossier reçoivent quoi que ce soit.

## Espaces réservés de personnalisation {#personalisation-placeholders}

Écrivez `#[CODE]` dans votre message et chaque candidat recevra son propre code dans son
lieu. Les espaces réservés fonctionnent dans la ligne d'objet ainsi que dans le corps.

### Le candidat {#the-examinee}

| Espace réservé | Devient |
|---|---|
| `#[FNAME]` | Prénom |
| `#[MNAME]` | Deuxième prénom, ou rien |
| `#[LNAME]` | Nom de famille |
| `#[FLNAME]` | Nom complet |
| `#[TITLE]` | *M.* ou *Mme*, selon le sexe indiqué dans le dossier |
| `#[GEN]` | Genre sous forme de texte |
| `#[CODE]` | Code ou pièce d'identité du candidat |
| `#[PASS]` | Code d'accès |
| `#[EMAIL]` | Adresse e-mail |
| `#[PHONE]` | Numéro de téléphone, ou rien |
| `#[DOB]` | Date de naissance |
| `#[PIC]` | La photographie du candidat, comme image |

### L'examen {#the-exam}

| Espace réservé | Devient |
|---|---|
| `#[EXAM]` | Titre de l'examen |
| `#[ECODE]` | Code d'examen |
| `#[LINK]` | Le lien de l'examen, sous forme de lien cliquable |
| `#[MAGICLINK]` | Un lien de connexion pour ce candidat – voir ci-dessous |
| `#[TIME]` | L'heure de début cartographiée du candidat, ou rien lorsqu'aucune heure n'a été définie |
| `#[PAPERS]` | Les papiers auxquels ce candidat est mappé |

### Le résultat {#the-result}

| Espace réservé | Devient |
|---|---|
| `#[SCORE]` | Score obtenu |
| `#[MAX]` | Score pouvant être obtenu |
| `#[PERCENT]` | Score en pourcentage |
| `#[RESULT]` | Un résumé des résultats formaté |

!!! warning "Les espaces réservés aux résultats n'appartiennent qu'à un e-mail de résultats"
    Ceux-ci sont lus à partir d’une tentative terminée. Dans une invitation, envoyée avant tout le monde
    a passé l'examen, il n'y a pas de note à remplacer et ils rendent comme
    rien - laisser une phrase avec un trou. Gardez-les hors de
    invitations.

## Liens de connexion {#sign-in-links}

`#[MAGICLINK]` insère un lien qui signe le candidat directement dans son examen.
Ils ne saisissent pas de code ou de mot de passe ; le lien porte leur identité.

Cela vaut la peine d'être utilisé lorsque la distribution du mot de passe est la partie délicate de votre
processus – candidats plus jeunes, grandes cohortes ou toute personne susceptible de mal saisir un code
le matin de l'examen.

```text
Hello #[FNAME],

Your exam, #[EXAM], starts at #[TIME].

Open it here: #[MAGICLINK]

If the link does not work, sign in at #[LINK] with
code #[CODE] and passcode #[PASS].
```

### Ce qu'il faut savoir avant de l'utiliser {#what-to-know-before-you-use-it}

**Envoyez également le code et le mot de passe.** L'e-mail est la partie la moins fiable de l'examen
jour — filtres, retards, un candidat lisant un courrier sur un téléphone, il ne restera pas assis
examen. Traitez le lien comme le chemin pratique et les informations d'identification comme le
repli, exactement comme le fait l’exemple ci-dessus.

**Le lien est personnel et il s'agit d'un identifiant.** Toute personne qui le détient peut y accéder.
examen en tant que candidat. Dites aux candidats de ne pas le transmettre. Ce n'est plus
partageable qu’un mot de passe, mais il est plus facile de le transmettre par accident.

**Un candidat ne peut pas s'asseoir deux fois à la fois.** Si le lien est ouvert pendant ce temps
Le candidat a déjà l'examen ouvert ailleurs, la deuxième tentative est refusée. Un
le candidat dont le navigateur est tombé en panne peut rouvrir le même lien et continuer.

**Le lien cesse de fonctionner une fois l'examen terminé.** Il expire trois jours après son examen.
envoyé, ou peu de temps après la fin de la séance lorsque le candidat a été mappé avec un début
le temps. Il cesse également de fonctionner une fois soumis, si vous passez l'examen.
invisibles, ou si vous supprimez leur mappage.

**Le renvoi est sécurisé.** Un e-mail de rappel réutilise le lien déjà présent dans le
la boîte de réception du candidat plutôt que de la remplacer, afin que le premier e-mail continue de fonctionner.

### Quand un lien ne fonctionne pas {#when-a-link-does-not-work}

Le candidat arrive sur la page de connexion pour cet examen avec un message expliquant
pourquoi, et peuvent se connecter avec leur code et leur mot de passe à la place. Un lien expiré dit
si clairement, séparément d'un lien qui n'a jamais été valable pour cet examen, donc un
le candidat n'est pas informé que ses informations d'identification sont erronées lorsque son lien a simplement été exécuté
dehors.

La seule exception est un examen qui a été supprimé. Il n'y a plus d'examen à faire
afficher une page de connexion pour que le lien mène à une page introuvable.

## Avant d'envoyer {#before-you-send}

1. Envoyez-vous d'abord un test, en utilisant un candidat associé à l'examen.
2. Vérifiez chaque espace réservé résolu : un espace réservé mal orthographié est envoyé comme
   texte littéral.
3. Confirmez que les destinataires correspondent à la liste que vous attendez, sur la liste mappée de l'examen.
4. Vérifiez l'heure de début et le fuseau horaire dans le message par rapport au mappage.

## Étape suivante {#next-step}

Continuez avec [Livrer, surveiller et signaler](deliver-monitor-report.md).
