# 003 — Précisions du groupe et du professeur

Date : 2 octobre 2026.

Ces points complètent [001-contrats.md](001-contrats.md). Les questions encore ouvertes restent dans [000-groupe.md](000-groupe.md).

## Retenu

- Le rapport est visé le 8 décembre 2026, une semaine avant la soutenance FISA du 15 décembre. Le professeur aura accès au dépôt GitHub du groupe. Le dépôt https://github.com/LTom19/formaitions reste un entraînement personnel.
- `"W"` est le coin sud-ouest de la carte. `"E"` est le coin sud-est, pour observer le même comportement depuis un autre départ. `"NW"` et `"NE"` sont acceptés. L’axe x va vers l’est, l’axe y vers le sud.
- Le château est toujours au centre, même si `map_size` change.
- Personne ne commande les unités à la souris. On relance la bataille avec d’autres paramètres. Selon ces paramètres, les chances de victoire doivent pouvoir monter ou descendre.
- La bataille n’est pas déterministe et n’est pas un script de troupes. `seed` reste dans la signature du sujet, sans garantir deux parties identiques.
- On prévoit la sauvegarde et le chargement d’un instantané de bataille, pour la répétition de la soutenance. Ce n’est pas encore codé.
- Le journal d’IA enregistre quelle règle s’est déclenchée, pas seulement qu’une décision a eu lieu.
- Une troupe vivante a une hitbox. Pour atteindre une cible, on contourne l’unité qui bloque ou on la tue. On ne passe pas au travers.
- Le timeout est une sécurité pour arrêter une partie où les IA refusent d’agir ou de conclure. Le délai de référence reste celui du sujet : une minute sans dégât.
- Les Romains passent en formation serrée, type tortue, face aux archers, et se dispersent face aux dégâts de zone. Les Parthes s’adaptent aussi. Ce n’est pas une trajectoire écrite d’avance.
- Pendant le développement, des variantes d’une même IA doivent pouvoir s’affronter pour comparer leur progression.
- Un général voit toutes les troupes du terrain et leurs PV, alliées comme ennemies. Il ne reçoit pas la direction des troupes.
- La minicarte permanente sert à se déplacer sur la carte. Elle n’est plus optionnelle.

## Laissé ouvert

- La liste 68 à 83 est-elle bien celle du rapport vert / jaune / rouge ?
- Que fait un tir de trébuchet manqué, et comment part la salve de 5 du château ?
- Le code des années précédentes est-il disponible ?

## Ce qui n’a pas été implémenté

Le placement réel des armées, le combat, les généraux, la sauvegarde et la minicarte. Seuls les contrats et les coins de départ sont dans le code, pour que la suite ne les réinterprète pas.
