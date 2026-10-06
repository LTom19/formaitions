# Dossiers — qui écrit où

Groupe 2. Les paquets restent ceux de la décision 001 : on ne range pas le code par numéro de membre, parce que `simulation` n'a pas le droit d'importer `ia`, et `formations` n'a pas le droit d'importer `simulation`. À l'intérieur d'un paquet partagé, chaque fichier a un seul auteur.

Ouvre ton fichier. La constante `MEMBER` en haut confirme que c'est le tien. Tu remplis les fonctions qui lèvent `NotImplementedError`. Tu ne renommes pas ces fonctions. Le détail chiffré de chaque tâche est dans [repartition-taches.md](repartition-taches.md).

```bash
pytest -m membre1
pytest -m membre2
pytest -m membre3
pytest -m membre4
pytest -m membre5
pytest -m membre6
pytest -m membre7
pytest
```

La dernière commande lance toute la suite. Elle doit rester verte sur `main`.

## Dossiers entiers

| Dossier | Membre | Rôle |
| --- | --- | --- |
| `src/formaitions/vue/` | 6 | Affichage. L'import du paquet ne charge pas Pygame. |
| `src/formaitions/scenario/` | 7 | Carrhes, placement, victoire, sauvegarde, campagne. |
| `src/formaitions/domaine/` | personne | Contrats et nombres du sujet. Deux revues pour le changer, dont le membre 1. |
| `docs/decisions/` | personne | Décisions déjà prises. On n'en réécrit pas l'historique. |

## Dossiers partagés, fichier par fichier

### `src/formaitions/simulation/`

| Fichier | Membre | Ce qu'il contient déjà |
| --- | --- | --- |
| `step.py` | 1 | `step`. Refuse un pas différent de 0,05. Le corps de la bataille lève encore une erreur. |
| `mouvement.py` | 1 | `integrate_move`, `animation_blocks_movement`. |
| `monde.py` | 1 | `World`, le contenant. `observe` est à écrire. |
| `carte.py` | 2 | `Map`, que les tests peuvent remplir à la main. `build_map`, `blocks_ground`, `blocks_shot`, `castle_footprint`, `cliff_tiles`. |
| `collision.py` | 2 | `radius`, `overlaps`, `blocked`, `segment_blocked`, `units_within`. |
| `combat.py` | 3 | `damage_simple`, `damage_typed`, `shield_wall`, `can_start_attack`, `resolve_attack_end`, `resolve_castle_volley`, et le type `AttackResolution`. |

`__init__.py` ne fait qu'exposer `step`. Chacun importe son module : `from formaitions.simulation.carte import build_map`.

### `src/formaitions/formations/`

| Fichier | Membre | Ce qu'il contient déjà |
| --- | --- | --- |
| `shapes.py` | 4 | L'énumération `Shape`, et `slots`. |
| `model.py` | 4 | `Formation`, `reassign`, `cohesion_error`. |
| `commands.py` | 5 | Les sept commandes, le type `Translation`, et `translate`. |

Les membres 4 et 5 ne s'approuvent pas l'un l'autre.

### `src/formaitions/ia/`

| Fichier | Membre | Ce qu'il contient déjà |
| --- | --- | --- |
| `crassus.py` | 4 | `Crassus(aggressiveness=50)`. `decide` est à écrire. |
| `surena.py` | 5 | `Surena(boldness=50)`. `decide` est à écrire. |
| `braindead.py` | 7 | `Braindead`. `decide` est à écrire. |
| `bedlam.py` | 7 | `Bedlam(team_name)`. `decide` est à écrire. |

## Tests

| Fichier | Membre |
| --- | --- |
| `tests/test_step.py` | 1 |
| `tests/test_carte.py`, `tests/test_collision.py` | 2 |
| `tests/test_combat.py` | 3 |
| `tests/test_shapes.py`, `tests/test_crassus.py` | 4 |
| `tests/test_commands.py`, `tests/test_surena.py` | 5 |
| `tests/test_vue.py`, `tests/test_spike.py`, `tests/test_vue_import.py` | 6 |
| `tests/test_placement.py`, `tests/test_carrhae.py`, `tests/test_save.py`, `tests/test_reference_ai.py` | 7 |
| `tests/test_contracts.py`, `tests/test_stats.py`, `tests/test_architecture.py` | tout le groupe |

Tu ajoutes tes tests de comportement dans ton fichier. Tu n'effaces pas le test qui vérifie le nom des paramètres : c'est le contrat avec les autres.

## Déjà écrit, à ne pas refaire

- `domaine/contracts.py` : `Observation`, `Order`, `Event`, `Decision`, `BattleResult`, `FIXED_DT`.
- `domaine/stats.py` : PV, attaques, armures, portées, vitesses, rayons, 0,42, 0,75, 60 s, et les deux hypothèses jaunes.
- `scenario/placement.py` : `"W"` sud-ouest, `"E"` sud-est, château au centre. Pas le placement des unités.
- `vue/playback.py` : pause et vitesses 0,5, 1, 2, 4. Pas le dessin.
- `vue/spike.py` : l'essai d'une case. La bataille se dessine dans `bataille.py`.
