"""Règles de simulation. Ce package n'importe ni les formations, ni les IA, ni la vue.

Membre 1 : `step`, `monde`, `mouvement`.
Membre 2 : `carte`, `collision`.
Membre 3 : `combat`.
"""

from formaitions.simulation.step import step

__all__ = ["step"]
