"""Suréna, sur une observation fabriquée. Membre 5.

Ajoute ici un test par règle. N'appelle pas `Carrhae`.
"""

from __future__ import annotations

import inspect

import pytest

from formaitions.ia.surena import Surena

pytestmark = pytest.mark.membre5


def test_surena_exposes_a_weight_and_decide() -> None:
    general = Surena(boldness=50)
    assert general.boldness == 50
    assert list(inspect.signature(general.decide).parameters) == [
        "observation",
        "now",
    ]
