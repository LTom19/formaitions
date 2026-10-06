"""Règles de combat. Membre 3.

Ajoute ici les tests sur des unités fictives. Ils n'appellent pas `step`
tant que la tâche 8 n'est pas branchée par le membre 1.
"""

from __future__ import annotations

import inspect

import pytest

from formaitions.simulation.combat import (
    can_start_attack,
    damage_simple,
    damage_typed,
    resolve_attack_end,
    resolve_castle_volley,
    shield_wall,
)

pytestmark = pytest.mark.membre3


def test_member_three_functions_keep_their_names() -> None:
    assert list(inspect.signature(damage_simple).parameters) == ["attack", "armour"]
    assert "pairs" in inspect.signature(damage_typed).parameters
    assert list(inspect.signature(shield_wall).parameters) == ["legionary", "units"]
    attack = inspect.signature(can_start_attack).parameters
    assert list(attack) == ["attacker", "target", "game_map", "order"]
    resolution = inspect.signature(resolve_attack_end).parameters
    assert "attacker" in resolution
    assert "animation_just_finished" in resolution
    assert "roll" in resolution
    volley = inspect.signature(resolve_castle_volley).parameters
    assert list(volley) == ["units", "castle_position", "next_projectile_id"]
