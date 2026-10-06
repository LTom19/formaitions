"""Boucle, placement, campagne. Membre 7.

Les coins sont déjà testés dans `test_placement.py`.
Ajoute ici les tests d'issue et de paramètres.
"""

from __future__ import annotations

import inspect

import pytest

from formaitions.scenario.campagne import run_campaign
from formaitions.scenario.placement import place_armies
from formaitions.scenario.victoire import outcome

pytestmark = pytest.mark.membre7


def test_member_seven_scenario_functions_keep_their_names() -> None:
    placed = inspect.signature(place_armies).parameters
    assert "roman_start_position" in placed
    assert "n_legionaries" in placed
    verdict = inspect.signature(outcome).parameters
    assert list(verdict) == ["castle_hp", "trebuchets_alive", "events", "elapsed"]
    assert "n" in inspect.signature(run_campaign).parameters
