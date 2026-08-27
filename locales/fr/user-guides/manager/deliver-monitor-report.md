---
title: Organiser, surveiller et créer des rapports sur les examens
description: Configurez la visibilité et la surveillance, partagez les liens d'examen, suivez les candidats et consultez les résultats dans Manager.
tags:
- livraison d'examen
- surveillance des examens
- rapports d'examen
- directeur
- surveillance
translation_source: user-guides/manager/deliver-monitor-report.md
translation_source_sha256: 74a4d64e098d4e04bc3abe5f3633c98f1b4983e3b63028da67e9a0cdbe2854ec
---

# Livrer, surveiller et créer des rapports {#deliver-monitor-and-report}

Utilisez ce guide une fois l’examen, les candidats et les mappages papier préparés.
Les actions exactes disponibles dépendent du type d'examen, du plan, du rôle et de l'état actuel
état de l'examen.

## Liste de contrôle avant la livraison {#pre-delivery-checklist}

Sélectionnez l'examen dans Manager et vérifiez :

- **Visibilité :** gardez l'examen invisible jusqu'à ce qu'il soit prêt pour les candidats.
- **Candidats cartographiés :** la liste et les devoirs sont terminés.
- **Heure :** les heures de début et les fuseaux horaires cartographiés sont corrects.
- **Affichage des résultats :** décidez si les candidats voient les résultats une fois terminés ou
  un message d'achèvement générique.
- **Surveillance en direct :** activez-la uniquement lorsque cela est nécessaire et en présence de personnel.
- **Vérification d'identité :** vérifiez les photos, le consentement, les exemptions et les solutions de secours
  contacts lorsque la fonctionnalité est utilisée.
- **Appareils :** décidez si les téléphones mobiles ou les tablettes sont autorisés et lesquels
  Mise en page client qu'ils devraient recevoir.
- **Politique de déconnexion :** choisissez ce qui doit se passer après une sauvegarde répétée
  pannes ou une perte de connexion prolongée.
- **Instructions :** confirmez que les instructions de l'examen et du papier correspondent à la finale
  règles de fonctionnement.

Le client enregistre périodiquement l'état de l'examen lorsqu'il est connecté. Une déconnexion empêche
nouvel état d'atteindre le serveur, donc la politique configurée et le candidat
les instructions doivent tenir compte de la perte du réseau.

## Testez avant de publier {#test-before-publishing}

Utilisez un candidat au test désigné et ouvrez **Ouvrir le lien d'examen** dans un navigateur privé
fenêtre. Testez le même chemin que les vrais candidats utiliseront :

1. connectez-vous avec les informations d'identification du candidat ;
2. effectuer toute vérification d'identité ou d'appareil ;
3. vérifier les papiers disponibles ;
4. commencer et répondre à un court test ;
5. reconnectez-vous après une brève interruption du réseau si possible ;
6. terminer et confirmer l'écran d'achèvement ou de résultat ; et
7. Vérifiez le résultat dans Manager.

Ne réutilisez pas les informations d'identification d'un vrai candidat pour les tests.

## Publier et envoyer l'examen {#publish-and-send-the-exam}

1. Basculez l'examen sur **Visible**.
2. Sélectionnez **Ouvrir le lien d'examen** et copiez le lien final.
3. Utilisez **Envoyer un e-mail aux candidats** lorsque les candidats mappés disposent d'une adresse e-mail valide.
   adresses, ou distribuez le lien via votre communication approuvée
   système. Voir [Envoyez un e-mail à vos candidats](email-examinees.md) pour le
   des espaces réservés de personnalisation et des liens de connexion qui enregistrent les candidats
   en tapant un code et un mot de passe.

Indiquez aux candidats la date, l'heure, le fuseau horaire, le lien, la méthode de distribution des informations d'identification,
les exigences relatives aux appareils, les attentes en matière de surveillance et le contact de l'assistance. Partagez le
[guide du jour de test](../client/take-an-exam.md).

## Surveiller une session active {#monitor-an-active-session}

La table des candidats mappés de l'examen constitue la vue de surveillance. Il montre celui de chaque personne
état de connexion et, une fois terminé, leur score.

![État de connexion et scores dans le tableau des candidats mappés](../../assets/images/manager/exam-details.png)

Manager affiche les états de mappage et de connexion tels que **Connecté**, **Prêt**,
**En cours**, **Déconnecté** et **Terminé**, avec code couleur donc en cours
assis peut être lu d'un seul coup d'œil. Actualisez la table de mappage avant de créer un
décision afin que vous disposiez des dernières données du serveur.

Selon la configuration de l'examen, les actions peuvent inclure :

- démarrer ou arrêter l'examen d'un candidat ;
- démarrer ou arrêter l'examen ;
- surveiller un candidat ou l'examen complet ;
- inspecter les informations cartographiques ; et
- déconnecter un candidat de l'examen.

Si la surveillance en direct est activée, ouvrez l'examen sous **Proctoring** depuis le
barre latérale du compte. Les surveillants devront peut-être approuver un candidat avant l'examen.
démarre.

## Gérer les incidents courants {#handle-common-incidents}

**Le candidat ne peut pas voir l'examen**

: Confirmez la visibilité, la cartographie, les articles sélectionnés, l'heure de début, le fuseau horaire et
  Accès au cercle pour le membre du personnel qui enquête.

**Le candidat ne peut pas se connecter**

: Vérifiez le lien exact de l'examen, le code, le mot de passe, le mappage de l'examen et la majuscule.
  Réinitialisez ou redistribuez les informations d'identification uniquement via un canal approuvé.

**La connexion affiche Déconnecté**

: Demandez au candidat de garder la page d'examen ouverte, de restaurer le réseau et de suivre
  le [guide de reconnexion](../client/troubleshooting.md). Actualiser Manager
  avant d'envoyer des commandes de démarrage, d'arrêt ou de déconnexion.

**Le surveillant ne peut pas voir l'examen**

: Vérifiez que la surveillance en direct est activée, que le rôle de surveillant est correct et que le
  le surveillant a accès via le Cercle concerné.

## Examiner les résultats {#review-results}

Une fois qu'un candidat a terminé, utilisez **Voir le résultat du candidat** pour un individu ou
**Voir le résultat de l'examen** pour l'évaluation. Les résultats peuvent inclure :

- questions répondues et sans réponse ;
- questions sautées ;
- score pouvant être obtenu et atteint ; et
- score en pourcentage.

Utilisez **Générer un rapport** pour un rapport d'examen plus large. Les candidats qui n'ont pas
fini peut être exclu, donc confirmez le décompte terminé avant de traiter un
rapport comme définitif.

## Corrections et reprises {#corrections-and-retakes}

**Effacer le résultat** supprime le résultat existant du candidat sélectionné pour cet examen
et peut permettre une reprise. Cette action n'est pas réversible. Avant de l'utiliser :

1. confirmer le bon candidat et l'examen ;
2. conserver tout enregistrement d'audit ou de résultat requis ;
3. enregistrer l'autorisation et le motif ; et
4. vérifier la nouvelle mission et le plan de communication.

Faites preuve de la même prudence pour supprimer un examen, un candidat ou une cartographie.
