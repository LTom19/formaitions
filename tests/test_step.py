"""Le pas, le déplacement, le monde. Membre 1.

Ajoute ici les tests de comportement. Ne retire pas celui qui vérifie le pas de 0,05 s.
"""

from __future__ import annotations

import inspect

import pytest

from formaitions.domaine.contracts import FIXED_DT
from formaitions.simulation.monde import World, observe
from formaitions.simulation.mouvement import animation_blocks_movement, integrate_move
from formaitions.simulation.step import step

pytestmark = pytest.mark.membre1


def test_step_rejects_a_timestep_other_than_the_frozen_one() -> None:
    world = World(now=0.0, map_size=(120, 120))
    with pytest.raises(ValueError, match="0.05"):
        step(world, [], 1.0)
    assert FIXED_DT == 0.05


def test_member_one_entry_points_keep_their_names() -> None:
    assert list(inspect.signature(integrate_move).parameters) == [
        "position",
        "destination",
        "speed",
        "dt",
    ]
    assert "attack_animation_remaining" in inspect.signature(
        animation_blocks_movement
    ).parameters
    assert "world" in inspect.signature(observe).parameters
    assert list(inspect.signature(step).parameters)[:2] == ["world", "orders"]
