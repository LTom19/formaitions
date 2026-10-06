"""Déplacement continu. Membre 1.

Tâches 2 à 5 dans docs/repartition-taches.md.
Les vitesses et les durées sont dans `formaitions.domaine.stats`, pas ici.
Ce module n'écrit pas dans le monde : il calcule une position ou un booléen.
Lancer : pytest -m membre1
"""

from __future__ import annotations

from formaitions.domaine.contracts import Vec2

MEMBER = 1


def integrate_move(
    position: Vec2,
    destination: Vec2,
    speed: float,
    dt: float,
) -> Vec2:
    """Avance en ligne droite d'au plus `speed * dt`, sans dépasser la destination."""

    del position, destination, speed, dt
    raise NotImplementedError(
        "Membre 1, tâche 2 : déplacement continu. docs/repartition-taches.md."
    )


def animation_blocks_movement(attack_animation_remaining: float) -> bool:
    """Vrai tant que l'animation d'attaque n'est pas finie. Le rechargement seul ne bloque pas."""

    del attack_animation_remaining
    raise NotImplementedError(
        "Membre 1, tâche 4 : gel pendant l'animation. docs/repartition-taches.md."
    )
