"""Essai sprint 0 : une case isométrique et une silhouette, sans règle de jeu.

Les tests fixent `SDL_VIDEODRIVER=dummy` avant d'importer ce module.
Lancé directement, il utilise l'écran disponible.
"""

from __future__ import annotations

import os
import sys

import pygame

TILE_WIDTH = 64
TILE_HEIGHT = 32
CANVAS_SIZE = (320, 240)


def iso_to_screen(x: float, y: float, origin: tuple[int, int]) -> tuple[int, int]:
    """Projection 2:1. L'axe x va vers le bas-droite, l'axe y vers le bas-gauche."""

    origin_x, origin_y = origin
    screen_x = origin_x + (x - y) * (TILE_WIDTH / 2)
    screen_y = origin_y + (x + y) * (TILE_HEIGHT / 2)
    return int(screen_x), int(screen_y)


def make_placeholder_sprite() -> pygame.Surface:
    """Silhouette interchangeable, en attendant une source de sprites acceptée."""

    sprite = pygame.Surface((20, 28), pygame.SRCALPHA)
    pygame.draw.ellipse(sprite, (170, 45, 40), (4, 10, 12, 16))
    pygame.draw.circle(sprite, (230, 190, 140), (10, 7), 5)
    return sprite


def render_spike() -> pygame.Surface:
    """Dessine une case et un sprite. N'ouvre pas de fenêtre."""

    if not pygame.get_init():
        pygame.init()
    canvas = pygame.Surface(CANVAS_SIZE)
    canvas.fill((24, 32, 24))
    center = iso_to_screen(0, 0, (CANVAS_SIZE[0] // 2, 96))
    half_width = TILE_WIDTH // 2
    half_height = TILE_HEIGHT // 2
    center_x, center_y = center
    diamond = [
        (center_x, center_y - half_height),
        (center_x + half_width, center_y),
        (center_x, center_y + half_height),
        (center_x - half_width, center_y),
    ]
    pygame.draw.polygon(canvas, (96, 148, 72), diamond)
    pygame.draw.polygon(canvas, (36, 72, 32), diamond, 2)
    sprite = make_placeholder_sprite()
    canvas.blit(
        sprite,
        (
            center_x - sprite.get_width() // 2,
            center_y - sprite.get_height() + 6,
        ),
    )
    return canvas


def main() -> None:
    """Affiche l'essai si un écran existe, et écrit toujours une image."""

    image = render_spike()
    output = os.environ.get("FORMAITIONS_SPIKE_OUT", "artifacts/spike_isometric.png")
    os.makedirs(os.path.dirname(output) or ".", exist_ok=True)
    pygame.image.save(image, output)
    print(f"essai écrit : {output}")
    if os.environ.get("SDL_VIDEODRIVER") == "dummy":
        return
    pygame.display.set_mode(CANVAS_SIZE)
    screen = pygame.display.get_surface()
    if screen is None:
        return
    screen.blit(image, (0, 0))
    pygame.display.flip()
    pygame.time.wait(800)
    pygame.quit()


if __name__ == "__main__":
    main()
    sys.exit(0)
