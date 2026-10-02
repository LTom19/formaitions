"""État d'une formation. Pas de calcul de slots au sprint 0."""

from __future__ import annotations

from dataclasses import dataclass

from formaitions.domaine.contracts import Vec2
from formaitions.formations.shapes import Shape


@dataclass(frozen=True)
class Formation:
    """Arrangement suivi par un général. Le monde ne stocke pas cet objet."""

    id: int
    member_ids: tuple[int, ...]
    anchor: Vec2
    facing: float
    shape: Shape
