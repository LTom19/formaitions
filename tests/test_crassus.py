"""Crassus, sur une observation fabriquée. Membre 4.

Ajoute ici un test par règle. N'appelle pas `Carrhae`.
"""

from __future__ import annotations

import inspect

import pytest

from formaitions.ia.crassus import Crassus

pytestmark = pytest.mark.membre4


def test_crassus_exposes_a_weight_and_decide() -> None:
    general = Crassus(aggressiveness=50)
    assert general.aggressiveness == 50
    assert list(inspect.signature(general.decide).parameters) == [
        "observation",
        "now",
    ]
