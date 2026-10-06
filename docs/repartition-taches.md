# Répartition des tâches — FormAItions, groupe 2

Document de travail. Il reprend les parties VI et VII du cours (sections 68 à 83, Vincent Hugot, 25 septembre 2026) et les contrats déjà gelés dans `docs/decisions/`. Il ne change pas ces contrats. Une modification de `Observation`, `Order` ou `step` reste soumise à deux revues, dont celle du membre 1.

Sept membres, sept paquets de **huit tâches**. Les tâches 1 à 6 se codent et se testent sans attendre le code d’un autre. Les tâches 7 et 8 branchent ce paquet sur le reste. Chacun écrit les tests de ses huit tâches. Chacun relit les pull requests d’un seul autre membre, jamais les siennes.

Le secrétaire n’est pas encore nommé. Le sujet ne lui retire qu’une petite part de code. Ce document ne lui enlève aucune des huit tâches : le rapport et les diapositives sont un travail du groupe, en plus, au moment du rendu.

## Nombres du sujet utilisés partout

Carte 120×120. Château au centre, emprise 4×4, anneau de falaises d’une case, infranchissable au sol, franchissable par un tir. Pas de simulation : `FIXED_DT = 0,05` s. `speed` change le rapport au temps réel, pas ce pas.

| Unité | PV | Attaque | Armure mêlée | Armure perçage | Portée | Vitesse | Rechargement | Animation | Rayon |
| --- | ---: | --- | ---: | ---: | --- | ---: | ---: | ---: | ---: |
| Légionnaire | 75 | mêlée 16 | 6 | 6, +6 en mur | 0 (contact) | 1,06 | 2,0 s | 1,26 s | 0,20 |
| Cataphracte d’élite | 150 | mêlée 14 | 5 | 5 | 0 (contact) | 1,35 | 1,7 s | 1,36 s | 0,25 |
| Archer de cavalerie lourd | 80 | perçage 12 | 5 | 6 | 8 | 1,44 | 1,8 s | 1,17 s | 0,25 |
| Trébuchet | 150 | perçage 200, +250 bâtiments | 2 | 8 | 4 à 16 | 0,80 | 10 s | 1,00 s | 0,50 |
| Château | 10000 | perçage 15, salve de 5 | — | 13 | 11 | — | 2 s | — | emprise 4×4 |

Contact : distance des centres inférieure ou égale à la somme des rayons, sans que les disques se recouvrent. Mur de boucliers : au moins 4 autres légionnaires à une distance de centres ≤ 0,42. Piétinement : à la fin de l’attaque, toute cible dont le centre est à ≤ 0,75 du centre de la cataphracte. Dégâts ordinaires : `max(1, attaque − armure)`. Dégâts à plusieurs types : `max(1, Σ max(0, attaque_i − armure_i))`. Les points de vie baissent à la **fin** de l’animation, pas au début.

Ordres du monde, et rien d’autre : `MoveTo`, `Hold`, `Attack`, `Pack`, `Unpack`. Les sept commandes de formation (`FormCircle`, `Advance`, `Screen`, `Spread`, `Transition`, `Split`, `Merge`) sont traduites en ces ordres. Elles ne sont pas des ordres du monde.

Hypothèses encore jaunes, à la charge du membre 3, déjà écrites dans la décision 001 : un trébuchet qui rate inflige 0, sans dispersion ; la salve du château émet cinq projectiles en fin d’animation vers l’ennemi le plus proche à portée, et les projectiles en trop frappent cette même cible. L’armure de classe « bâtiment » du château est prise à 0 tant que le professeur n’a pas tranché : un tir de trébuchet réussi vaut alors `max(1, max(0, 200−13) + max(0, 250−0)) = 437`.

## Règles communes aux sept

- Chaque membre est l’auteur de ses fichiers. Il ne commit pas dans les fichiers d’un autre. Le nom Git est `NOM Prénom`, comme dans le rapport.
- Branche courte, pull request, au moins une revue extérieure à l’auteur. Les membres 4 et 5 ne s’approuvent pas.
- Le premier jour, chacun teste son module avec des données écrites à la main. Il n’invente pas un type d’ordre. La vue ne calcule pas de dégâts. Une IA lit une `Observation` et renvoie des ordres : elle ne modifie pas le monde.
- `formations` n’importe pas `simulation`, `ia`, `vue`, ni Pygame. `simulation` n’importe pas `ia`, `formations`, `vue`, `scenario`, ni Pygame. `ia` lit `domaine` et peut appeler `formations`. `vue` lit des instantanés. `scenario` appelle `simulation` et `ia`, et `vue` seulement si la bataille n’est pas headless.
- Un général voit toutes les unités et leurs PV, pas leur direction. `Decision.rule` n’est jamais vide.
- `"W"` est le sud-ouest, `"E"` le sud-est. L’axe x va vers l’est, l’axe y vers le sud.

## Membre 1 — temps, déplacement, événements

Fichiers : `src/formaitions/simulation/step.py`, et `src/formaitions/simulation/mouvement.py` s’il découpe le fichier. Tests : `tests/test_step.py`.

Il fait avancer le monde d’un pas. Il ne calcule pas un dégât, il ne dessine rien, il ne choisit pas une formation.

1. **Pas gelé.** `step(world, orders, dt=0.05)` avance `now` de 0,05 s et renvoie une liste d’`Event` dont chaque `time` vaut le temps du monde à la fin du pas. Un `dt` différent de 0,05 lève `ValueError`. `speed` n’apparaît pas dans cette fonction. Terminé quand un test refuse `dt=0.1` et qu’un autre vérifie `now` après exactement 20 pas (1 seconde de jeu).

2. **Déplacement continu.** Un ordre `MoveTo` déplace l’unité en ligne droite, en nombres flottants, sans tour par tour. Distance par pas = vitesse × 0,05. Vitesses : légionnaire 1,06, cataphracte 1,35, archer 1,44, trébuchet 0,80. L’unité s’arrête sur la destination sans la dépasser. Terminé quand un légionnaire parti de `(0, 0)` vers l’est a `x = 1.06` après 20 pas, à la tolérance des flottants, et qu’un trébuchet a parcouru 0,80 dans le même temps.

3. **Hold.** `Hold` annule la destination en cours. La position ne change pas aux pas suivants. Un `MoveTo` ultérieur remplace ce `Hold`. Terminé quand un test enchaîne `MoveTo`, puis `Hold`, puis constate l’arrêt, puis un second `MoveTo` et constate la reprise.

4. **Gel pendant l’animation.** Si `attack_animation_remaining > 0`, la position ne change pas, même avec un `MoveTo`. Le membre 1 décrémente ce compteur de 0,05 à chaque pas, et `reload_remaining` de la même façon. Le rechargement seul n’interdit pas de marcher. Durées d’animation qu’il doit respecter quand le membre 3 les aura posées : 1,26 s, 1,36 s, 1,17 s, 1,00 s. Pour ses tests à lui, il fabrique une unité avec `attack_animation_remaining = 1.26` et vérifie qu’elle n’a pas bougé après 25 pas (1,25 s) et qu’elle peut repartir au pas où le compteur tombe à 0. Il n’enlève aucun point de vie.

5. **Emballer et déballer.** `Pack` et `Unpack` ne concernent que le trébuchet. La transition dure 11 s (220 pas). Pendant ces 11 s, un `MoveTo` et un `Attack` sont refusés. Un trébuchet emballé accepte `MoveTo` et refuse `Attack`. Un trébuchet déballé accepte `Attack` (le tir lui-même est au membre 3) et refuse `MoveTo` tant qu’il n’est pas emballé. Deux événements datés : début et fin de transition. Terminé quand un test compte 220 pas entre les deux événements et vérifie les refus.

6. **Ordre refusé, visible au pas d’après.** Le monde peut refuser. Le pas du refus émet `order_refused` avec l’identifiant de l’unité. Au pas suivant, l’unité exécute encore l’ordre précédent, pas l’ordre refusé. Tant que le membre 2 n’est pas branché, le cas testé ici est celui de la tâche 5 (trébuchet), pas une falaise.

7. **Appeler le blocage, sans l’écrire.** Dès que `formaitions.simulation.collision.blocked` existe, `step` l’appelle avant d’écrire la nouvelle position. Si la position est refusée, l’unité ne l’occupe pas, ne pousse personne, et ne garde pas d’élan : elle s’arrête, ou elle glisse le long de l’obstacle si une position voisine sur le même pas est libre. Le membre 1 n’édite pas `collision.py`. Terminé quand un test, qui injecte un `blocked` faux refusant `x > 2`, arrête l’unité à la frontière.

8. **Appeler le combat à la fin de l’animation, sans écrire la formule.** Quand `attack_animation_remaining` passe de positif à zéro dans le pas, `step` appelle `formaitions.simulation.combat.resolve_attack_end`. Avant que ce module existe, l’appel est une fonction vide que le test remplace. Le membre 1 vérifie seulement que l’appel a lieu au bon pas, une seule fois, avec l’identifiant de l’attaquant. Il n’édite pas `combat.py`.

Revue qu’il doit faire : les pull requests du membre 3, parce que le moment des dégâts est un contrat de `step`.

## Membre 2 — carte et collisions

Fichiers à créer : `src/formaitions/simulation/carte.py`, `src/formaitions/simulation/collision.py`. Tests : `tests/test_carte.py`, `tests/test_collision.py`. Ces tests n’importent pas `step`.

Il dit où l’on a le droit de poser un disque. Il ne déplace pas l’unité, il n’enlève pas de points de vie, il ne décide pas du mur de boucliers.

1. **Carte.** `build_map(map_size=(120, 120))` décrit une plaine sans forêt, eau, mur, colline ni relief. Le château est centré : son centre est `(largeur/2, hauteur/2)`, son emprise est le carré 4×4 autour de ce centre. Un anneau d’exactement une case de falaises entoure cette emprise. Si `map_size` change, le château reste au centre et l’anneau se redessine autour de lui. Terminé quand un test sur `(120, 120)` et un test sur `(80, 80)` retrouvent le centre et comptent les cases de l’anneau.

2. **Sol infranchissable.** `blocks_ground(map, position)` est vrai sur une case de falaise et sur l’emprise du château. Il est faux sur la plaine. `blocks_shot(map, position)` est faux partout : un tir passe au-dessus des falaises. Terminé quand une position sur l’anneau est refusée au sol et acceptée pour un tir, et qu’une position de plaine est acceptée pour les deux.

3. **Quatre rayons.** `radius(kind)` vaut 0,20, 0,25, 0,25 et 0,50 pour le légionnaire, la cataphracte, l’archer et le trébuchet. `overlaps(a, b)` est vrai quand la distance des centres est **strictement inférieure** à la somme des rayons. Le contact exact (égalité) ne se recouvre pas : il est permis. Terminé quand deux légionnaires à distance 0,39 se recouvrent, à distance 0,40 ne se recouvrent pas, et quand un trébuchet (0,50) et un légionnaire (0,20) se recouvrent en dessous de 0,70.

4. **Vivant bloque, mort non.** `blocked(unit, position, others, map)` est vrai si la position tombe sur une falaise, sur le château, ou sur le disque d’une unité de `others` dont `alive` est vrai. Une unité morte ne bloque pas, même si sa position est au même endroit. Allié et ennemi bloquent de la même façon. La fonction ne modifie pas les listes reçues. Terminé quand les trois cas du README passent : falaise refusée, deux légionnaires de rayon 0,20 qui ne peuvent pas se chevaucher, mort qui ne bloque plus.

5. **Segment.** `segment_blocked(start, end, others, map)` est vrai si un disque du rayon de l’unité, déplacé le long du segment, toucherait un obstacle de la tâche 4. Le membre 1 s’en sert pour le contournement. Le membre 2 ne déplace personne. Terminé quand un segment qui rase un légionnaire vivant est refusé, et que le même segment est accepté si ce légionnaire est mort.

6. **Voisinage, sans bonus.** `units_within(units, origin, radius)` renvoie les unités vivantes dont le centre est à une distance ≤ `radius` de `origin`, origine exclue. Le membre 3 l’appellera avec 0,42 (voisins d’un légionnaire) et 0,75 (piétinement). Le membre 2 ne sait pas ce qu’est une armure. Terminé quand un test place cinq points à 0,42 et un sixième à 0,43, et ne récupère que les cinq.

7. **Branchement dans `step`, sans éditer `step.py`.** Il prévient le membre 1 dès que la signature de `blocked` est stable. Il n’écrit pas le `if` dans `step`. Son test d’intégration, dans `tests/test_collision.py`, appelle `step` avec un `MoveTo` vers une falaise et attend l’événement `order_refused` ou l’arrêt devant l’anneau. Ce test est marqué et n’est exigé qu’après la tâche 7 du membre 1. Avant ça, les tâches 1 à 6 restent vertes seules.

8. **Emprise et placement.** Il exporte `castle_footprint(map)` et `cliff_tiles(map)` pour le membre 7. Un test vérifie qu’aucune case de l’emprise n’est dans `cliff_tiles`, et que les deux ensembles sont disjoints de la plaine jouable. Il ne place pas les armées.

Revue qu’il doit faire : les pull requests du membre 1, parce qu’il vérifie que `step` appelle bien `blocked` sans recopier la géométrie.

## Membre 3 — règles de combat

Fichier à créer : `src/formaitions/simulation/combat.py`. Tests : `tests/test_combat.py`, sur des unités fictives, sans `step` et sans `formations`.

Il transforme un ordre `Attack` arrivé au bout de son animation en dégâts et en projectiles. Il ne déplace pas les unités, il ne fait pas voler le projectile (la position du projectile avance dans `step`, tâche 1 du membre 1, une fois le projectile créé), il ne décide pas qui il faut viser.

1. **Formule simple.** `damage_simple(attack, armour) = max(1, attack - armour)`. Le test du sujet : attaque 12 contre armure 6 retourne 6. La même attaque contre une armure 12 retourne 1. Une attaque inférieure à l’armure ne retourne jamais 0.

2. **Formule à plusieurs types.** `damage_typed(pairs) = max(1, sum(max(0, attack_i - armour_i)))`. Trébuchet contre château, hypothèse jaune documentée dans le nom du test : paires `(200, 13)` et `(250, 0)`, résultat 437. Si le professeur fixe une autre armure de bâtiment, seul ce test et cette constante changent.

3. **Mur de boucliers.** `shield_wall(legionary, units)` est vrai si au moins 4 autres légionnaires vivants ont leur centre à ≤ 0,42. Le bonus est +6 d’armure de perçage, et seulement de perçage : la mêlée reste à 6. Le mur ne consulte pas l’identifiant de formation. Un test avec 4 voisins à 0,42 donne une flèche de 12 qui inflige 1. Un test avec 3 voisins inflige 6. Un test où l’un des 4 meurt (`alive=False`) inflige 6 au calcul suivant. La distance est lue sur les positions, ou via `units_within` du membre 2 si ce module est déjà importable ; les tests de cette tâche fabriquent les positions eux-mêmes et n’échouent pas si `collision.py` est absent.

4. **Qui a le droit de tirer.** `can_start_attack(attacker, target, map)` est faux si l’attaquant n’a pas d’ordre `Attack`, si `reload_remaining > 0`, si une animation est déjà en cours, ou si la cible est hors de portée. Portées : légionnaire et cataphracte au contact (tâche 3 du membre 2 : distance ≤ somme des rayons) ; archer ≤ 8 ; trébuchet entre 4 et 16 inclus ; château ≤ 11. Le château et le trébuchet ne frappent pas en mêlée à travers les falaises : un légionnaire au contact du château, de l’autre côté de l’anneau, n’est pas une cible de mêlée valide, et un légionnaire n’a aucune attaque contre le château. Terminé quand chaque portée a un test juste en dessous et juste au-dessus du seuil.

5. **Fin d’animation.** `resolve_attack_end(...)` applique les dégâts. L’appeler au début de l’animation est une erreur que le test interdit : un second appel avec `animation_just_finished=False` ne retire rien. Cataphracte : la cible principale doit être au contact, sinon la fonction ne retire rien ; si elle l’est, la cible principale et toute unité vivante à ≤ 0,75 du centre subissent `damage_simple(14, armure_de_melee)`. Archer : précision 100 %, création d’un `ProjectileState` vers la cible, dégâts au moment où `step` signalera l’impact, pas à la création. Le test d’archer vérifie qu’un projectile a été ajouté et que les PV n’ont pas encore baissé dans cette fonction si le projectile n’est pas arrivé. Pour l’archer, l’arrivée est immédiate dans le test unitaire seulement si la fonction reçoit `impact=True` ; le vol lui-même n’est pas codé ici.

6. **Trébuchet et château.** Le jet est tiré dans le générateur fourni par l’appelant, au moment du tir. Contre un bâtiment, seuil 0,80 ; contre une unité, seuil 0,15. En dessous du seuil, le tir est réussi et passe par la formule de la tâche 2 (bâtiment) ou 1 (unité). Au-dessus, les dégâts valent 0 et un événement `shot_missed` est prévu dans les détails. Le château, en fin d’animation, crée cinq projectiles d’attaque 15 vers l’ennemi vivant le plus proche dont la distance est ≤ 11. S’il n’y a qu’une cible, les cinq ont cette cible. S’il n’y a personne à portée, il ne crée rien. Le rechargement du château (2 s) et du trébuchet (10 s) est un nombre retourné à `step`, pas un `sleep`. Terminé quand un générateur truqué à 0,79 puis 0,80 fait réussir puis rater un tir sur le château, et quand la salve compte cinq projectiles.

7. **Liste d’événements, pas d’écriture cachée.** La fonction retourne les nouveaux projectiles, les nouveaux PV et les événements (`damage`, `shot_missed`, `shield_wall_on`, `shield_wall_off`). Elle ne va pas chercher le monde global. Terminé quand un test remplace les PV d’entrée et vérifie que l’objet d’entrée n’a pas été muté : la copie de sortie porte les nouveaux PV.

8. **Attendre le pas, puis prouver la date.** Après la tâche 8 du membre 1, un test d’intégration construit une unité dont l’animation vaut 0,05, appelle `step` une fois, et vérifie que les PV baissent dans ce pas-là et pas avant. Ce test vit dans `tests/test_combat.py`. Il n’est pas exigé pour considérer les tâches 1 à 7 comme faites.

Revue qu’il doit faire : les pull requests du membre 4. Il vérifie que Crassus ne recalcule pas le mur de boucliers dans l’IA, et qu’il se contente de demander une forme serrée ou lâche.

## Membre 4 — formes, cohésion, Crassus

Fichiers : `src/formaitions/formations/shapes.py`, `src/formaitions/formations/model.py`, et `src/formaitions/ia/crassus.py` à créer. Tests : `tests/test_shapes.py`, `tests/test_crassus.py`. Aucun test ne crée de monde et aucun n’appelle `step`.

Il dit où chaque soldat devrait être, et ce que le général romain décide. Il ne fait pas marcher les unités. Il n’écrit pas la traduction `Split` / `Merge`. Il n’écrit pas Suréna.

1. **Bloc serré.** `slots(Shape.BLOCK_DENSE, ids, anchor)` renvoie une position par identifiant. Pour des légionnaires, chaque paire de voisins de grille est à une distance strictement supérieure à 0,40 et inférieure ou égale à 0,42. Sur un groupe d’au moins 5, au moins un légionnaire a 4 autres centres à ≤ 0,42, sinon le mur du membre 3 ne pourra jamais s’activer. Terminé quand ce test passe sur 5, sur 60, et échoue si quelqu’un écarte les slots à 0,50.

2. **Bloc lâche.** `Shape.BLOCK_LOOSE` sur les mêmes identifiants. Aucun légionnaire n’a 4 voisins à ≤ 0,42. Les slots ne se recouvrent pas (distance > 0,40). Terminé quand le prédicat du mur, recopié dans le test comme une distance et pas importé depuis `combat.py`, est faux pour tout le groupe.

3. **Cercle et ligne.** `Shape.CIRCLE` répartit les identifiants sur un cercle autour de `anchor`, ou autour d’une position passée pour « autour de cette unité ». `Shape.LINE` les aligne. Les disques de rayon 0,20 ne se recouvrent pas. Le cercle complet de rayon 8 demandé par le calcul du sujet (~125 légionnaires) n’est pas une tactique à utiliser avec 60 hommes : la fonction doit quand même exister. Terminé quand 8 points de cercle ont le même rayon et des angles réguliers, et quand une ligne de 10 a un pas constant > 0,40.

4. **Après une mort.** `reassign(formation, living_ids)` enlève les morts, garde chaque vivant, et recalcule les slots de la forme courante. Personne n’est inventé. L’ancre ne saute pas de l’autre côté de la carte : le centre des nouveaux slots reste à moins d’un pas de grille de l’ancien centre. Terminé sur une formation de 10 dont on retire 3 identifiants.

5. **Écart de cohésion.** `cohesion_error(positions, slots)` est la plus grande distance entre un soldat et son slot. Ce n’est pas un déplacement. Crassus s’en sert comme signal. Terminé quand l’erreur vaut 0 si les positions sont les slots, et vaut la distance imposée si un seul soldat est décalé.

6. **Crassus, six règles, sur un instantané fabriqué.** `Crassus(...).decide(observation, now)` renvoie une liste d’`Order` et enregistre des `Decision` dont `rule` est exactement l’un de ces noms :
   - `trebs_behind_infantry` : les trois trébuchets reçoivent un `MoveTo` dont la destination est du côté opposé à l’ennemi le plus proche, derrière le bloc de légionnaires, pas au contact ;
   - `screen_cataphracts` : une partie des légionnaires, pas les trébuchets, reçoit des `MoveTo` situés entre la cataphracte la plus menaçante et le trébuchet le plus proche d’elle ;
   - `dense_against_arrows` : si un archer ennemi est à une distance ≤ 8 d’un légionnaire, la forme demandée est le bloc serré ;
   - `spread_against_trample` : si une cataphracte est au contact d’un légionnaire, la forme demandée est le bloc lâche, même si des archers sont aussi là (le piétinement gagne dans ce cas, et le test le fixe) ;
   - `do_not_chase` : un archer situé plus loin que la portée 8 ne devient pas la destination de tous les légionnaires ;
   - `sacrifice_periphery` : si une cataphracte est plus proche d’un trébuchet que le gros du bloc, seuls les légionnaires du bord reçoivent un `MoveTo` vers ce trou, et le trébuchet reçoit `Hold` ou un `MoveTo` qui l’éloigne, jamais un `Attack` de mêlée.

   Chaque règle a son test, avec une `Observation` écrite à la main. `decide` ne modifie pas l’observation.

7. **Poids.** Le constructeur expose au moins `aggressiveness` (nombre). Sur la même observation, deux valeurs changent un seuil visible : par exemple la distance à laquelle `screen_cataphracts` se déclenche. Aucun de ces seuils n’est une constante inaccessible. Terminé quand les deux appels ne produisent pas la même liste d’ordres, et que les deux journalisent la règle qui a gagné.

8. **Passer par le traducteur, sans le réécrire.** Tant que `translate` du membre 5 n’existe pas, Crassus a le droit de construire des `MoveTo` à partir de `slots`. Dès que `translate` est importable, Crassus l’utilise pour `Advance`, `Screen`, `Spread` et `Transition`, et le test 8 vérifie qu’il n’y a plus de seconde copie de la géométrie des commandes dans `crassus.py`. Il n’édite pas `commands.py`.

Revue qu’il doit faire : les pull requests du membre 7. Il vérifie que `Carrhae` appelle `decide` sans écrire une trajectoire à la place de Crassus, et que les effectifs lus par l’IA viennent de l’observation, pas de constantes 60, 20, 20, 3.

## Membre 5 — commandes de formation et Suréna

Fichier : `src/formaitions/formations/commands.py`. Fichier à créer : `src/formaitions/ia/surena.py`. Tests : `tests/test_commands.py`, `tests/test_surena.py`.

Il traduit une intention collective en ordres individuels, et il décide pour les Parthes. Il ne choisit pas la place géométrique de chaque soldat dans la forme : il reçoit `slots_for(shape, ids, anchor)`. Il ne code pas Crassus. Il ne déplace personne.

Les noms sont déjà gelés. Le premier jour, il relit cette liste avec le membre 4 et il ne la change pas : `FormCircle`, `Advance`, `Screen`, `Spread`, `Transition`, `Split`, `Merge`.

1. **Advance.** `translate(Advance, formation, slots_for)` produit exactement un `MoveTo` par membre, vers le slot de la forme courante ramené sur `destination`. Aucun id oublié, aucun id doublé, aucun id étranger. Le test injecte un `slots_for` faux qui retourne des positions connues, et compare les destinations une à une. Il n’appelle pas le vrai `slots` du membre 4.

2. **Split.** Entrée : une formation et `member_ids` de ceux qui partent. Sortie : deux nouvelles formations (deux identifiants neufs, différents de l’ancien), la partition exacte des membres, et les `MoveTo` de chaque moitié vers les slots que `slots_for` renvoie pour cette moitié. Chaque soldat d’origine est dans une seule des deux. Terminé sur une formation de 10 dont 4 partent.

3. **Merge.** Entrée : deux formations. Sortie : un identifiant neuf, l’union des membres sans doublon, et des `MoveTo` vers `slots_for` sur cette union. Terminé quand 3 + 5 membres donnent 8 ordres.

4. **Screen.** Les slots sont demandés au `slots_for` du bloc courant, puis placés le long du segment qui va de l’unité protégée (`protected_unit_id`) à `threat`. Le test fabrique un protégé en `(0, 0)`, une menace en `(10, 0)`, et vérifie que chaque destination a un `x` strictement entre les deux. Aucun ordre ne déplace l’unité protégée si elle n’est pas membre de la formation.

5. **Spread, Transition, FormCircle.** `Spread` demande la forme lâche et renvoie les `MoveTo`. `Transition` remplace `formation.shape` dans la copie retournée (la formation d’entrée n’est pas mutée) et renvoie les `MoveTo` vers les nouveaux slots. `FormCircle` fait la même chose avec le cercle, autour du point ou de l’unité selon les champs déjà présents sur la commande. Trois tests, un par commande, toujours avec un `slots_for` injecté.

6. **Contrat d’injection.** La signature publique de `translate` prend `slots_for` en argument. Elle n’importe pas `simulation`. Un test vérifie que le module `commands` n’a pas chargé `step`, `combat`, `pygame` ni `surena`.

7. **Suréna, cinq règles, sur un instantané fabriqué.** `Surena(...).decide(observation, now)` :
   - `retreat_if_legionaries_close` : un archer qui a un légionnaire vivant à une distance inférieure à un seuil (poids, défaut inférieur à 8 pour qu’il puisse encore tirer) reçoit un `MoveTo` qui augmente cette distance, pas un `Attack` ;
   - `lure_away_from_trebs` : si un groupe de légionnaires est loin des trébuchets, une partie des archers seulement reçoit un `MoveTo` vers ce groupe, et les cataphractes ne suivent pas toutes ;
   - `attack_through_gap` : si le segment entre une cataphracte et un trébuchet ne passe près d’aucun légionnaire (distance au segment supérieure au rayon 0,20, calcul local dans le test), cette cataphracte reçoit un `MoveTo` vers ce trébuchet puis, au contact dans un second instantané, un `Attack` vers son id ;
   - `abandon_bad_engagement` : une cataphracte sous le seuil de PV du poids reçoit un `MoveTo` de repli et pas un `Attack`, même si un légionnaire est au contact ;
   - `snipe_trebs` : si un trébuchet est à portée 8 d’un archer, cet archer reçoit `Attack` sur le trébuchet plutôt que sur un légionnaire plus proche. C’est le cœur de la section 75 : tuer les trébuchets, pas farmer l’infanterie.

   Cinq tests, cinq observations. `decide` ne modifie pas l’observation. Chaque décision a un `rule` non vide.

8. **Poids et absence de script.** Le constructeur expose au moins `boldness`. Deux valeurs sur la même observation changent `abandon_bad_engagement` ou la taille du groupe envoyé dans `lure_away_from_trebs`. Un test donne deux fois la même observation et n’exige pas les mêmes ordres si le poids change. Un autre test vérifie qu’aucune destination n’est une constante de carte du genre « aller en (60, 60) quoi qu’il arrive » : en déplaçant le trébuchet dans l’observation, la destination de `attack_through_gap` suit le trébuchet.

Revue qu’il doit faire : les pull requests du membre 6. Il vérifie que la vue ne contient pas une deuxième copie de `translate` ni un déplacement de formation au clavier.

## Membre 6 — vue 2.5D

Dossier : `src/formaitions/vue/`. L’essai existant `spike.py` reste lançable. Le rendu de bataille est un nouveau module, par exemple `src/formaitions/vue/bataille.py`. Tests : `tests/test_vue.py`, avec `SDL_VIDEODRIVER=dummy`. `import formaitions.vue` ne charge pas Pygame : le test `tests/test_vue_import.py` doit rester vert.

Il dessine un instantané. Il ne recalcule aucun dégât, aucune collision, aucun slot.

1. **Fenêtre isométrique.** Une `Observation` fabriquée (plaine, une falaise, le château, deux unités) produit une surface Pygame en projection 2:1, dans la continuité de `spike.py`. Pas de 3D. Terminé quand le test dummy écrit une image et trouve les couleurs convenues de la falaise et du château à des pixels différents.

2. **Unités reconnaissables.** Quatre dessins distincts : légionnaire, cataphracte, archer, trébuchet, plus le château. Les sprites d’Age of Empires II sont la cible dès que la source est confirmée par l’enseignant. En attendant, quatre silhouettes de formes différentes, documentées dans le module comme provisoires. Un projectile est un trait ou un point entre `position` et `target`. Un mort (`alive=False`) est une marque au sol, plus petite, et n’utilise pas le sprite de l’unité vivante. Terminé quand un test d’image distingue les quatre types par un pixel de contrôle chacun.

3. **Caméra, sans physique.** Le défilement change la fenêtre visible sur la carte. Les coordonnées du monde ne sont pas modifiées. Un test appelle le décalage de caméra et vérifie que l’`Observation` d’entrée est inchangée.

4. **Minicarte permanente.** Un rectangle fixe dans un coin dessine la carte entière : château, falaises, unités. Un clic (en test : un appel `pan_to_minimap(x, y)`) recentre la caméra sur le point correspondant. La touche M du sujet n’est pas exigée en plus : le groupe a déjà décidé que la minicarte reste affichée. Terminé quand la minicarte et la vue principale comptent le même nombre d’unités vivantes pour le même instantané.

5. **Pause.** Une touche, exposée aussi comme `set_paused(True)`, fige le dessin : deux captures successives sont identiques, et le temps affiché reste `observation.now`. La reprise affiche l’instantané suivant quand on lui en donne un nouveau. La pause ne crée pas d’ordre.

6. **Vitesse.** Des valeurs 0,5, 1, 2 et 4 sont affichées et stockées dans un objet `Playback` que le membre 7 lira. Changer la vitesse ne modifie pas `FIXED_DT` et ne lance pas de bataille. Terminé quand un test passe de 1 à 4 et vérifie que `Playback.speed` vaut 4, et que `FIXED_DT` vaut encore 0,05.

7. **Lire l’état, ne pas l’inventer.** Le trébuchet `packed=True` et le trébuchet `packed=False` ont deux dessins. Le mur de boucliers n’est dessiné que si l’instantané porte l’information. Aujourd’hui `UnitState` n’a pas ce champ : le membre 6 ne le devine pas depuis les distances. Il décrit le champ voulu (`shield_wall: bool`) dans la pull request, et il attend les deux revues, dont le membre 1, avant de l’utiliser. Tant que le champ n’est pas dans `domaine`, le test de cette tâche vérifie seulement les deux dessins de `packed`, qui existe déjà.

8. **Même scène que le scénario.** Après la tâche 3 du membre 7, `Carrhae(..., headless=False)` appelle ce module et lui passe l’observation de chaque pas. Le membre 6 n’écrit pas la boucle. Il fournit `draw(observation, playback)`. Un test headless du membre 7 ne doit pas importer ce module : le membre 6 ajoute un test qui importe `formaitions.scenario.carrhae` avec un faux et vérifie que sa propre fonction `draw` n’est pas appelée quand `headless=True`. Cet import de test reste dans `tests/test_vue.py`.

Revue qu’il doit faire : les pull requests du membre 5, comme indiqué plus haut.

## Membre 7 — scénario, IA de référence, sauvegarde

Fichiers : `src/formaitions/scenario/carrhae.py`, `placement.py`, `save.py`, et `src/formaitions/ia/braindead.py`, `src/formaitions/ia/bedlam.py` à créer. Tests : `tests/test_placement.py` (déjà commencé), `tests/test_carrhae.py`, `tests/test_save.py`, `tests/test_reference_ai.py`.

Il met les armées sur la carte, il tourne la boucle, il sait qui a gagné, il fournit les deux IA de référence de la section 78. Il n’améliore pas Crassus ni Suréna.

1. **Coins et centre.** Déjà esquissé : `"W"` sud-ouest, `"E"` sud-est, `"NW"` et `"NE"` acceptés, château au centre, x vers l’est, y vers le sud. Il garde ces tests verts. Il n’ajoute pas de nouveau codage des coins.

2. **Placement initial.** `place_armies(...)` met les Romains autour de l’ancre du coin, sans forme régulière (le test refuse un espacement constant de bloc serré sur les 60 légionnaires). Les Parthes sont entre 10 et 20 cases du centre du château, et dans le demi-plan situé entre ce centre et le coin romain. Effectifs égaux aux arguments, pas à 60/20/20/3 en dur. Aucune position sur une falaise ni dans l’emprise 4×4 : il appelle `cliff_tiles` et `castle_footprint` dès qu’ils existent. Avant ça, le test vérifie les distances au centre et le demi-plan, sur une carte sans obstacle. Les armées ne commencent pas en formation : deux lancements du placement peuvent différer.

3. **Issues, sur un état fabriqué, sans boucle.** `outcome(castle_hp, trebuchets_alive, events, elapsed)` : château à 0 → `Outcome.ROMAN` ; tous les trébuchets morts et château encore positif → `Outcome.PARTHIAN` ; des légionnaires tous morts ne changent rien si un trébuchet vit et le château aussi ; 60 s sans événement de dégât → `Outcome.DRAW`. Un dégât à `elapsed = 59` remet le compteur à zéro : le nul n’arrive pas 1 s plus tard. Terminé par ces quatre tests.

4. **BRAINDEAD.** `decide` retourne `[]` pour n’importe quelle observation, y compris une observation pleine. Il journalise `rule="idle"`. Il ne regarde pas les effectifs.

5. **BEDLAM.** Pour chaque unité vivante de son camp : `Attack` sur l’ennemi vivant le plus proche s’il est à portée (les portées sont les nombres du tableau, recopiés ici seulement pour choisir la cible, pas pour appliquer les dégâts), sinon `MoveTo` vers cet ennemi. Pas de forme, pas de préférence pour les trébuchets, pas de repli. Règle `attack_nearest`. Un trébuchet emballé reçoit `Unpack` s’il veut tirer et qu’il n’est pas à portée de marche utile, plutôt qu’un `Attack` illégal. Test sur une observation de trois unités, sans `Carrhae`.

6. **Boucle headless.** `Carrhae(..., headless=True)` répète : fabriquer l’observation, appeler les deux `decide`, appeler `step`, jusqu’à une issue de la tâche 3. Le retour est un `BattleResult` avec issue, durée, unités finales, chronologie des pertes, journal des décisions. `headless=True` n’importe pas `formaitions.vue` et n’ouvre pas de fenêtre. `speed` n’introduit pas de sommeil dans ce mode. BRAINDEAD contre BRAINDEAD termine en nul, et le test borne le nombre de pas (60 s / 0,05 = 1200 pas, plus une petite marge) pour prouver qu’il n’y a pas de boucle infinie. Ce test n’exige pas que `step` sache déjà combattre : si `step` ne produit aucun dégât, le nul à 60 s est justement le résultat attendu.

7. **Sauvegarde.** `save_battle` écrit l’observation (temps, unités, PV, projectiles, château, falaises). `load_battle` relit exactement ça. La bataille rechargée rappelle `decide` : le fichier ne contient pas une liste d’ordres futurs. Terminé quand un aller-retour conserve les positions et les PV, et quand un test relance deux `decide` de BEDLAM après chargement au lieu de rejouer des ordres enregistrés.

8. **Campagne de paramètres.** `run_campaign(n, **variants)` lance `n` appels headless. Le test n’en lance pas 100 : il lance 2, avec un faux général qui enregistre `len(observation.units)` ou le coin lu dans les positions. Un appel avec `n_legionaries=10` et un appel avec `n_legionaries=60` doivent être distinguables dans cet enregistrement. Un appel `"W"` et un appel `"E"` placent les Romains dans deux coins opposés. Il n’affirme pas qu’une graine rejoue la même partie. Le 50/50 du sujet est un objectif expérimental plus tard, quand Crassus et Suréna existent : cette tâche-ci vérifie seulement que les paramètres arrivent jusqu’à la bataille.

Revue qu’il doit faire : les pull requests du membre 2. Il vérifie que le placement peut se caler sur `cliff_tiles` sans recopier l’anneau dans `placement.py`.

## Charge

| Membre | Tâches 1 à 6, sans attendre | Tâches 7 et 8, assemblage | Tests qu’il écrit |
| --- | --- | --- | --- |
| 1 | pas, vitesses, Hold, gel, pack, refus | appeler `blocked`, appeler `resolve_attack_end` | `tests/test_step.py` |
| 2 | carte, falaises, rayons, morts, segment, voisinage | test d’intégration falaise, empreinte exportée | `tests/test_carte.py`, `tests/test_collision.py` |
| 3 | deux formules, mur, portées, fin d’animation, tirs | fonctions pures, puis date du dégât dans `step` | `tests/test_combat.py` |
| 4 | trois familles de formes, réassignation, cohésion, règles de Crassus | poids, puis appel de `translate` | `tests/test_shapes.py`, `tests/test_crassus.py` |
| 5 | Advance, Split, Merge, Screen, trois autres commandes, import propre | cinq règles de Suréna, poids | `tests/test_commands.py`, `tests/test_surena.py` |
| 6 | isométrie, quatre unités, caméra, minicarte, pause, vitesse | champ de mur seulement après revue, `draw` appelé par le scénario | `tests/test_vue.py` |
| 7 | coins, placement, issues, BRAINDEAD, BEDLAM, boucle | sauvegarde, campagne de paramètres | `tests/test_placement.py`, `tests/test_carrhae.py`, `tests/test_save.py`, `tests/test_reference_ai.py` |

Les deux généraux notés par le jury (sections 74 et 75) sont séparés : Crassus au membre 4, Suréna au membre 5. BEDLAM et la campagne restent au membre 7, sinon son paquet se réduirait à de la colle entre les modules des autres. La vue compte la minicarte, la pause et la vitesse, pas seulement le dessin d’une case.

## Qui travaille ensemble

Travailler ensemble veut dire figer une signature et se relire. Cela ne veut pas dire committer dans le même fichier, ni approuver sa propre paire.

| Paire | Ce qu’ils figent ensemble | Ce qu’ils ne font pas |
| --- | --- | --- |
| 1 et 2 | `blocked(unit, position, others, map)` et `segment_blocked` | Le membre 2 n’écrit pas dans `step.py`. Le membre 1 n’écrit pas les rayons. |
| 1 et 3 | « le compteur d’animation tombe à 0 » appelle `resolve_attack_end` une fois | Le membre 3 n’écrit pas le décrément. Le membre 1 n’écrit pas la formule. |
| 2 et 3 | `units_within` pour 0,42 et 0,75 | Le membre 2 ne code pas le +6. Le membre 3 peut tester ses distances sans ce module. |
| 2 et 7 | `cliff_tiles`, `castle_footprint`, demi-plan du placement | Le membre 7 ne redessine pas l’anneau. |
| 4 et 5 | noms déjà gelés, et `slots_for(shape, ids, anchor)` injecté dans `translate` | Ils ne s’approuvent pas. Le membre 5 n’écrit pas `slots`. Le membre 4 n’écrit pas `Split`. |
| 4 et 7 | `decide(observation, now) -> list[Order]`, journal `rule` | Le membre 7 ne code pas une tactique romaine dans `Carrhae`. |
| 5 et 7 | même signature pour Suréna et pour BEDLAM | BEDLAM ne passe pas par `translate`. |
| 6 et 7 | `draw(observation, playback)` ; `headless=True` n’importe pas la vue | La vue ne lance pas `Carrhae`. Le scénario ne dessine pas. |
| 1, 3 et 6 | ajout éventuel de `shield_wall: bool` sur `UnitState` | Deux revues, dont le membre 1, avant de toucher `contracts.py`. |

Les sept commencent le même jour. Aucune tâche 1 à 6 n’attend une autre personne.

Groupes qui peuvent avancer en parallèle toute la première moitié du projet :

- **Simulateur, sans se marcher dessus :** membres 1, 2 et 3, trois dossiers, trois fichiers de tests.
- **Formations :** membres 4 et 5. Ils se parlent le premier jour, puis chacun sur ses fichiers.
- **Autour de la bataille :** membres 6 et 7. La vue sur des instantanés écrits à la main, le scénario sur des états écrits à la main.

Groupes qui ne sont utiles qu’au moment de l’assemblage : 1 avec 2, 1 avec 3, 4 avec 5, 7 avec tout le monde pour la boucle réelle. Avant ça, un point d’une demi-heure suffit à figer la signature.

## Qui dépend de qui pour le code

Une flèche `A → B` signifie : A ne peut pas terminer sa tâche d’assemblage tant que B n’a pas livré la fonction nommée. Les tâches 1 à 6 de A ne sont pas sur ce dessin.

```text
collision.blocked, segment_blocked     (membre 2)
        └──────────────► step            (membre 1, tâche 7)

combat.resolve_attack_end              (membre 3)
        └──────────────► step            (membre 1, tâche 8)

carte.cliff_tiles, castle_footprint    (membre 2)
        └──────────────► place_armies    (membre 7, fin de la tâche 2)

step                                   (membre 1)
        └──────────────► Carrhae         (membre 7, tâche 6)
                         La boucle tourne déjà avec un step qui ne combat pas.
                         L’issue est alors le nul à 60 s.

resolve_attack_end branché dans step   (membres 1 et 3)
        └──────────────► issues réelles  (membre 7, tâches 3 et 6 sur une vraie bataille)

slots                                  (membre 4)
        └──────────────► translate       (membre 5, tâches 1 à 5, en injection :
                                          le membre 5 n’est pas bloqué, il passe un faux)

translate                              (membre 5)
        └──────────────► Crassus         (membre 4, tâche 8 seulement)

decide de Crassus et de Suréna         (membres 4 et 5)
        └──────────────► Campagne utile  (membre 7, lecture des taux.
                                          La tâche 8 du membre 7, elle, ne les attend pas.)

draw                                   (membre 6)
        └──────────────► Carrhae         (membre 7, seulement headless=False)

Observation complète                   (membre 7, boucle)
        └──────────────► vue en direct   (membre 6, tâche 8)
```

Personne ne dépend du membre 6 pour que les tests de simulation, de formation ou d’IA passent.

Crassus et Suréna ne dépendent pas de `Carrhae` pour exister. Leurs tests lisent une `Observation` fabriquée. C’est voulu : sinon les membres 4 et 5 attendraient toute la chaîne.

## Qui dépend de qui pour les tests

Tests qui passent sur une machine où le reste du groupe n’a encore rien livré :

| Test | Membre | Données |
| --- | --- | --- |
| `tests/test_step.py` tâches 1 à 6 | 1 | monde minuscule écrit dans le test |
| `tests/test_carte.py`, `tests/test_collision.py` tâches 1 à 6 | 2 | positions écrites dans le test |
| `tests/test_combat.py` tâches 1 à 7 | 3 | unités fictives, PV et armures du tableau |
| `tests/test_shapes.py` | 4 | listes d’identifiants, pas de monde |
| `tests/test_crassus.py` tâches 6 et 7 | 4 | `Observation` écrite dans le test |
| `tests/test_commands.py` | 5 | `slots_for` faux |
| `tests/test_surena.py` | 5 | `Observation` écrite dans le test |
| `tests/test_vue.py` tâches 1 à 7 | 6 | `Observation` écrite dans le test, driver dummy |
| `tests/test_reference_ai.py` | 7 | BRAINDEAD et BEDLAM sur un instantané |
| `tests/test_placement.py` | 7 | distances et coins, sans falaise tant que le membre 2 n’est pas là |
| `tests/test_carrhae.py` nul BRAINDEAD | 7 | attend `step` du membre 1, même si `step` ne combat pas encore |
| `tests/test_save.py` | 7 | une `Observation`, pas une bataille jouée |

Tests qui échouent tant qu’une autre personne n’a pas mergé, et qui ne doivent pas être exigés avant :

| Test | Écrit par | Attend le merge de |
| --- | --- | --- |
| `MoveTo` vers une falaise s’arrête | 2 | membre 1, tâche 7 |
| les PV baissent au pas où l’animation tombe à 0 | 3 | membre 1, tâche 8 |
| Crassus appelle `translate` et ne recolle pas les slots à la main | 4 | membre 5, tâches 1 à 5 |
| le placement ne pose personne sur l’anneau | 7 | membre 2, tâches 1, 2 et 8 |
| BRAINDEAD contre BEDLAM produit un vainqueur, pas un nul | 7 | membres 1, 2 et 3 assemblés |
| la fenêtre suit une vraie `Carrhae` | 6 | membre 7, tâche 6, avec `headless=False` |
| deux poids de Crassus changent le taux de victoires | 4, lancé par 7 | toute la chaîne, plus Suréna |
| deux poids de Suréna changent le taux de victoires | 5, lancé par 7 | toute la chaîne, plus Crassus |

Le dernier couple de tests est celui de la section 69 : les chances bougent quand les paramètres bougent. Il arrive en dernier. Il n’est le travail d’aucun membre seul. Le membre 7 tient le script, les membres 4 et 5 tiennent les poids.

## Ordre d’assemblage

Dès que le morceau précédent existe. Le travail des tâches 1 à 6 n’attend pas cet ordre.

1. Le membre 1 fournit `step` qui marche sur une plaine vide.
2. Le membre 2 fournit `blocked`. Le membre 1 l’appelle.
3. Le membre 7 appelle cette boucle depuis `Carrhae` en headless, départ `"W"`.
4. Le membre 6 affiche un instantané, avec pause et minicarte. Il branche `draw` ensuite.
5. Le membre 3 fournit `resolve_attack_end`. Le membre 1 l’appelle à la fin de l’animation.
6. Les membres 4 et 5 font exécuter `Advance` par `step`. Le membre 4 réassigne les slots après une mort, le membre 5 traduit.
7. Le membre 7 ajoute BEDLAM sur cette bataille réelle, puis la sauvegarde.
8. Les membres 4 et 5 branchent Crassus et Suréna. La campagne du membre 7 compare alors les poids.

## Ce que le jury regarde, et qui le porte

La section 77 n’est pas un barème. Elle dit ce qui doit être visible le 15 décembre.

| Critère | Membre qui le rend vrai | Les autres |
| --- | --- | --- |
| La formation tient en marchant | 5 traduit `Advance`, 1 exécute les `MoveTo`, 2 empêche le chevauchement | 4 fournit les slots |
| Elle se reforme après les morts | 4, `reassign` | 5 traduit, 1 exécute |
| Elle bouche le chemin des trébuchets | 4, `screen_cataphracts` | 2 pour le blocage physique |
| Serré sous les flèches, lâche sous le piétinement | 4 pour la décision, 3 pour le calcul du bonus et du piétinement | 5 pour `Spread` et `Transition` |
| Les Romains protègent les trébuchets | 4 | 7 ne le code pas dans la boucle |
| Les Parthes visent les trébuchets et les trous | 5 | 7, BEDLAM ne le fait exprès pas, pour servir de contraste |
| Ça tient quand les effectifs et le coin changent | 7 pour les paramètres, 4 et 5 pour des IA qui lisent l’observation | personne ne fige 60 et 20 dans une IA |
| On comprend la décision à l’écran | 6 | 3 et 1 si le booléen de mur entre dans l’instantané |

Les sections 80 à 83 (secrétaire, rapport `2 python report.pdf`, deux diapositives, démonstration de 10 minutes, sauvegarde pour répéter) ne sont pas des tâches de code de ce découpage. Chacun écrira le paragraphe de ses huit tâches. Le fichier de sauvegarde du membre 7 sert à enchaîner les scènes le jour de la soutenance sans temps mort.
