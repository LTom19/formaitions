# 002 — Essai Pygame

Date : 2 octobre 2026.

## Décision

Pygame est retenu pour la vue. L’essai du sprint 0 a réussi : une case isométrique 2:1 et une silhouette, sans règle de jeu et sans fenêtre ouverte par l’import du package.

Version constatée ici : Pygame 2.6.1, SDL 2.28.4, Python 3.13.5. Le dessin a été produit avec `SDL_VIDEODRIVER=dummy`, donc cet essai ne prouve pas le branchement à un écran physique. La commande ouvre une fenêtre seulement si cette variable n’est pas `dummy`.

## Ce qui a été vérifié

- `pytest` : 12 tests passent, dont le dessin d’une case verte et d’une silhouette rouge sans `display.set_mode`.
- `import formaitions.vue` ne charge pas Pygame.
- `SDL_VIDEODRIVER=dummy python -m formaitions.vue.spike` écrit `artifacts/spike_isometric.png`.

## Ce qui n’est pas commencé

La vue de bataille, la caméra, la pause, la vitesse, la minicarte et les sprites d’Age of Empires II. La silhouette est un placeholder. La source des vrais sprites reste à confirmer avec l’enseignant.

## Conséquence

Le package `formaitions.vue` reste vide de règles. Seul `formaitions.vue.spike` importe Pygame tant que la vue complète n’est pas ouverte.
