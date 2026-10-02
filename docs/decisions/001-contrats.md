# 001 — Contrats gelés

Date : 2 octobre 2026.

Le groupe a validé l’architecture. Les signatures ci-dessous sont le contrat de développement parallèle. On ne les change qu’en ajoutant une décision datée dans ce dossier. Une modification de `Observation`, `Order` ou `step` demande deux revues, dont la personne responsable du noyau (Membre 1).

## Décisions d’architecture

1. Le pas de simulation est fixe : `FIXED_DT = 0.05` seconde de jeu. Le paramètre `speed` change le rapport au temps réel, pas `dt`.
2. Si `seed` est fourni, deux appels devront produire la même bataille. Le générateur appartient au monde. Le sprint 0 ne simule pas encore.
3. Les identifiants Python sont en anglais, comme la signature `Carrhae` du sujet. Le rapport peut être en français ou en anglais.
4. Les formations vivent dans `formaitions.formations` et dans les généraux. `formaitions.simulation` ne contient pas le mot formation, sauf plus tard la requête spatiale du mur de boucliers, qui ne devra importer ni `formations` ni `ia`.
5. Un général reçoit une `Observation` figée et renvoie des `Order`. Il ne modifie pas le monde. Le monde peut refuser un ordre ; le refus se verra au pas suivant.
6. `formaitions.vue` ne contient aucune règle. Importer `formaitions.vue` ne charge pas Pygame et n’ouvre pas de fenêtre. L’essai graphique est `python -m formaitions.vue.spike`.
7. Python 3.10 ou plus récent, un seul environnement, tests avec `pytest`. Le cours (section 18.1) écrit 3.9 comme minimum et rend 3.10 obligatoire dès sa sortie. Le code utilise la syntaxe 3.10.
8. Noms d’IA retenus pour la suite : Crassus et Suréna, avec des poids en arguments. Ils ne sont pas implémentés dans ce sprint.
9. Minicarte retenue pour la suite : permanente dans un coin. Réversible si l’essai de navigation échoue.
10. Les humains ne commandent pas les unités. Ils mettent en pause, règlent la vitesse, déplacent la caméra et relancent `Carrhae`. Ce point reste à confirmer avec l’enseignant, parce que le sujet dit « interaction » sans la détailler.

## Hypothèses provisoires, pas des règles du sujet

À signaler en jaune si elles survivent sans confirmation :

- Un tir de trébuchet manqué n’inflige aucun dégât. Il n’y a pas de dispersion. Le jet est tiré dans le générateur du monde au moment du tir.
- La salve du château émet cinq projectiles à la fin d’une seule animation, vers l’ennemi le plus proche à portée. Les projectiles supplémentaires frappent cette même cible s’il n’y en a pas cinq.

## Non décidé

Le secrétaire, le nombre exact de jours avant le rapport, l’adresse GitHub, le sens de « coin ouest » et la source des sprites AoE2. Voir [000-groupe.md](000-groupe.md). La filière est FISA, le groupe est le 2, l’effectif est 7. En attendant les sprites, l’essai utilise une silhouette dessinée, interchangeable. Il n’y a pas de second scénario à préparer.

## Signature publique

```python
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
) -> BattleResult: ...
```

`step(world, orders, dt=FIXED_DT) -> list[Event]` vit dans `formaitions.simulation`. Tant que le sprint 1 n’est pas là, elle lève `NotImplementedError`. Un `dt` différent de `0.05` est refusé.

## Ordres compris par le monde

`MoveTo`, `Hold`, `Attack`, `Pack`, `Unpack`. Rien d’autre. Une formation n’est pas un ordre du monde : `FormCircle`, `Advance`, `Screen`, `Spread`, `Transition`, `Split` et `Merge` sont des `FormationCommand`, traduites plus tard en ordres individuels.

## Qui peut importer qui

- `scenario` peut appeler `simulation`, `ia` et, seulement si la bataille n’est pas headless, `vue`.
- `ia` peut appeler `formations` et lire `domaine`. Elle n’écrit pas dans le monde.
- `formations` ne déplace rien. Elle ne importe pas `simulation`, `ia`, `vue`, ni Pygame.
- `simulation` ne importe pas `ia`, `formations`, `vue`, `scenario`, ni Pygame.
- `domaine` ne dépend d’aucun autre package du projet.
- `vue` lit des instantanés. L’essai isométrique est le seul module autorisé à importer Pygame pour l’instant.

## Git

La section 81 du sujet prime.

- Chaque commit est fait avec `user.name` au format `NOM Prénom`, le même que le rapport.
- Pas de compte partagé, pas d’historique réécrit, pas de squash qui efface l’auteur réel d’un autre membre.
- Un amend n’est acceptable que sur un commit encore local, par son auteur.
- `main` reste lançable. Branche courte `numero-resume-court`. Pull request avec au moins une revue extérieure à l’auteur.
- Le binôme des formations (Membres 4 et 5) ne s’auto-approuve pas.

La configuration Git de chaque machine se fait localement. Elle n’est pas imposée par un `git config` global du dépôt.
