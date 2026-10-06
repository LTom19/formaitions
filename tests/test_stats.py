"""Nombres du sujet, une seule fois, dans le contrat partagé."""

from formaitions.domaine.contracts import UnitKind
from formaitions.domaine.stats import (
    BUILDING_ARMOUR,
    CASTLE_HP,
    CASTLE_VOLLEY,
    DRAW_AFTER_SECONDS_WITHOUT_DAMAGE,
    MISSED_SHOT_DAMAGE,
    SHIELD_WALL_DISTANCE,
    SHIELD_WALL_MIN_NEIGHBOURS,
    TRAMPLE_CENTRE_DISTANCE,
    unit_stats,
)


def test_legionary_speed_and_radius_match_the_subject() -> None:
    stats = unit_stats(UnitKind.LEGIONARY)
    assert stats.speed == 1.06
    assert stats.radius == 0.20
    assert stats.animation == 1.26
    assert stats.pierce_armour == 6


def test_shared_thresholds_match_the_subject() -> None:
    assert SHIELD_WALL_MIN_NEIGHBOURS == 4
    assert SHIELD_WALL_DISTANCE == 0.42
    assert TRAMPLE_CENTRE_DISTANCE == 0.75
    assert CASTLE_HP == 10000
    assert CASTLE_VOLLEY == 5
    assert DRAW_AFTER_SECONDS_WITHOUT_DAMAGE == 60
    assert BUILDING_ARMOUR == 0
    assert MISSED_SHOT_DAMAGE == 0


def test_trebuchet_range_and_pack_time() -> None:
    stats = unit_stats(UnitKind.TREBUCHET)
    assert stats.range_min == 4
    assert stats.range_max == 16
    assert stats.pack_time == 11
    assert stats.accuracy_vs_buildings == 0.80
    assert stats.accuracy_vs_units == 0.15
    assert stats.bonus_vs_buildings == 250
