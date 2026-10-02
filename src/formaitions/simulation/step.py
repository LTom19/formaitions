"""Un pas de temps. Le déplacement et le combat ne sont pas encore écrits."""

from __future__ import annotations

from formaitions.domaine.contracts import FIXED_DT, Event, Order


def step(world: object, orders: list[Order], dt: float = FIXED_DT) -> list[Event]:
    """Avance le monde de `dt` secondes de jeu.

    Le monde peut refuser un ordre. Le refus devra être visible au pas suivant.
    Cette fonction n'applique encore aucune règle : le sprint 1 la remplit.
    """

    del world, orders
    if dt != FIXED_DT:
        raise ValueError(f"le pas gelé est {FIXED_DT} s, reçu {dt}")
    raise NotImplementedError("Le pas de simulation commence au sprint 1.")
