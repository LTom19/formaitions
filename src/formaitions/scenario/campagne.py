"""Plusieurs batailles headless, pour voir si un paramètre change quelque chose. Membre 7, tâche 8.

Ne promet pas que la même graine rejoue la même partie.
Lancer : pytest -m membre7
"""

from __future__ import annotations

from formaitions.domaine.contracts import BattleResult

MEMBER = 7


def run_campaign(n: int, **variants: object) -> tuple[BattleResult, ...]:
    """Lance `n` appels de `Carrhae`. `variants` sont les arguments qui changent."""

    del n, variants
    raise NotImplementedError(
        "Membre 7, tâche 8 : campagne. docs/repartition-taches.md."
    )
