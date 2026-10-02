"""Sauvegarde d'une bataille pour la reprendre en soutenance. Pas encore écrite."""

from __future__ import annotations

from formaitions.domaine.contracts import Observation


def save_battle(snapshot: Observation, path: str) -> None:
    """Écrit l'instantané. Le rechargement ne rejoue pas un script."""

    del snapshot, path
    raise NotImplementedError("La sauvegarde d'une bataille n'est pas encore écrite.")


def load_battle(path: str) -> Observation:
    """Relit un instantané écrit par `save_battle`."""

    del path
    raise NotImplementedError("Le chargement d'une bataille n'est pas encore écrit.")
