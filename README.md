# FormAItions — sprint 0

Groupe 2, FISA, sept personnes. Rapport visé le 8 décembre 2026, soutenance le 15 décembre 2026. Le professeur n’a pas annoncé de suite : le périmètre est Carrhes, parties VI et VII du cours.

Ce dépôt contient les contrats gelés et un essai graphique d’une case. Il ne simule pas encore le combat ni les généraux.

## Lancer les tests

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest
```

Si la création de l’environnement échoue parce que `ensurepip` est absent, installer le paquet `python3-venv`, ou bien :

```bash
python3 -m venv --without-pip .venv
curl -fsSL https://bootstrap.pypa.io/get-pip.py | .venv/bin/python
.venv/bin/pip install -e ".[dev]"
```

## Essai isométrique

```bash
SDL_VIDEODRIVER=dummy python -m formaitions.vue.spike
```

L’image est écrite dans `artifacts/spike_isometric.png`. Sans la variable `SDL_VIDEODRIVER`, la même commande tente d’ouvrir une fenêtre.

## À lire avant de coder

- [docs/decisions/000-groupe.md](docs/decisions/000-groupe.md) — filière, secrétaire et questions ouvertes.
- [docs/decisions/001-contrats.md](docs/decisions/001-contrats.md) — signatures et frontières entre packages.
- [docs/decisions/002-essai-pygame.md](docs/decisions/002-essai-pygame.md) — Pygame retenu après l’essai d’une case.
- [docs/decisions/003-precisions-prof.md](docs/decisions/003-precisions-prof.md) — sud-ouest, bataille non scriptée, journal des règles.

Chaque commit doit porter le nom complet `NOM Prénom` de son auteur. Voir la décision 001.

## Le premier jour

Chacun travaille sur son module et le teste avec des données fabriquées à la main. On utilise `Observation`, `Order`, `Decision` et `Carrhae`, déjà dans le dépôt. On n’invente pas un autre type d’ordre. La vue ne calcule pas les dégâts. Une IA lit l’instantané et renvoie des ordres : elle ne modifie pas le monde.

Le binôme 4 et 5 se met d’accord le premier jour sur les noms des commandes de formation. Chacun reste auteur de ses fichiers. Ils ne s’approuvent pas entre eux.

### Membre 1 — déplacement

Fichier : `src/formaitions/simulation/step.py`.

Il fait avancer une unité d’un point à un autre en temps continu, avec l’ordre `MoveTo`. Les positions sont des nombres à virgule. Une unité qui a commencé son animation d’attaque ne bouge plus jusqu’à la fin de cette animation. Chaque événement produit est daté.

Il ne gère pas encore les collisions entre unités, les dégâts, ni l’affichage.

Terminé quand un test vérifie la distance parcourue à la vitesse du légionnaire, 1,06 case par seconde, et qu’un autre test vérifie l’arrêt pendant l’animation.

### Membre 2 — carte et blocage

Fichiers à créer : `src/formaitions/simulation/carte.py` et `src/formaitions/simulation/collision.py`.

Il décrit la carte 120×120, le château au centre et l’anneau de falaises infranchissables. Il écrit le blocage entre deux cercles : une unité vivante occupe son rayon, personne ne la traverse ni ne la pousse, un mort ne bloque plus.

Ses tests appellent ces fonctions avec des positions écrites à la main. Ils ne passent pas par `step`.

Terminé quand une position sur une falaise est refusée, quand deux légionnaires de rayon 0,20 ne peuvent pas se chevaucher, et quand un mort ne bloque plus.

### Membre 3 — règles de combat

Fichier à créer : `src/formaitions/simulation/combat.py`.

Il écrit les formules de dégâts, la différence entre rechargement et animation, et la création d’un projectile. Les tests lui donnent des unités fictives, avec des PV et des armures choisis dans le sujet.

Il ne branche pas encore ces règles sur le déplacement. Une attaque ne part que si l’unité a reçu un ordre `Attack`. Le mur de boucliers se calcule ici, à partir des positions, pas à partir d’une formation de l’IA.

Terminé quand les tests retrouvent les exemples du sujet : une flèche d’attaque 12 contre une armure 6 inflige 6, et la même flèche contre un mur de boucliers inflige `max(1, 12 - 12) = 1`. Les dégâts sont calculés à la fin de l’animation, pas au début.

### Membre 4 — formes

Fichiers : `src/formaitions/formations/shapes.py` et `src/formaitions/formations/model.py`.

Il calcule les emplacements d’un bloc serré et d’un bloc lâche. Le bloc serré place les légionnaires assez près pour le mur de boucliers, à au plus 0,42 entre les centres, sans que leurs rayons de 0,20 se coupent. Le bloc lâche les écarte.

Il ne fait pas marcher les unités, il ne code pas Suréna, et il n’écrit pas scinder ni fusionner.

Terminé quand un test vérifie ces distances sur une liste de slots, sans créer de monde.

### Membre 5 — commandes de formation

Fichier : `src/formaitions/formations/commands.py`.

Il transforme deux commandes collectives en ordres individuels : avancer une formation vers un point, et la scinder en deux. Chaque résultat est une liste de `MoveTo`. Scinder produit aussi deux identifiants de formation.

Il ne choisit pas la place de chaque soldat dans la forme. Il ne code pas Crassus.

Terminé quand un test lit la liste d’ordres et vérifie qu’aucun soldat n’a été oublié, sans déplacer qui que ce soit.

### Membre 6 — affichage

Dossier : `src/formaitions/vue/`.

Il dessine une `Observation` écrite à la main : le château, une falaise, deux unités reconnaissables. Il ajoute la pause et une minicarte permanente pour se déplacer sur la carte. La vitesse peut rester affichée sans encore changer une vraie bataille.

Il ne recalcule aucun dégât et n’invente pas un second déplacement dans la vue.

Terminé quand la fenêtre s’ouvre sur cet instantané fabriqué, que la pause fige l’image, et que la minicarte montre la même scène.

### Membre 7 — scénario et IA immobile

Fichiers : `src/formaitions/scenario/carrhae.py`, `placement.py`, et `src/formaitions/ia/` pour BRAINDEAD.

Il vérifie que `"W"` est le sud-ouest, que `"E"` est le sud-est, et que le château est au centre. Il écrit la victoire romaine quand le château est à 0 PV, la victoire parthe quand aucun trébuchet n’est vivant, et le nul après une minute sans dégât. BRAINDEAD, devant n’importe quel instantané, renvoie une liste d’ordres vide.

Il ne lance pas encore une bataille complète et n’améliore pas Crassus ni Suréna.

Terminé quand ces trois issues et BRAINDEAD sont testés sur des états fabriqués à la main.

## Associer le code

On assemble dans cet ordre, dès que le module précédent existe. Le travail du premier jour n’attend pas cet ordre.

1. Le Membre 1 fournit `step`.
2. Le Membre 2 y fait refuser le passage sur une falaise et à travers une unité vivante.
3. Le Membre 7 appelle cette boucle depuis `Carrhae`, en headless, départ `"W"` au sud-ouest.
4. Le Membre 6 affiche le même état, avec la pause.
5. Le Membre 3 fait sortir les dégâts à la fin de l’animation.
6. Les Membres 4 et 5 font exécuter leurs ordres de formation par `step`, puis réassignent les slots après une mort.
7. Le Membre 7 ajoute BEDLAM, la victoire et le nul sur une vraie bataille.
8. Les Membres 4 et 5 branchent Crassus et Suréna. La sauvegarde d’une bataille, au nom du Membre 7, vient quand une partie sait déjà s’arrêter.
