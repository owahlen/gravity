"""Physics update step (numerical integrator)."""

import pygame

from physics import gravitational_acceleration


# ---------------------------------------------------------------------
def update_physics(bodies, dt: float) -> None:
    """Advance all bodies by *dt* seconds using Euler integration."""
    for i, b in enumerate(bodies):
        a_total = pygame.math.Vector2()
        for j, other in enumerate(bodies):
            if i == j:
                continue
            a_total += gravitational_acceleration(b, other)
        b.vel += a_total * dt
        b.pos += b.vel * dt
