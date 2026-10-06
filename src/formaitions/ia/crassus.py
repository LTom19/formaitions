"""Général romain. Membre 4.

Tâches 6 à 8 dans docs/repartition-taches.md.
`decide` lit une observation et renvoie des ordres. Il ne modifie pas le monde.
Les slots viennent de `formations.shapes`. La traduction collective, de `commands.translate`.
Lancer : pytest -m membre4
"""

from __future__ import annotations

from formaitions.domaine.contracts import Decision, Observation, Order

MEMBER = 4


class Crassus:
    """Poids nommés, pas une trajectoire écrite d'avance."""

    def __init__(self, aggressiveness: float = 50, **weights: float) -> None:
        self.aggressiveness = aggressiveness
        self.weights = weights
        self.decisions: list[Decision] = []

    def decide(self, observation: Observation, now: float) -> list[Order]:
        """Membre 4, tâche 6. Chaque règle journalisée a un nom fixe, voir le document."""

        del observation, now
        raise NotImplementedError(
            "Membre 4, tâche 6 : Crassus. docs/repartition-taches.md."
        )
