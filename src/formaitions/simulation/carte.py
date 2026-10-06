"""Carte, château, falaises. Membre 2.

Tâches 1, 2 et 8 dans docs/repartition-taches.md.
`Map` se construit à la main dans les tests. `build_map` reste à écrire.
Lancer : pytest -m membre2
"""

from __future__ import annotations

from dataclasses import dataclass

from formaitions.domaine.contracts import Vec2

MEMBER = 2


@dataclass(frozen=True)
class Map:
    """Plaine, emprise du château, anneau de falaises. Pas d'unités."""

    size: tuple[int, int]
    footprint: tuple[tuple[int, int], ...]
    cliffs: tuple[tuple[int, int], ...]


def build_map(map_size: tuple[int, int] = (120, 120)) -> Map:
    """Centre le château, emprise 4×4, anneau d'une case. Membre 2, tâche 1."""

    del map_size
    raise NotImplementedError(
        "Membre 2, tâche 1 : construire la carte. docs/repartition-taches.md."
    )


def blocks_ground(game_map: Map, position: Vec2) -> bool:
    """Vrai sur une falaise et sur l'emprise du château. Membre 2, tâche 2."""

    del game_map, position
    raise NotImplementedError(
        "Membre 2, tâche 2 : sol infranchissable. docs/repartition-taches.md."
    )


def blocks_shot(game_map: Map, position: Vec2) -> bool:
    """Toujours faux : un tir passe au-dessus des falaises. Membre 2, tâche 2."""

    del game_map, position
    raise NotImplementedError(
        "Membre 2, tâche 2 : un tir n'est pas bloqué. docs/repartition-taches.md."
    )


def castle_footprint(game_map: Map) -> tuple[tuple[int, int], ...]:
    """Cases de l'emprise 4×4. Le membre 7 s'en sert pour le placement."""

    del game_map
    raise NotImplementedError(
        "Membre 2, tâche 8 : emprise du château. docs/repartition-taches.md."
    )


def cliff_tiles(game_map: Map) -> tuple[tuple[int, int], ...]:
    """Cases de l'anneau. Disjointes de l'emprise. Le membre 7 s'en sert."""

    del game_map
    raise NotImplementedError(
        "Membre 2, tâche 8 : anneau de falaises. docs/repartition-taches.md."
    )
