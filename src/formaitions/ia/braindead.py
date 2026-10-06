"""Sergent BRAINDEAD. Membre 7, tâche 4.

Devant n'importe quel instantané, aucun ordre. La règle journalisée est `idle`.
Lancer : pytest -m membre7
"""

from __future__ import annotations

from formaitions.domaine.contracts import Decision, Observation, Order

MEMBER = 7


class Braindead:
    def __init__(self) -> None:
        self.decisions: list[Decision] = []

    def decide(self, observation: Observation, now: float) -> list[Order]:
        del observation, now
        raise NotImplementedError(
            "Membre 7, tâche 4 : BRAINDEAD. docs/repartition-taches.md."
        )
