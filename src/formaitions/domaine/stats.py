"""Nombres du sujet. Contrat partagé : aucune règle, aucun propriétaire de module.

Les formules restent dans `simulation/combat.py`. Ce fichier ne fait que nommer
les valeurs pour que les sept membres n'en recopient pas sept versions.
Les deux dernières constantes sont les hypothèses jaunes de la décision 001.
"""

from __future__ import annotations

from dataclasses import dataclass

from formaitions.domaine.contracts import UnitKind

SHIELD_WALL_MIN_NEIGHBOURS = 4
SHIELD_WALL_DISTANCE = 0.42
SHIELD_WALL_PIERCE_BONUS = 6.0
TRAMPLE_CENTRE_DISTANCE = 0.75

CASTLE_HP = 10000.0
CASTLE_PIERCE_ARMOUR = 13.0
CASTLE_RANGE = 11.0
CASTLE_PIERCE_ATTACK = 15.0
CASTLE_VOLLEY = 5
CASTLE_RELOAD = 2.0
CASTLE_FOOTPRINT = 4
CLIFF_RING = 1

PARTHIAN_SPAWN_MIN = 10.0
PARTHIAN_SPAWN_MAX = 20.0
DRAW_AFTER_SECONDS_WITHOUT_DAMAGE = 60.0

# Hypothèses jaunes, décision 001. Un seul endroit à changer si le professeur tranche.
BUILDING_ARMOUR = 0.0
MISSED_SHOT_DAMAGE = 0.0


@dataclass(frozen=True)
class UnitStats:
    hp: float
    melee_attack: float
    pierce_attack: float
    melee_armour: float
    pierce_armour: float
    range_min: float
    range_max: float
    speed: float
    reload: float
    animation: float
    radius: float
    bonus_vs_buildings: float = 0.0
    accuracy_vs_buildings: float | None = None
    accuracy_vs_units: float | None = None
    pack_time: float | None = None


_STATS: dict[UnitKind, UnitStats] = {
    UnitKind.LEGIONARY: UnitStats(
        hp=75,
        melee_attack=16,
        pierce_attack=0,
        melee_armour=6,
        pierce_armour=6,
        range_min=0,
        range_max=0,
        speed=1.06,
        reload=2.0,
        animation=1.26,
        radius=0.20,
    ),
    UnitKind.ELITE_CATAPHRACT: UnitStats(
        hp=150,
        melee_attack=14,
        pierce_attack=0,
        melee_armour=5,
        pierce_armour=5,
        range_min=0,
        range_max=0,
        speed=1.35,
        reload=1.7,
        animation=1.36,
        radius=0.25,
    ),
    UnitKind.HEAVY_CAVALRY_ARCHER: UnitStats(
        hp=80,
        melee_attack=0,
        pierce_attack=12,
        melee_armour=5,
        pierce_armour=6,
        range_min=0,
        range_max=8,
        speed=1.44,
        reload=1.8,
        animation=1.17,
        radius=0.25,
    ),
    UnitKind.TREBUCHET: UnitStats(
        hp=150,
        melee_attack=0,
        pierce_attack=200,
        melee_armour=2,
        pierce_armour=8,
        range_min=4,
        range_max=16,
        speed=0.80,
        reload=10.0,
        animation=1.0,
        radius=0.50,
        bonus_vs_buildings=250,
        accuracy_vs_buildings=0.80,
        accuracy_vs_units=0.15,
        pack_time=11.0,
    ),
}


def unit_stats(kind: UnitKind) -> UnitStats:
    """Retourne la ligne du sujet pour cette unité. Ne calcule aucun dégât."""

    return _STATS[kind]
