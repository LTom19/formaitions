# FormAItions — groupe 2

Sept personnes, FISA. Rapport visé le 8 décembre 2026, soutenance le 15 décembre 2026. Le périmètre est Carrhes, parties VI et VII du cours.

Les fonctions sont déclarées. Le corps de chacune lève encore `NotImplementedError`, avec le numéro de ta tâche. Tu ouvres tes fichiers, tu lis le message, tu écris le corps. Tu ne renommes rien.

## Lancer

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest
```

Si la création de l'environnement échoue parce que `ensurepip` est absent, installer le paquet `python3-venv`, ou bien :

```bash
python3 -m venv --without-pip .venv
curl -fsSL https://bootstrap.pypa.io/get-pip.py | .venv/bin/python
.venv/bin/pip install -e ".[dev]"
```

Ton poste seulement :

```bash
pytest -m membre1
pytest -m membre2
pytest -m membre3
pytest -m membre4
pytest -m membre5
pytest -m membre6
pytest -m membre7
```

## Où lire

- [docs/dossiers.md](docs/dossiers.md) — quel dossier, quel fichier, quelle commande.
- [docs/repartition-taches.md](docs/repartition-taches.md) — les huit tâches de chacun, les tests, qui travaille avec qui, qui attend qui.
- [docs/decisions/001-contrats.md](docs/decisions/001-contrats.md) — ce qui est déjà gelé : pas de 0,05 s, ordres, qui a le droit d'importer qui.

## Les sept postes

| Membre | Dossier | Commande |
| --- | --- | --- |
| 1 | `src/formaitions/simulation/step.py`, `mouvement.py`, `monde.py` | `pytest -m membre1` |
| 2 | `src/formaitions/simulation/carte.py`, `collision.py` | `pytest -m membre2` |
| 3 | `src/formaitions/simulation/combat.py` | `pytest -m membre3` |
| 4 | `src/formaitions/formations/shapes.py`, `model.py`, `src/formaitions/ia/crassus.py` | `pytest -m membre4` |
| 5 | `src/formaitions/formations/commands.py`, `src/formaitions/ia/surena.py` | `pytest -m membre5` |
| 6 | `src/formaitions/vue/` | `pytest -m membre6` |
| 7 | `src/formaitions/scenario/`, `src/formaitions/ia/braindead.py`, `bedlam.py` | `pytest -m membre7` |

`src/formaitions/domaine/` n'appartient à personne. On n'y met pas une règle de combat. Les nombres du sujet sont dans `domaine/stats.py` : importe-les, ne les recopie pas.

## Essai isométrique

```bash
SDL_VIDEODRIVER=dummy python -m formaitions.vue.spike
```

L'image est écrite dans `artifacts/spike_isometric.png`. Sans la variable `SDL_VIDEODRIVER`, la même commande tente d'ouvrir une fenêtre.

## Avant le premier commit

Chacun travaille sur ses fichiers et les teste avec des données écrites à la main. On n'invente pas un autre type d'ordre que `MoveTo`, `Hold`, `Attack`, `Pack`, `Unpack`. La vue ne calcule pas les dégâts. Une IA lit une `Observation` et renvoie des ordres : elle ne modifie pas le monde.

Les membres 4 et 5 ne s'approuvent pas entre eux. Une modification de `Observation`, `Order` ou `step` demande deux revues, dont celle du membre 1.

Chaque commit porte le nom complet `NOM Prénom` de son auteur. Branche courte, pull request, au moins une revue extérieure à l'auteur.

L'ordre d'assemblage, les paires, et les tests qui attendent quelqu'un d'autre sont dans le document des tâches. Tes six premières tâches n'attendent personne.
