"""Scénario jouable depuis un appel de fonction, sans menu."""

from formaitions.scenario.carrhae import Carrhae
from formaitions.scenario.placement import StartCorner, castle_center, parse_start_position
from formaitions.scenario.save import load_battle, save_battle

__all__ = [
    "Carrhae",
    "StartCorner",
    "castle_center",
    "load_battle",
    "parse_start_position",
    "save_battle",
]
