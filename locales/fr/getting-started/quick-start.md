---
title: Démarrage rapide examina.io
description: Configurez votre organisation, créez ou importez un examen, ajoutez des
  candidats, attribuez des épreuves et publiez votre premier examen avec examina.io.
tags:
- configuration de l'examen
- commencer
- évaluation en ligne
- démarrage rapide
translation_source: getting-started/quick-start.md
translation_source_sha256: 535b1a2e6b873d0f6b729817ca3c9e64db7b8931167422d03e8816351d9da894
---

# Démarrage rapide : publiez votre premier examen {#quick-start-publish-your-first-exam}

Cette liste de contrôle fait passer un administrateur d'organisation d'un nouveau compte à un
lien d'examen testable. Si une autre personne rédige les questions, elle peut répondre
les étapes Designer et vous envoyer le fichier `.smex` exporté.

## 1. Confirmez l'accès du personnel {#1-confirm-staff-access}

Depuis **Accueil**, vérifiez que les personnes qui préparent l'évaluation ont le droit
[rôles de compte](roles-and-permissions.md). Utilisez **Utilisateurs** pour ajouter des comptes de personnel
et **Cercles** si l'accès doit être limité à des examens ou à des candidats particuliers.

![La galerie d'applications examina.io après la connexion](../assets/images/dashboard/apps-gallery.png)

## 2. Créez le contenu de l'examen {#2-create-the-exam-content}

Ouvrez **Designer**, puis :

1. Sélectionnez **Fichier → Nouveau projet d'examen**.
2. Créez un examen et au moins une épreuve.
3. Ajoutez des sections et des questions.
4. Définissez les instructions de l'examen et de l'épreuve, le timing, la notation et les règles de navigation.
5. Prévisualisez le contenu.
6. Exportez l'examen terminé sous forme de fichier `.smex`.

Pour des instructions de création détaillées, voir [Présentation
Designer](../user-guides/designer/introduction.md).

## 3. Importez l'examen dans Manager {#3-import-the-exam-into-manager}

Ouvrez **Manager** et choisissez **Fichier → Ajouter un nouvel examen**. Sélectionnez le fichier exporté
`.smex` et attendez le message de réussite. Vérifiez le titre importé,
le code, les papiers et les propriétés de livraison avant d'attribuer quelqu'un.

Voir [Importer les examens](../user-guides/manager/import-exams.md).

## 4. Ajouter des candidats {#4-add-examinees}

Choisissez l'une de ces approches :

- **Fichier → Ajouter un nouveau candidat** pour une ou plusieurs personnes.
- **Fichier → Importer les candidats depuis un fichier/Excel** pour une classe ou une cohorte.

Un candidat est un candidat qui passe un examen et non un utilisateur du personnel. Conservez leur code ou
Identifiant unique. Si vous importez un fichier, vérifiez le mappage des champs et prévisualisez-le avant
démarrer l'importation.

Voir [Ajouter et importer des candidats](../user-guides/manager/examinees.md).

## 5. Créez des groupes lorsque cela est utile {#5-create-groups-when-useful}

Les groupes sont facultatifs, mais ils réduisent le travail répétitif. Créer un groupe pour un
classe, cohorte, département ou séance, puis ajoutez les candidats appropriés.

Vous pouvez affecter un groupe entier à un examen tout en sélectionnant les épreuves et
heure de début facultative pour cette mission.

## 6. Attribuez l'examen et les copies {#6-assign-the-exam-and-papers}

Sélectionnez un examen et choisissez **Map Examinees** ou **Map Groups**. Déplacez le prévu
personnes ou groupes à la liste sélectionnée, continuez le mappage papier et choisissez le
papiers qu'ils peuvent prendre.

Si vous définissez une heure d'examen, sélectionnez également le fuseau horaire correct. L'heure cartographiée est
le plus tôt possible lorsque l'examen sera disponible pour ce devoir.

## 7. Configurer la livraison {#7-configure-delivery}

Avant de partager le lien, vérifiez :

- visibilité des examens ;
- si les résultats apparaissent après l'achèvement ;
- les exigences en matière de surveillance en direct et de vérification d'identité ;
- accès autorisé sur mobile ou tablette ;
- comportement de déconnexion Internet ; et
- les éventuelles exemptions de surveillance.

Gardez l'examen invisible pendant sa préparation. Rendre visible uniquement lors de l'examen
et les devoirs sont prêts.

## 8. Testez le parcours du candidat {#8-test-the-examinee-journey}

Ouvrez le lien de l'examen dans une fenêtre de navigateur privée. Confirmez que :

- le logo de l'organisation et le style de connexion sont corrects ;
- le candidat au test peut se connecter ;
- les communications attendues sont disponibles ;
- les instructions et le timing sont corrects ; et
- tout appareil, caméra, microphone ou contrôle d'identité se comporte comme prévu.

Utilisez un candidat fictif ou désigné plutôt qu’un vrai candidat.

## 9. Publier et communiquer {#9-publish-and-communicate}

Rendez l'examen visible, puis copiez **Ouvrir le lien d'examen** ou utilisez [**Envoyer un e-mail à
Candidats**](../user-guides/manager/email-examinees.md) de Manager. Inclure :

- la date de l'examen, l'heure de début et le fuseau horaire ;
- le lien de l'examen ;
- la méthode de distribution du code du candidat et du mot de passe ;
- les exigences en matière d'appareil et de navigateur ;
- les exigences en matière de surveillance ; et
- un contact d'assistance.

Partagez le [guide du jour de test du candidat](../user-guides/client/take-an-exam.md) avec
participants.

## 10. Surveiller et rapporter {#10-monitor-and-report}

Pendant la session, actualisez Manager pour voir les états de connexion actuels. Si je vis
la surveillance est activée, ouvrez l'examen sous **Proctoring**. Après les candidats
terminer, examiner les résultats individuels ou générer un rapport d’examen.

La [livraison, le suivi et le reporting
le guide](../user-guides/manager/deliver-monitor-report.md) contient les informations détaillées
liste de contrôle de fonctionnement.

!!! tip "Organiser une répétition"
    Pour une évaluation à enjeux élevés, effectuez une courte répétition avec le même
    règles de l'appareil, conditions du réseau et paramètres de surveillance prévus pour le
    véritable examen.
