"""BRAINDEAD et BEDLAM. Membre 7.

Ajoute ici les tests sur un instantané fabriqué, sans lancer `Carrhae`.
"""

from __future__ import annotations

import inspect

import pytest

from formaitions.ia.bedlam import Bedlam
from formaitions.ia.braindead import Braindead

pytestmark = pytest.mark.membre7


def test_reference_generals_expose_decide() -> None:
    idle = Braindead()
    brawler = Bedlam(team_name="parthian")
    assert brawler.team_name == "parthian"
    assert list(inspect.signature(idle.decide).parameters) == ["observation", "now"]
    assert list(inspect.signature(brawler.decide).parameters) == ["observation", "now"]
