"""Affichage. Importer ce package n'ouvre pas de fenêtre et ne charge pas Pygame.

`Playback` est le contrat entre le membre 6 et le membre 7.
Le dessin est dans `bataille.py`, importé seulement par la fenêtre.
"""

from formaitions.vue.playback import Playback, set_paused, set_speed

__all__ = ["Playback", "set_paused", "set_speed"]
