"""Chaque fichier de code a un membre, et les frontières d'import tiennent."""

from __future__ import annotations

import ast
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src" / "formaitions"

EXPECTED = {
    "simulation/step.py": 1,
    "simulation/mouvement.py": 1,
    "simulation/monde.py": 1,
    "simulation/carte.py": 2,
    "simulation/collision.py": 2,
    "simulation/combat.py": 3,
    "formations/shapes.py": 4,
    "formations/model.py": 4,
    "ia/crassus.py": 4,
    "formations/commands.py": 5,
    "ia/surena.py": 5,
    "vue/spike.py": 6,
    "vue/bataille.py": 6,
    "vue/playback.py": 6,
    "scenario/carrhae.py": 7,
    "scenario/placement.py": 7,
    "scenario/save.py": 7,
    "scenario/victoire.py": 7,
    "scenario/campagne.py": 7,
    "ia/braindead.py": 7,
    "ia/bedlam.py": 7,
}


def _member_of(path: Path) -> int | None:
    tree = ast.parse(path.read_text(encoding="utf-8"))
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id == "MEMBER":
                assert isinstance(node.value, ast.Constant)
                return int(node.value.value)
    return None


def test_every_owned_file_names_its_member() -> None:
    found: dict[str, int] = {}
    for path in SRC.rglob("*.py"):
        relative = path.relative_to(SRC).as_posix()
        if path.name == "__init__.py" or relative.startswith("domaine/"):
            assert _member_of(path) is None, relative
            continue
        member = _member_of(path)
        assert member is not None, relative
        found[relative] = member
    assert found == EXPECTED
