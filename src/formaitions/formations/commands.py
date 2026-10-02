"""Commandes collectives. Elles décrivent une intention ; elles ne déplacent rien."""

from __future__ import annotations

from dataclasses import dataclass

from formaitions.domaine.contracts import Vec2
from formaitions.formations.shapes import Shape


@dataclass(frozen=True)
class FormCircle:
    formation_id: int
    around: Vec2
    around_unit_id: int | None = None


@dataclass(frozen=True)
class Advance:
    formation_id: int
    destination: Vec2


@dataclass(frozen=True)
class Screen:
    """Maintenir la formation entre une unité protégée et une menace."""

    formation_id: int
    protected_unit_id: int
    threat: Vec2


@dataclass(frozen=True)
class Spread:
    formation_id: int


@dataclass(frozen=True)
class Transition:
    formation_id: int
    shape: Shape


@dataclass(frozen=True)
class Split:
    formation_id: int
    member_ids: tuple[int, ...]


@dataclass(frozen=True)
class Merge:
    left_id: int
    right_id: int


FormationCommand = FormCircle | Advance | Screen | Spread | Transition | Split | Merge
