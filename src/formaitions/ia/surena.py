"""Général parthe. Membre 5.

Tâches 7 et 8 dans docs/repartition-taches.md.
`decide` ne modifie pas l'observation. Il ne code pas Crassus.
Lancer : pytest -m membre5
"""

from __future__ import annotations

from formaitions.domaine.contracts import Decision, Observation, Order

MEMBER = 5


class Surena:
    """Poids nommés. La destination suit les trébuchets de l'observation."""

    def __init__(self, boldness: float = 50, **weights: float) -> None:
        self.boldness = boldness
        self.weights = weights
        self.decisions: list[Decision] = []

    def decide(self, observation: Observation, now: float) -> list[Order]:
        """Membre 5, tâche 7. Les noms de règles sont dans le document."""

        del observation, now
        raise NotImplementedError(
            "Membre 5, tâche 7 : Suréna. docs/repartition-taches.md."
        )
