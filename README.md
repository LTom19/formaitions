# FormAItions — sprint 0

Groupe 2, FISA, sept personnes. Soutenance le 15 décembre 2026. Le professeur n’a pas annoncé de suite : le périmètre est Carrhes, parties VI et VII du cours.

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

Chaque commit doit porter le nom complet `NOM Prénom` de son auteur. Voir la décision 001.
