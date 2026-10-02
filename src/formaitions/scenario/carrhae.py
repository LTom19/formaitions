"""Point d'entrée du scénario Carrhes. La bataille elle-même commence au sprint 1."""

from formaitions.domaine.contracts import BattleResult, General


def Carrhae(
    roman_ai: General,
    parthian_ai: General,
    n_legionaries: int = 60,
    n_cataphracts: int = 20,
    n_cavalry_archers: int = 20,
    n_trebuchets: int = 3,
    roman_start_position: str = "W",
    seed: int | None = None,
    map_size: tuple[int, int] = (120, 120),
    headless: bool = False,
    speed: float = 1,
) -> BattleResult:
    """Lance une bataille de Carrhes et renvoie son résultat.

    `headless=True` ne devra pas créer de fenêtre. Les effectifs et `roman_start_position`
    sont des paramètres : les IA ne les recopient pas en trajectoire fixe. `"W"` est le
    coin sud-ouest. Deux appels identiques peuvent diverger. `seed` reste dans la
    signature du sujet, sans promesse de rejeu. L'exécution arrive plus tard.
    """

    del (
        roman_ai,
        parthian_ai,
        n_legionaries,
        n_cataphracts,
        n_cavalry_archers,
        n_trebuchets,
        roman_start_position,
        seed,
        map_size,
        headless,
        speed,
    )
    raise NotImplementedError("Carrhae est signé, pas encore simulé.")
