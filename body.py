"""Renderable point‑mass body."""
from pygame import Surface
from pygame.draw import circle
from pygame.math import Vector2


class Body:
    """A point mass represented as a colored circle."""

    def __init__(self,
                 mass: float, # mass in kg
                 pos: tuple[float, float], # 2D position vector in m
                 vel: tuple[float, float], # 2D velocity vector in m/s
                 color: tuple[int, int, int], # RGB color of circle
                 radius_px: int = 6 # radius in pixels
                 ) -> None:
        self.m = mass  # kg
        self.pos = Vector2(pos)  # m
        self.vel = Vector2(vel)  # m/s
        self.color = color
        self.r_px = radius_px

    # -----------------------------------------------------------------
    def draw(self, surface: Surface, width: int, height: int, scale: float) -> None:
        """Draw the body at its current position."""
        screen_x = int(width / 2 + self.pos.x * scale)
        screen_y = int(height / 2 - self.pos.y * scale)
        circle(surface, self.color, (screen_x, screen_y), self.r_px)
