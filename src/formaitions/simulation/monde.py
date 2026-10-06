"""État mutable d'une bataille. Membre 1.

Tâches : docs/repartition-taches.md, section « Membre 1 ».
Le contenant est là. `observe` et `step` restent à écrire.
Lancer : pytest -m membre1
"""

from __future__ import annotations

from dataclasses import dataclass, field

from formaitions.domaine.contracts import (
    Observation,
    ProjectileState,
    UnitState,
    Vec2,
)

MEMBER = 1


@dataclass
class World:
    """Monde que `step` fait avancer. Les généraux ne reçoivent jamais cet objet.

    Les unités sont remplacées, pas modifiées sur place : `UnitState` est gelé.
    """

    now: float
    map_size: tuple[int, int]
    units: list[UnitState] = field(default_factory=list)
    projectiles: list[ProjectileState] = field(default_factory=list)
    castle_hp: float = 10000.0
    castle_position: Vec2 = Vec2(60.0, 60.0)
    cliff_tiles: tuple[tuple[int, int], ...] = ()


def observe(world: World) -> Observation:
    """Copie figée pour un général et pour la vue. Membre 1, avant la tâche 7 du membre 7.

    La copie ne contient pas la direction, la vitesse ni la destination.
    """

    del world
    raise NotImplementedError(
        "Membre 1 : écrire observe. Voir docs/repartition-taches.md."
    )
