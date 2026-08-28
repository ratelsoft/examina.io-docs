---
title: Configurer et utiliser la vérification d’identité eFaceID
description: Activez eFaceID, inscrivez la photo du candidat, protégez un examen et gérez la vérification biométrique ou non biométrique.
tags: [eFaceID, vérification d’identité, détection de présence, sécurité des examens]
translation_source: user-guides/manager/efaceid-identity-verification.md
translation_source_sha256: b57baa79e7123322f1bfeb125b841a120d0e2a3728779ef9713fd580395f8872
---

# Configurer et utiliser eFaceID

eFaceID confirme que la personne qui commence un examen protégé est présente
et correspond à la photo d’identité fournie par un administrateur autorisé. La
décision est liée au candidat, à l’examen et à cette tentative.

Ce guide utilise l’organisation fictive **Cedar Valley University**, la
candidate **Amina Hassan** et l’examen **BIO 201 — Human Genetics Midterm**.

!!! important "Prévoyez une solution humaine"

    La biométrie ne doit pas être l’unique moyen d’accéder à l’examen. Publiez
    un contact d’assistance et utilisez l’examen non biométrique pour les
    candidats qui refusent le consentement, ne peuvent pas utiliser la caméra
    ou ont besoin d’un aménagement.

## Avant de commencer

Prévoyez un abonnement compatible, les droits nécessaires, une photo récente
par candidat, une caméra prise en charge et une procédure non biométrique.

## 1. Activer eFaceID

Ouvrez **Facturation** et vérifiez que **Vérification eFaceID** est
**Activée**. La carte indique aussi le lieu de traitement et les durées de
conservation applicables.

![Carte eFaceID activée pour Cedar Valley University](../../assets/images/identity-proctoring/organization-efaceid-enabled.png)

Le lieu est affiché sous forme de ville ou région et de pays, par exemple
**Virginie du Nord, États-Unis**. Les paramètres de votre organisation peuvent
être différents.

## 2. Inscrire la photo du candidat

Dans **Manager**, ouvrez **Candidats**, sélectionnez la personne, choisissez
**Changer l’image**, puis téléversez un portrait récent, net, de face et bien
éclairé. Vérifiez le nom, le code du candidat et l’affectation à l’examen.

![Fiche d’Amina Hassan avec une photo d’inscription nette](../../assets/images/identity-proctoring/manager-enroll-candidate-photo.png)

N’utilisez pas une photo de groupe, une page de document numérisée, un selfie
filtré ou une image contenant plusieurs visages.

## 3. Protéger l’examen

Ouvrez les paramètres de l’examen et activez **Vérification eFaceID**.
Activez aussi **Surveillance en direct** si un surveillant doit suivre la
session. Confirmez les candidats, les sujets, les durées de conservation et la
procédure de secours.

![eFaceID et la surveillance activés pour BIO 201](../../assets/images/identity-proctoring/exam-protection-controls.png)

## 4. Parcours du candidat

Le candidat ouvre le lien officiel, puis saisit son code et son mot de passe.

![Connexion d’Amina à BIO 201](../../assets/images/identity-proctoring/candidate-sign-in.png)

## 5. Examiner le consentement

Il examine ensuite le consentement : finalité, lieu de traitement, durées de
conservation, personnes autorisées, avertissement de photosensibilité et
option d’examen non biométrique.

![Consentement à la vérification d’identité](../../assets/images/identity-proctoring/candidate-identity-consent.png)

## 6. Effectuer le contrôle de présence

Après avoir coché le consentement, il autorise la caméra, place son visage dans
le guide et suit les indications de couleur et de mouvement. Une seule personne
doit être visible et l’éclairage doit venir de face.

![Positionnement respectueux de la vie privée pour la détection de présence](../../assets/images/identity-proctoring/candidate-liveness-positioning.png)

La capture publiée utilise un portrait fictif pour protéger la vie privée ;
les contrôles correspondent au parcours réellement testé.

## 7. Comprendre la décision

**Approuvée** : le candidat poursuit vers la configuration de l’appareil ou
l’aperçu de l’examen.

**Examen requis** : la tentative est mise en pause. Un administrateur autorisé
examine le dossier et peut approuver une méthode non biométrique documentée.

**Échec technique** : vérifiez l’autorisation de la caméra, l’éclairage, le
navigateur et la connexion avant de réessayer.

**Consentement refusé ou retiré** : aucun accord biométrique n’est émis. Le
candidat choisit **Demander un examen non biométrique**.

Seule une décision de sécurité biométrique terminée est facturable. Les erreurs
d’autorisation, abandons et pannes de réseau ou du service ne sont pas des
décisions réussies. Consultez **Facturation** pour votre tarif et votre quota.

## 8. Conservation et audit

Les administrateurs autorisés voient la décision et la photo inscrite, mais la
vidéo de la caméra n’est pas mise à leur disposition dans examina.io. Les
décisions réussies et les dossiers examinés peuvent avoir des durées de
conservation différentes. N’envoyez pas d’images biométriques par courriel,
messagerie ou ticket d’assistance.

## Dépannage

**La caméra ne s’ouvre pas** : autorisez la caméra pour le site exact, fermez
les autres applications qui l’utilisent et rechargez. macOS ou Windows peut
exiger de relancer le navigateur après une nouvelle autorisation système.

**Le visage n’est pas détecté** : améliorez l’éclairage frontal, centrez le
visage et retirez les autres visages de l’image.

**Le candidat change de navigateur** : l’approbation est liée à la session de
tentative ; une nouvelle vérification peut être requise.

Pour un examen surveillé, continuez avec
[Surveillance d’un examen en direct](live-exam-proctoring.md).
