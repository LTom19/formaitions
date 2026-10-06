"""Sauvegarde d'une bataille pour la reprendre en soutenance. Membre 7, tâche 7.

Le fichier contient un instantané, pas la liste des ordres futurs.
Lancer : pytest -m membre7
"""

from __future__ import annotations

from formaitions.domaine.contracts import Observation

MEMBER = 7


def save_battle(snapshot: Observation, path: str) -> None:
    """Écrit l'instantané. Le rechargement ne rejoue pas un script."""

    del snapshot, path
    raise NotImplementedError(
        "Membre 7, tâche 7 : sauvegarde. docs/repartition-taches.md."
    )


def load_battle(path: str) -> Observation:
    """Relit un instantané écrit par `save_battle`."""

    del path
    raise NotImplementedError(
        "Membre 7, tâche 7 : chargement. docs/repartition-taches.md."
    )
