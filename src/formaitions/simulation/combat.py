"""Dégâts, mur de boucliers, projectiles. Membre 3.

Tâches 1 à 8 dans docs/repartition-taches.md.
Les nombres sont dans `formaitions.domaine.stats`. Ce module ne déplace pas
les unités et n'importe ni `formations` ni `ia`.
Lancer : pytest -m membre3
"""

from __future__ import annotations

from dataclasses import dataclass

from formaitions.domaine.contracts import (
    Event,
    Order,
    ProjectileState,
    UnitState,
    Vec2,
)
from formaitions.simulation.carte import Map

MEMBER = 3


@dataclass(frozen=True)
class AttackResolution:
    """Effet retourné à `step`. Les unités reçues en entrée ne sont pas modifiées.

    `hp_by_id` : identifiant, nouveaux points de vie.
    `castle_hp` vaut None si le château n'a pas été touché.
    """

    hp_by_id: tuple[tuple[int, float], ...]
    castle_hp: float | None
    projectiles: tuple[ProjectileState, ...]
    events: tuple[Event, ...]
    reload_remaining: float | None


def damage_simple(attack: float, armour: float) -> float:
    """`max(1, attaque - armure)`. Membre 3, tâche 1."""

    del attack, armour
    raise NotImplementedError(
        "Membre 3, tâche 1 : formule simple. docs/repartition-taches.md."
    )


def damage_typed(pairs: tuple[tuple[float, float], ...]) -> float:
    """`max(1, somme max(0, attaque_i - armure_i))`. Membre 3, tâche 2."""

    del pairs
    raise NotImplementedError(
        "Membre 3, tâche 2 : formule à plusieurs types. docs/repartition-taches.md."
    )


def shield_wall(legionary: UnitState, units: tuple[UnitState, ...]) -> bool:
    """Vrai s'il y a au moins 4 autres légionnaires vivants à ≤ 0,42. Membre 3, tâche 3."""

    del legionary, units
    raise NotImplementedError(
        "Membre 3, tâche 3 : mur de boucliers. docs/repartition-taches.md."
    )


def can_start_attack(
    attacker: UnitState,
    target: UnitState,
    game_map: Map,
    order: Order | None,
) -> bool:
    """Faux sans ordre Attack, pendant un rechargement, une animation, ou hors de portée.

    `order` vient de `step` : `UnitState` ne stocke pas l'ordre en cours.
    """

    del attacker, target, game_map, order
    raise NotImplementedError(
        "Membre 3, tâche 4 : droit de tirer. docs/repartition-taches.md."
    )


def resolve_attack_end(
    attacker: UnitState,
    primary: UnitState | None,
    units: tuple[UnitState, ...],
    *,
    castle_hp: float,
    castle_position: Vec2,
    game_map: Map,
    roll: float = 0.0,
    impact: bool = True,
    animation_just_finished: bool = True,
    next_projectile_id: int = 1,
) -> AttackResolution:
    """Applique les dégâts en fin d'animation. Membre 3, tâches 5 à 7.

    `roll` est tiré par l'appelant, dans le générateur du monde, pas ici.
    `impact=False` sert au test de l'archer : le projectile est créé, les PV ne baissent pas.
    """

    del (
        attacker,
        primary,
        units,
        castle_hp,
        castle_position,
        game_map,
        roll,
        impact,
        animation_just_finished,
        next_projectile_id,
    )
    raise NotImplementedError(
        "Membre 3, tâche 5 : fin d'animation. docs/repartition-taches.md."
    )


def resolve_castle_volley(
    units: tuple[UnitState, ...],
    castle_position: Vec2,
    next_projectile_id: int,
) -> AttackResolution:
    """Cinq projectiles vers l'ennemi le plus proche à portée. Le château n'est pas une UnitState."""

    del units, castle_position, next_projectile_id
    raise NotImplementedError(
        "Membre 3, tâche 6 : salve du château. docs/repartition-taches.md."
    )
