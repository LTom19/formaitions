"""Formes et slots. Membre 4.

Tâches 1 à 3 dans docs/repartition-taches.md.
`slots` ne crée pas de monde et ne déplace personne.
Les distances utiles sont dans `formaitions.domaine.stats`.
Lancer : pytest -m membre4
"""

from __future__ import annotations

from enum import Enum

from formaitions.domaine.contracts import Vec2

MEMBER = 4


class Shape(Enum):
    CIRCLE = "circle"
    LINE = "line"
    BLOCK_DENSE = "block_dense"
    BLOCK_LOOSE = "block_loose"


def slots(shape: Shape, ids: tuple[int, ...], anchor: Vec2) -> dict[int, Vec2]:
    """Une position par identifiant. Membre 4, tâches 1 à 3.

    Bloc serré : voisins dans ]0,40 ; 0,42]. Bloc lâche : le mur ne peut pas s'activer.
    """

    del shape, ids, anchor
    raise NotImplementedError(
        "Membre 4, tâches 1 à 3 : slots. docs/repartition-taches.md."
    )
