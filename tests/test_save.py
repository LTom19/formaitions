"""La sauvegarde est prévue, pas encore écrite."""

import pytest

from formaitions.domaine.contracts import Observation, Vec2
from formaitions.scenario.save import load_battle, save_battle

pytestmark = pytest.mark.membre7


def _snapshot() -> Observation:
    return Observation(
        now=0.0,
        map_size=(120, 120),
        units=(),
        projectiles=(),
        castle_hp=10000,
        castle_position=Vec2(60, 60),
        cliff_tiles=(),
    )


def test_save_and_load_are_not_written_yet() -> None:
    with pytest.raises(NotImplementedError):
        save_battle(_snapshot(), "bataille.json")
    with pytest.raises(NotImplementedError):
        load_battle("bataille.json")
