"""État d'une formation, réassignation, écart. Membre 4.

Tâches 4 et 5 dans docs/repartition-taches.md.
Le monde ne stocke pas une `Formation`. Lancer : pytest -m membre4
"""

from __future__ import annotations

from dataclasses import dataclass

from formaitions.domaine.contracts import Vec2
from formaitions.formations.shapes import Shape

MEMBER = 4


@dataclass(frozen=True)
class Formation:
    """Arrangement suivi par un général. Le monde ne stocke pas cet objet."""

    id: int
    member_ids: tuple[int, ...]
    anchor: Vec2
    facing: float
    shape: Shape


def reassign(formation: Formation, living_ids: tuple[int, ...]) -> Formation:
    """Retire les morts et recalcule les slots. Membre 4, tâche 4."""

    del formation, living_ids
    raise NotImplementedError(
        "Membre 4, tâche 4 : réassignation. docs/repartition-taches.md."
    )


def cohesion_error(
    positions: dict[int, Vec2],
    assigned: dict[int, Vec2],
) -> float:
    """Plus grande distance entre un soldat et son slot. Membre 4, tâche 5."""

    del positions, assigned
    raise NotImplementedError(
        "Membre 4, tâche 5 : cohésion. docs/repartition-taches.md."
    )
