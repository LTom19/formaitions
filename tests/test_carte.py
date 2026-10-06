"""Carte, château, falaises. Membre 2.

Ajoute ici les tests de comportement, avec des positions écrites à la main.
Ils n'importent pas `step`.
"""

from __future__ import annotations

import inspect

import pytest

from formaitions.simulation.carte import (
    Map,
    blocks_ground,
    blocks_shot,
    build_map,
    castle_footprint,
    cliff_tiles,
)

pytestmark = pytest.mark.membre2


def test_map_can_be_built_by_hand_before_build_map_exists() -> None:
    game_map = Map(size=(120, 120), footprint=((60, 60),), cliffs=((59, 60),))
    assert game_map.size == (120, 120)


def test_member_two_map_functions_keep_their_names() -> None:
    assert "map_size" in inspect.signature(build_map).parameters
    assert list(inspect.signature(blocks_ground).parameters) == ["game_map", "position"]
    assert list(inspect.signature(blocks_shot).parameters) == ["game_map", "position"]
    assert "game_map" in inspect.signature(castle_footprint).parameters
    assert "game_map" in inspect.signature(cliff_tiles).parameters
