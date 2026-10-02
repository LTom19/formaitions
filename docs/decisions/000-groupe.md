# 000 — Confirmation du groupe

Mise à jour : 2 octobre 2026, après lecture du document de cours complet et des informations du groupe.

## Confirmé

- Filière : **FISA**.
- Soutenance : **15 décembre 2026**. La date FISE du 17 janvier ne concerne pas ce groupe.
- Numéro de groupe : **2**. Le rapport devra s’appeler `2 python report.pdf`.
- Effectif : **7**. Le sujet écrit « groupes de ≈ 6 » ; l’effectif réel de ce groupe est 7.
- Dépôt d’entraînement, sur le compte personnel LTom19, privé, pour répéter le flux avant le dépôt du groupe. Les sept membres n’y sont pas. URL : https://github.com/LTom19/formaitions
- Le professeur n’a pas annoncé de suite au projet. Le périmètre est celui des parties VI et VII seulement.

## Document lu

`PythonNotesSC.pdf`, Vincent Hugot, STI 3A, 25 septembre 2026, 473 pages. Les pages 380 à 402, parties VI et VII, sont identiques à l’extrait du 2 octobre déjà utilisé pour l’architecture.

Ce qui en sort pour le projet :

- Le projet de l’année est **Partie VI — Python Project 2026–2027 : FormAItions** et **Partie VII — modalités pratiques**, sections 68 à 83.
- La partie VIII et les suivantes sont des **projets archivés**. La partie VIII est « Archived Python Project 2025–2026 ». Le sujet dit qu’en reproduire un réussi vaudrait 0/20, parce que les formations n’y sont pas.
- La section 1.4 envoie encore vers « le projet de cette année » en partie VIII, page 404. Cette phrase est périmée : la page 404 est l’archive 2025, pas FormAItions. On ne la prend pas comme consigne.
- Il n’y a pas de second scénario dans le document. Carrhes est décrit comme le premier, « et probablement le seul ».
- Les parties I à V sont le cours, les exercices et la récursivité. Elles ne ajoutent pas d’exigence au simulateur. La section 18.1 fixe la version de Python : 3.9 est le minimum écrit, et 3.10 devient obligatoire dès sa sortie, ce qui est le cas depuis 2021.
- Les anciennes listes titrées « Requirements » (sections 85 et 87.1) appartiennent aux archives. Elles ne sont pas la liste de cette année.

## Pas encore fixé

- Secrétaire (format `NOM Prénom`) : `____`. Le sujet le recommande. Il suit qui fait quoi, assemble le PDF, et garde son module. Il n’est pas automatiquement le chef.
- Nombre exact de jours entre le rapport et la soutenance : le sujet dit « quelques jours avant », sans chiffre. Le Git part immédiatement avant la soutenance, les diapositives immédiatement après.
- Noms des sept membres. Les rôles ci-dessous restent ceux de la répartition, en attendant les noms.

| Rôle | Module principal | Nom (`NOM Prénom`) |
| --- | --- | --- |
| Membre 1 | temps, déplacement, événements | |
| Membre 2 | carte et collisions | |
| Membre 3 | règles de combat | |
| Membre 4 | formes, cohésion, Crassus | |
| Membre 5 | commandes collectives, Suréna | |
| Membre 6 | vue 2.5D | |
| Membre 7 | scénario, IA de référence, campagne | |

Chaque personne configure Git localement, sans compte partagé :

```bash
git config user.name "NOM Prénom"
git config user.email "adresse-identifiable"
```

Le nom doit être le même que dans le rapport. On ne réécrit pas l’historique pour le corriger après coup.

## Liste d’exigences de travail

Les sections 68 à 83, titres du sujet. Aucune autre liste numérotée ne figure dans le projet de cette année. Statut actuel : non commencée. Le sprint 0 ne les réalise pas.

- 68 — S’en tenir au cahier des charges — Simulateur
- 69 — Périmètre du projet — Simulateur
- 70 — Le problème central : les formations — Simulateur et IA
- 71 — Scénario 1 : Carrhes — Simulateur
- 71.1 — Forces initiales — Simulateur
- 71.2 — Le champ de bataille — Simulateur
- 71.3 — Conditions de victoire — Simulateur
- 72 — Unités et statistiques exactes de simulation — Simulateur
- 72.1 — Collision — Simulateur
- 72.2 — Animation d’attaque — Simulateur
- 72.3 — Légionnaire — Simulateur
- 72.4 — Cataphracte d’élite — Simulateur
- 72.5 — Archer de cavalerie lourd — Simulateur
- 72.6 — Trébuchet — Simulateur
- 72.7 — Château — Simulateur
- 73 — Mécaniques de combat — Simulateur
- 74 — Ce que le général romain doit chercher à faire — IA
- 75 — Ce que le général parthe doit chercher à faire — IA
- 76 — Visualisation — Interface
- 77 — Évaluation — critères du jury, pas un barème
- 78 — Mangez-le par petites bouchées — méthode
- 78.1 — Sergent BRAINDEAD — IA
- 78.2 — Major BEDLAM — IA
- 78.3 — Généraux YOURWITTYAINAMEGOESHERE_ROMAN et _PARTHIAN — IA
- 78.4 — davantage ? — IA
- 79 — Démonstration finale — Soutenance
- 80 — Groupes : taille et composition — organisation
- 81 — Évaluation — Rapport, Soutenance, Git
- 82 — Court rapport — Rapport
- 83 — La soutenance — Soutenance
- 83.0.1 — Horaires de passage — Soutenance
- 83.0.2 — Minutage — Soutenance
- 83.0.3 — Les diapositives — Soutenance
- 83.0.4 — La démonstration en direct — Soutenance

Les sections 74 et 75 décrivent le problème tactique. Elles n’imposent pas un algorithme. La section 77 n’est pas une grille de points.

Échéance connue : soutenance le 15 décembre 2026. Le découpage en sprints reste relatif tant que le calendrier des séances sur Celene n’est pas relevé.

## Questions encore ouvertes

1. Combien de jours avant le 15 décembre le rapport doit-il être sur Celene ? Le Git se remet-il en archive, par lien vers GitHub, ou les deux ?
2. Les exigences du rapport sont-elles bien les sections 68 à 83, tant que le sujet est marqué « travail en cours » ?
3. « Coin ouest » désigne-t-il un coin de la carte ou le bord ouest ?
4. Un trébuchet qui rate inflige-t-il zéro dégât, ou une dispersion ? La salve de 5 du château vise-t-elle une cible ou cinq ?
5. La sauvegarde citée pour la soutenance est-elle exigée, ou seulement un exemple ?
6. L’interaction du jury consiste-t-elle à relancer des paramètres, ou aussi à commander des unités ?
7. Le code des années précédentes annoncé par le `TODO` du sujet est-il disponible ? Le groupe ne l’attend pas pour commencer, et ne reprend pas le projet 2025.
