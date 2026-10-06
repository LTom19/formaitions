"""Commandes collectives. Membre 5.

Tâches 1 à 6 dans docs/repartition-taches.md.
`translate` reçoit `slots_for` : il ne choisit pas la géométrie.
Il n'importe pas `simulation`. Lancer : pytest -m membre5
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass

from formaitions.domaine.contracts import Order, Vec2
from formaitions.formations.model import Formation
from formaitions.formations.shapes import Shape

MEMBER = 5

SlotsFor = Callable[[Shape, tuple[int, ...], Vec2], dict[int, Vec2]]


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


@dataclass(frozen=True)
class Translation:
    """Ordres individuels, et les formations qui résultent d'un split ou d'un merge.

    `formations` reprend l'entrée telle quelle quand la commande ne la coupe pas.
    """

    orders: tuple[Order, ...]
    formations: tuple[Formation, ...]


def translate(
    command: FormationCommand,
    formation: Formation,
    slots_for: SlotsFor,
) -> Translation:
    """Un ordre par soldat concerné, personne oublié. Membre 5, tâches 1 à 5."""

    del command, formation, slots_for
    raise NotImplementedError(
        "Membre 5, tâches 1 à 5 : traduire une commande. docs/repartition-taches.md."
    )
