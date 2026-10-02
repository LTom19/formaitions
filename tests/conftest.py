"""Les tests graphiques ne doivent pas ouvrir l'écran de la machine."""

import os

os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
os.environ.setdefault("SDL_AUDIODRIVER", "dummy")
