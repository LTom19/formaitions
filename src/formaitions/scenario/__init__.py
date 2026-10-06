"""Scénario jouable depuis un appel de fonction, sans menu."""

from formaitions.scenario.campagne import run_campaign
from formaitions.scenario.carrhae import Carrhae
from formaitions.scenario.placement import (
    StartCorner,
    castle_center,
    parse_start_position,
    place_armies,
)
from formaitions.scenario.save import load_battle, save_battle
from formaitions.scenario.victoire import outcome

__all__ = [
    "Carrhae",
    "StartCorner",
    "castle_center",
    "load_battle",
    "outcome",
    "parse_start_position",
    "place_armies",
    "run_campaign",
    "save_battle",
]
