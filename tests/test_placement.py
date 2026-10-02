"""Coins de départ et centre du château."""

import pytest

from formaitions.scenario.placement import (
    StartCorner,
    castle_center,
    corner_anchor,
    parse_start_position,
)


def test_west_means_southwest() -> None:
    assert parse_start_position("W") is StartCorner.SOUTHWEST
    assert parse_start_position("sw") is StartCorner.SOUTHWEST


def test_east_means_southeast() -> None:
    assert parse_start_position("E") is StartCorner.SOUTHEAST


def test_unknown_corner_is_rejected() -> None:
    with pytest.raises(ValueError, match="inconnu"):
        parse_start_position("north")


def test_castle_stays_at_the_center() -> None:
    assert castle_center((120, 120)) == castle_center((120, 120))
    center = castle_center((120, 80))
    assert center.x == 60
    assert center.y == 40


def test_southwest_anchor_is_in_the_southwest_corner() -> None:
    anchor = corner_anchor(StartCorner.SOUTHWEST, (120, 120))
    assert anchor.x < 60
    assert anchor.y > 60


def test_east_anchor_is_not_the_west_anchor() -> None:
    west = corner_anchor(parse_start_position("W"), (120, 120))
    east = corner_anchor(parse_start_position("E"), (120, 120))
    assert east.x > west.x
    assert east.y == west.y
