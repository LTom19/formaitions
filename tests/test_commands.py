"""Traduction des commandes collectives. Membre 5.

Ajoute ici les tests avec un `slots_for` faux. Ils n'appellent pas le vrai `slots`.
"""

from __future__ import annotations

import inspect

import pytest

from formaitions.formations.commands import Translation, translate

pytestmark = pytest.mark.membre5


def test_translate_takes_an_injected_slot_function() -> None:
    parameters = inspect.signature(translate).parameters
    assert list(parameters) == ["command", "formation", "slots_for"]
    assert "orders" in Translation.__dataclass_fields__
    assert "formations" in Translation.__dataclass_fields__
