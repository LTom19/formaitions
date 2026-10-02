"""Types partagés. Aucune règle de simulation, aucune formation, aucun affichage."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Protocol, runtime_checkable

# Pas fixe. `speed` ne modifie pas cette valeur : il rapproche le temps de jeu du temps réel.
FIXED_DT = 0.05


class Team(Enum):
    ROMAN = "roman"
    PARTHIAN = "parthian"


class UnitKind(Enum):
    LEGIONARY = "legionary"
    ELITE_CATAPHRACT = "elite_cataphract"
    HEAVY_CAVALRY_ARCHER = "heavy_cavalry_archer"
    TREBUCHET = "trebuchet"


class Outcome(Enum):
    ROMAN = "roman"
    PARTHIAN = "parthian"
    DRAW = "draw"


@dataclass(frozen=True)
class Vec2:
    x: float
    y: float


@dataclass(frozen=True)
class UnitState:
    """Copie lisible d'une unité. La modifier ne change pas le monde.

    Pas de direction, de vitesse ni de destination : un général voit les troupes
    et leurs PV, pas le cap des ennemis.
    """

    id: int
    kind: UnitKind
    team: Team
    position: Vec2
    hp: float
    alive: bool
    reload_remaining: float
    attack_animation_remaining: float
    packed: bool


@dataclass(frozen=True)
class ProjectileState:
    id: int
    position: Vec2
    target: Vec2
    source_id: int


@dataclass(frozen=True)
class Observation:
    """Instantané figé transmis aux généraux.

    Toutes les unités, alliées et ennemies, avec leurs PV. Les projectiles visibles
    y figurent aussi. La direction des troupes n'y est pas.
    """

    now: float
    map_size: tuple[int, int]
    units: tuple[UnitState, ...]
    projectiles: tuple[ProjectileState, ...]
    castle_hp: float
    castle_position: Vec2
    cliff_tiles: tuple[tuple[int, int], ...]


@dataclass(frozen=True)
class MoveTo:
    unit_id: int
    destination: Vec2


@dataclass(frozen=True)
class Hold:
    unit_id: int


@dataclass(frozen=True)
class Attack:
    unit_id: int
    target_id: int


@dataclass(frozen=True)
class Pack:
    unit_id: int


@dataclass(frozen=True)
class Unpack:
    unit_id: int


Order = MoveTo | Hold | Attack | Pack | Unpack


@dataclass(frozen=True)
class Event:
    time: float
    name: str
    details: tuple[tuple[str, str], ...] = ()


@dataclass(frozen=True)
class Decision:
    """Règle d'IA qui s'est déclenchée. `rule` ne peut pas être vide."""

    time: float
    general: str
    rule: str
    details: tuple[tuple[str, str], ...] = ()

    def __post_init__(self) -> None:
        if not self.rule.strip():
            raise ValueError("une décision doit nommer la règle qui s'est déclenchée")


@dataclass(frozen=True)
class BattleResult:
    outcome: Outcome
    elapsed: float
    units: tuple[UnitState, ...]
    loss_timeline: tuple[Event, ...]
    decision_log: tuple[Decision, ...]


@runtime_checkable
class General(Protocol):
    """Un général lit un instantané et renvoie des ordres. Il n'écrit pas dans le monde."""

    def decide(self, observation: Observation, now: float) -> list[Order]:
        """Prochaines intentions de cette armée à l'instant `now`."""
