"""Vue 2.5D d'une observation. Membre 6.

Tâches 1 à 5, 7 et 8 dans docs/repartition-taches.md.
La pause et la vitesse sont déjà dans `playback.py`. Ce module dessine.
Il n'est pas importé par `formaitions.vue` : l'import du package ne charge pas Pygame.
Lancer : pytest -m membre6
"""

from __future__ import annotations

from formaitions.domaine.contracts import Observation
from formaitions.vue.playback import Playback

MEMBER = 6


def draw(observation: Observation, playback: Playback) -> None:
    """Dessine l'instantané. Ne modifie ni l'observation, ni les points de vie, ni les positions."""

    del observation, playback
    raise NotImplementedError(
        "Membre 6, tâche 1 : vue isométrique. docs/repartition-taches.md."
    )


def pan_to_minimap(playback: Playback, x: float, y: float) -> None:
    """Recentre `playback.camera` sur le point de carte visé dans la minicarte."""

    del playback, x, y
    raise NotImplementedError(
        "Membre 6, tâche 4 : minicarte. docs/repartition-taches.md."
    )
