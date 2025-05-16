"""Render the simulation world each frame."""

from typing import List

import pygame

from body import Body


# ---------------------------------------------------------------------
def render_frame(screen: pygame.Surface,
                 bodies: List[Body],
                 width: int,
                 height: int,
                 scale: float,
                 caption: str) -> None:
    screen.fill((10, 10, 30))          # space background
    for b in bodies:
        b.draw(screen, width, height, scale)
    pygame.display.set_caption(caption)
    pygame.display.flip()
