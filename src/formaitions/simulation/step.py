"""Un pas de temps. Membre 1.

Tâches 1, 6, 7 et 8 dans docs/repartition-taches.md.
Ordre prévu, quand les fonctions existent :
1. refuser un `dt` différent de 0,05 ;
2. appliquer MoveTo, Hold, Pack, Unpack via `mouvement` ;
3. appeler `collision.blocked` avant d'écrire une position ;
4. décrémenter animation et rechargement ;
5. appeler `combat.resolve_attack_end` quand l'animation tombe à 0 ;
6. avancer `now` et renvoyer des `Event` datés.

Ce fichier n'écrit pas les formules ni les rayons.
Lancer : pytest -m membre1
"""

from __future__ import annotations

from formaitions.domaine.contracts import FIXED_DT, Event, Order
from formaitions.simulation.monde import World

MEMBER = 1


def step(world: World, orders: list[Order], dt: float = FIXED_DT) -> list[Event]:
    """Avance le monde de `dt` secondes de jeu.

    Le monde peut refuser un ordre. Le refus est visible au pas suivant.
    """

    del world, orders
    if dt != FIXED_DT:
        raise ValueError(f"le pas gelé est {FIXED_DT} s, reçu {dt}")
    raise NotImplementedError(
        "Membre 1, tâche 1 : le pas de simulation. docs/repartition-taches.md."
    )
