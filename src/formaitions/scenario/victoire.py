"""Issues de Carrhes, sur un état déjà calculé. Membre 7, tâche 3.

Pas de boucle ici. Les pertes de légionnaires ou de cavalerie ne décident rien.
Lancer : pytest -m membre7
"""

from __future__ import annotations

from formaitions.domaine.contracts import Event, Outcome

MEMBER = 7


def outcome(
    castle_hp: float,
    trebuchets_alive: int,
    events: tuple[Event, ...],
    elapsed: float,
) -> Outcome:
    """Château à 0 : romain. Plus aucun trébuchet : parthe. 60 s sans dégât : nul."""

    del castle_hp, trebuchets_alive, events, elapsed
    raise NotImplementedError(
        "Membre 7, tâche 3 : conditions de victoire. docs/repartition-taches.md."
    )
