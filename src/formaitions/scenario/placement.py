"""Coins de départ, centre du château, placement des armées. Membre 7.

Tâches 1 et 2 dans docs/repartition-taches.md.
Les coins sont écrits. `place_armies` reste à faire.
Lancer : pytest -m membre7
"""

from __future__ import annotations

from enum import Enum

from formaitions.domaine.contracts import UnitState, Vec2

MEMBER = 7

CORNER_MARGIN = 8.0


class StartCorner(Enum):
    """`"W"` du sujet est le sud-ouest, pas tout le bord ouest."""

    SOUTHWEST = "SW"
    SOUTHEAST = "SE"
    NORTHWEST = "NW"
    NORTHEAST = "NE"


_ALIASES = {
    "W": StartCorner.SOUTHWEST,
    "SW": StartCorner.SOUTHWEST,
    "E": StartCorner.SOUTHEAST,
    "SE": StartCorner.SOUTHEAST,
    "NW": StartCorner.NORTHWEST,
    "NE": StartCorner.NORTHEAST,
}


def parse_start_position(value: str) -> StartCorner:
    """Traduit le paramètre de `Carrhae`. `"E"` est le sud-est, symétrique du sud-ouest."""

    try:
        return _ALIASES[value.upper()]
    except KeyError as error:
        known = ", ".join(sorted(_ALIASES))
        raise ValueError(f"coin de départ inconnu : {value!r}. Valeurs : {known}.") from error


def castle_center(map_size: tuple[int, int]) -> Vec2:
    """Le château reste au centre, quelle que soit la taille de carte acceptée."""

    width, height = map_size
    return Vec2(width / 2, height / 2)


def corner_anchor(corner: StartCorner, map_size: tuple[int, int]) -> Vec2:
    """Point de référence du coin, à `CORNER_MARGIN` cases du bord.

    L'axe x va vers l'est, l'axe y vers le sud. L'origine est le coin nord-ouest.
    """

    width, height = map_size
    if width <= 2 * CORNER_MARGIN or height <= 2 * CORNER_MARGIN:
        raise ValueError("carte trop petite pour un coin de départ")
    if corner in (StartCorner.SOUTHWEST, StartCorner.NORTHWEST):
        x = CORNER_MARGIN
    else:
        x = width - CORNER_MARGIN
    if corner in (StartCorner.SOUTHWEST, StartCorner.SOUTHEAST):
        y = height - CORNER_MARGIN
    else:
        y = CORNER_MARGIN
    return Vec2(x, y)


def place_armies(
    map_size: tuple[int, int],
    roman_start_position: str,
    n_legionaries: int,
    n_cataphracts: int,
    n_cavalry_archers: int,
    n_trebuchets: int,
    seed: int | None = None,
) -> tuple[UnitState, ...]:
    """Pose les deux armées. Membre 7, tâche 2.

    Romains autour du coin, sans bloc serré. Parthes entre 10 et 20 cases du centre,
    entre les Romains et le château. Aucune unité sur une falaise ni dans l'emprise :
    appeler `cliff_tiles` et `castle_footprint` dès qu'ils existent.
    """

    del (
        map_size,
        roman_start_position,
        n_legionaries,
        n_cataphracts,
        n_cavalry_archers,
        n_trebuchets,
        seed,
    )
    raise NotImplementedError(
        "Membre 7, tâche 2 : placement. docs/repartition-taches.md."
    )
