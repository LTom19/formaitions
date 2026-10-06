"""Vue. Membre 6.

`Playback` est déjà écrit. Ajoute ici les tests d'image, avec le driver dummy.
Ils ne calculent pas de dégâts.
"""

from __future__ import annotations

import inspect

import pytest

from formaitions.domaine.contracts import FIXED_DT
from formaitions.vue.bataille import draw, pan_to_minimap
from formaitions.vue.playback import ALLOWED_SPEEDS, Playback, set_paused, set_speed

pytestmark = pytest.mark.membre6


def test_speed_changes_playback_and_not_the_timestep() -> None:
    playback = Playback()
    set_speed(playback, 4)
    set_paused(playback, True)
    assert playback.speed == 4
    assert playback.paused is True
    assert FIXED_DT == 0.05
    with pytest.raises(ValueError):
        set_speed(playback, 3)
    assert set(ALLOWED_SPEEDS) == {0.5, 1.0, 2.0, 4.0}


def test_draw_and_minimap_keep_their_names() -> None:
    assert list(inspect.signature(draw).parameters) == ["observation", "playback"]
    assert list(inspect.signature(pan_to_minimap).parameters) == ["playback", "x", "y"]
