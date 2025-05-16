"""Physics update step (numerical integrator)."""

import pygame

from physics import gravitational_acceleration


# ---------------------------------------------------------------------
def update_physics(bodies, dt: float) -> None:
    """
    Advance all bodies by *dt* seconds using a Velocity-Verlet step.

    The algorithm:
        1.  a_old = a(t)
        2.  x ← x + v·dt + ½·a_old·dt² (drift)
        3.  a_new = a(t + dt) (re-compute after drift)
        4.  v ← v + ½·(a_old + a_new)·dt (kick)

    This is time-reversible and symplectic, giving much better long-term
    stability for gravitational N-body problems than explicit Euler.
    """
    # 1) current accelerations for every body
    acc_old = []
    for i, b in enumerate(bodies):
        a = pygame.math.Vector2()
        for j, other in enumerate(bodies):
            if i == j:
                continue
            a += gravitational_acceleration(b, other)
        acc_old.append(a)

    # 2) drift: update positions using a_old
    for b, a_old in zip(bodies, acc_old):
        b.pos += b.vel * dt + 0.5 * a_old * dt * dt

    # 3) new accelerations after the drift
    acc_new = []
    for i, b in enumerate(bodies):
        a = pygame.math.Vector2()
        for j, other in enumerate(bodies):
            if i == j:
                continue
            a += gravitational_acceleration(b, other)
        acc_new.append(a)

    # 4) kick: update velocities with average of old & new acceleration
    for b, a_old, a_new in zip(bodies, acc_old, acc_new):
        b.vel += 0.5 * (a_old + a_new) * dt


def update_physics_euler(bodies, dt: float) -> None:
    """Advance all bodies by *dt* seconds using Euler integration."""
    for i, b in enumerate(bodies):
        a_total = pygame.math.Vector2()
        for j, other in enumerate(bodies):
            if i == j:
                continue
            a_total += gravitational_acceleration(b, other)
        b.vel += a_total * dt
        b.pos += b.vel * dt
