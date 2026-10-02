"""Contrats du sprint 0 : signatures, pas de temps, frontières."""

from __future__ import annotations

import ast
import inspect
from pathlib import Path

import pytest

from formaitions.domaine.contracts import (
    FIXED_DT,
    Attack,
    BattleResult,
    Event,
    General,
    Hold,
    MoveTo,
    Observation,
    Outcome,
    Pack,
    Team,
    UnitKind,
    UnitState,
    Unpack,
    Vec2,
)
from formaitions.formations.commands import Advance, FormCircle, Screen
from formaitions.formations.model import Formation
from formaitions.formations.shapes import Shape
from formaitions.scenario import Carrhae
from formaitions.simulation import step

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src" / "formaitions"


class _Idle:
    def decide(self, observation: Observation, now: float) -> list[MoveTo]:
        del observation, now
        return []


def test_fixed_timestep_is_twenty_hertz() -> None:
    assert FIXED_DT == 0.05


def test_observation_is_frozen() -> None:
    observation = Observation(
        now=0.0,
        map_size=(120, 120),
        units=(),
        projectiles=(),
        castle_hp=10000,
        castle_position=Vec2(60, 60),
        cliff_tiles=(),
    )
    with pytest.raises(AttributeError):
        observation.now = 1.0  # type: ignore[misc]


def test_orders_cover_the_world_contract() -> None:
    destination = Vec2(1.0, 2.0)
    orders = [
        MoveTo(1, destination),
        Hold(1),
        Attack(1, 2),
        Pack(1),
        Unpack(1),
    ]
    assert all(order.unit_id == 1 for order in orders)


def test_general_protocol_accepts_a_decide_method() -> None:
    assert isinstance(_Idle(), General)


def test_carrhae_signature_matches_the_subject() -> None:
    signature = inspect.signature(Carrhae)
    assert list(signature.parameters) == [
        "roman_ai",
        "parthian_ai",
        "n_legionaries",
        "n_cataphracts",
        "n_cavalry_archers",
        "n_trebuchets",
        "roman_start_position",
        "seed",
        "map_size",
        "headless",
        "speed",
    ]
    defaults = {
        name: parameter.default
        for name, parameter in signature.parameters.items()
    }
    assert defaults["n_legionaries"] == 60
    assert defaults["n_cataphracts"] == 20
    assert defaults["n_cavalry_archers"] == 20
    assert defaults["n_trebuchets"] == 3
    assert defaults["roman_start_position"] == "W"
    assert defaults["seed"] is None
    assert defaults["map_size"] == (120, 120)
    assert defaults["headless"] is False
    assert defaults["speed"] == 1
    assert signature.return_annotation is BattleResult


def test_carrhae_and_step_are_not_simulated_yet() -> None:
    with pytest.raises(NotImplementedError):
        Carrhae(_Idle(), _Idle())
    with pytest.raises(NotImplementedError):
        step(object(), [], FIXED_DT)
    with pytest.raises(ValueError, match="0.05"):
        step(object(), [], 1.0)


def test_formation_commands_do_not_move_units() -> None:
    formation = Formation(
        id=1,
        member_ids=(1, 2, 3),
        anchor=Vec2(0.0, 0.0),
        facing=0.0,
        shape=Shape.BLOCK_DENSE,
    )
    command = Screen(
        formation_id=formation.id,
        protected_unit_id=9,
        threat=Vec2(4.0, 0.0),
    )
    circle = FormCircle(formation.id, around=Vec2(2.0, 2.0))
    advance = Advance(formation.id, Vec2(8.0, 1.0))
    assert command.protected_unit_id == 9
    assert circle.around_unit_id is None
    assert advance.destination.x == 8.0


def test_unit_state_uses_float_position() -> None:
    unit = UnitState(
        id=1,
        kind=UnitKind.LEGIONARY,
        team=Team.ROMAN,
        position=Vec2(0.5, 1.25),
        hp=75,
        alive=True,
        reload_remaining=0.0,
        attack_animation_remaining=0.0,
        packed=False,
    )
    assert isinstance(unit.position.x, float)


def test_result_types_exist_for_the_public_return() -> None:
    assert Outcome.DRAW.value == "draw"
    event = Event(0.0, "decision", (("general", "crassus"),))
    assert event.details[0][0] == "general"


def test_simulation_does_not_import_formations_ai_or_view() -> None:
    banned_by_package = {
        "simulation": {
            "formaitions.ia",
            "formaitions.formations",
            "formaitions.vue",
            "formaitions.scenario",
            "pygame",
        },
        "formations": {
            "formaitions.simulation",
            "formaitions.ia",
            "formaitions.vue",
            "formaitions.scenario",
            "pygame",
        },
        "domaine": {
            "formaitions.simulation",
            "formaitions.ia",
            "formaitions.formations",
            "formaitions.vue",
            "formaitions.scenario",
            "pygame",
        },
    }
    violations: list[str] = []
    for package, banned in banned_by_package.items():
        for path in (SRC / package).rglob("*.py"):
            tree = ast.parse(path.read_text(encoding="utf-8"))
            for node in ast.walk(tree):
                modules = _imported_modules(node)
                for module in modules:
                    if module in banned or any(module.startswith(item + ".") for item in banned):
                        violations.append(f"{path.name} importe {module}")
    assert violations == []


def _imported_modules(node: ast.AST) -> list[str]:
    if isinstance(node, ast.Import):
        return [alias.name for alias in node.names]
    if isinstance(node, ast.ImportFrom) and node.module:
        return [node.module]
    return []
