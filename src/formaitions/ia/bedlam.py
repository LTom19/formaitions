"""Major BEDLAM. Membre 7, tâche 5.

Chaque unité vivante attaque l'ennemi le plus proche, ou marche vers lui.
Pas de formation. La règle journalisée est `attack_nearest`.
Lancer : pytest -m membre7
"""

from __future__ import annotations

from formaitions.domaine.contracts import Decision, Observation, Order

MEMBER = 7


class Bedlam:
    def __init__(self, team_name: str) -> None:
        """`team_name` vaut `roman` ou `parthian`, le camp que ce BEDLAM commande."""

        self.team_name = team_name
        self.decisions: list[Decision] = []

    def decide(self, observation: Observation, now: float) -> list[Order]:
        del observation, now
        raise NotImplementedError(
            "Membre 7, tâche 5 : BEDLAM. docs/repartition-taches.md."
        )
