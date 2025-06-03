import os
import sys
from pathlib import Path
from unittest.mock import patch

# Use dummy video driver for headless testing
os.environ.setdefault("SDL_VIDEODRIVER", "dummy")

sys.path.append(str(Path(__file__).resolve().parents[1]))

import pygame
import main


def test_draw_snake_invokes_rect_for_each_segment():
    main.game_display = pygame.Surface((100, 100))
    coords = [[0, 0], [10, 10], [20, 20]]
    with patch("pygame.draw.rect") as mock_rect:
        main.draw_snake(10, coords)
        assert mock_rect.call_count == len(coords)
