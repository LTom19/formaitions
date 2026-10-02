"""L'essai isométrique produit une case et un sprite sans ouvrir de fenêtre."""

from __future__ import annotations

import os

os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
os.environ.setdefault("SDL_AUDIODRIVER", "dummy")

from formaitions.vue.spike import CANVAS_SIZE, render_spike


def test_spike_draws_one_tile_and_one_sprite_without_a_window() -> None:
    import pygame

    image = render_spike()
    assert image.get_size() == CANVAS_SIZE
    assert pygame.display.get_surface() is None

    center_x = CANVAS_SIZE[0] // 2
    tile = image.get_at((center_x + 20, 96))
    assert tile.g > tile.r + 20
    assert tile.g > 100

    sprite_pixel = image.get_at((center_x, 92))
    assert sprite_pixel.r > sprite_pixel.g + 40
    assert sprite_pixel.r > 100
