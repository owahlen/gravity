"""Physics helpers (gravity)."""

from pygame.math import Vector2

from body import Body
from constants import G


# ---------------------------------------------------------------------
def gravitational_acceleration(body1: Body, body2: Body) -> Vector2:
    """Acceleration **on body1** caused by **body2** (vector)."""
    result_vector = body2.pos - body1.pos
    distance_squared = result_vector.length_squared()
    if distance_squared == 0:
        return Vector2()
    return G * body2.m / distance_squared * result_vector.normalize()
