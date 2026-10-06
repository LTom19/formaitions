"""Collisions et voisinage. Membre 2.

Ajoute ici les tests de comportement. Ils n'appellent pas `step`.
"""

from __future__ import annotations

import inspect

import pytest

from formaitions.simulation.collision import (
    blocked,
    overlaps,
    radius,
    segment_blocked,
    units_within,
)

pytestmark = pytest.mark.membre2


def test_member_two_collision_functions_keep_their_names() -> None:
    assert "kind" in inspect.signature(radius).parameters
    assert list(inspect.signature(overlaps).parameters) == ["left", "right"]
    assert list(inspect.signature(blocked).parameters) == [
        "unit",
        "position",
        "others",
        "game_map",
    ]
    assert list(inspect.signature(segment_blocked).parameters) == [
        "start",
        "end",
        "unit",
        "others",
        "game_map",
    ]
    assert list(inspect.signature(units_within).parameters) == [
        "units",
        "origin",
        "reach",
    ]
