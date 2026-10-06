"""Pause et vitesse partagées entre la vue et le scénario. Membre 6.

Le dessin n'est pas ici. `speed` ne change pas `FIXED_DT` : le scénario lit
cette valeur pour dormir plus ou moins longtemps entre deux pas, en mode fenêtré.
Lancer : pytest -m membre6
"""

from __future__ import annotations

from dataclasses import dataclass

from formaitions.domaine.contracts import Vec2

MEMBER = 6

ALLOWED_SPEEDS = (0.5, 1.0, 2.0, 4.0)


@dataclass
class Playback:
    """État d'affichage. Ce n'est pas un ordre, et ce n'est pas le monde."""

    paused: bool = False
    speed: float = 1.0
    camera: Vec2 = Vec2(60.0, 60.0)


def set_paused(playback: Playback, paused: bool) -> None:
    """La touche de pause appelle cette fonction. Elle ne crée pas d'ordre."""

    playback.paused = paused


def set_speed(playback: Playback, speed: float) -> None:
    """0,5, 1, 2 ou 4. Toute autre valeur est refusée. Ne touche pas à `FIXED_DT`."""

    if speed not in ALLOWED_SPEEDS:
        allowed = ", ".join(str(value) for value in ALLOWED_SPEEDS)
        raise ValueError(f"vitesse {speed} refusée. Valeurs : {allowed}.")
    playback.speed = speed
