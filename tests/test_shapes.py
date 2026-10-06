"""Slots des formes. Membre 4.

Ajoute ici les tests de distances. Ils ne créent pas de monde.
"""

from __future__ import annotations

import inspect

import pytest

from formaitions.formations.model import cohesion_error, reassign
from formaitions.formations.shapes import Shape, slots

pytestmark = pytest.mark.membre4


def test_four_shapes_exist() -> None:
    assert {shape.value for shape in Shape} == {
        "circle",
        "line",
        "block_dense",
        "block_loose",
    }


def test_member_four_shape_functions_keep_their_names() -> None:
    assert list(inspect.signature(slots).parameters) == ["shape", "ids", "anchor"]
    assert list(inspect.signature(reassign).parameters) == ["formation", "living_ids"]
    assert list(inspect.signature(cohesion_error).parameters) == [
        "positions",
        "assigned",
    ]
