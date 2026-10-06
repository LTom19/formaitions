"""Généraux. Crassus est au membre 4, Suréna au membre 5, BRAINDEAD et BEDLAM au membre 7.

Les variantes d'une même IA devront pouvoir s'affronter en headless. Une victoire
vient des formations qui s'adaptent, pas d'une trajectoire écrite d'avance.
Les quatre classes existent. Leur `decide` reste à écrire.
"""

from formaitions.ia.bedlam import Bedlam
from formaitions.ia.braindead import Braindead
from formaitions.ia.crassus import Crassus
from formaitions.ia.surena import Surena

__all__ = ["Bedlam", "Braindead", "Crassus", "Surena"]
