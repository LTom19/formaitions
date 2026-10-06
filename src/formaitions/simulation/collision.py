"""Disques, blocage, voisinage. Membre 2.

Tâches 3 à 6 dans docs/repartition-taches.md.
Les rayons sont dans `formaitions.domaine.stats`. Ce module ne déplace personne
et ne décide pas du mur de boucliers.
Lancer : pytest -m membre2
"""

from __future__ import annotations

from formaitions.domaine.contracts import UnitKind, UnitState, Vec2
from formaitions.simulation.carte import Map

MEMBER = 2


def radius(kind: UnitKind) -> float:
    """Rayon de collision du sujet. Membre 2, tâche 3."""

    del kind
    raise NotImplementedError(
        "Membre 2, tâche 3 : rayons. docs/repartition-taches.md."
    )


def overlaps(left: UnitState, right: UnitState) -> bool:
    """Vrai si les disques se recouvrent strictement. Le contact exact est permis."""

    del left, right
    raise NotImplementedError(
        "Membre 2, tâche 3 : chevauchement. docs/repartition-taches.md."
    )


def blocked(
    unit: UnitState,
    position: Vec2,
    others: tuple[UnitState, ...],
    game_map: Map,
) -> bool:
    """Vrai si cette position est interdite pour `unit`. Un mort ne bloque pas.

    Le membre 1 appelle cette fonction. Il n'édite pas ce fichier.
    """

    del unit, position, others, game_map
    raise NotImplementedError(
        "Membre 2, tâche 4 : blocked. docs/repartition-taches.md."
    )


def segment_blocked(
    start: Vec2,
    end: Vec2,
    unit: UnitState,
    others: tuple[UnitState, ...],
    game_map: Map,
) -> bool:
    """Vrai si le disque de `unit` touche un obstacle le long du segment."""

    del start, end, unit, others, game_map
    raise NotImplementedError(
        "Membre 2, tâche 5 : segment. docs/repartition-taches.md."
    )


def units_within(
    units: tuple[UnitState, ...],
    origin: Vec2,
    reach: float,
) -> tuple[UnitState, ...]:
    """Unités vivantes dont le centre est à une distance ≤ `reach`, origine exclue.

    Le membre 3 appelle cette fonction avec 0,42 et 0,75. Elle ne connaît pas l'armure.
    """

    del units, origin, reach
    raise NotImplementedError(
        "Membre 2, tâche 6 : voisinage. docs/repartition-taches.md."
    )
