"""Physics update step (numerical integrator)."""

import pygame

from physics import gravitational_acceleration

"""Physics update step (4-th-order symplectic Forest–Ruth integrator).

References
----------
H. Yoshida, *Phys. Lett. A* **150** (1990) 262-268.
"""

import pygame
from physics import gravitational_acceleration

# --- Forest–Ruth coefficients (order-4, time-reversible, symplectic) ----------
_ξ  = 2 ** (1 / 3)                     # cube-root of 2
w1  = 1.0 / (2.0 - _ξ)                 # 0.6756035959798288…
w2  = -_ξ / (2.0 - _ξ)                 # -0.17560359597982885…
# sequence of fractional time-steps for the DRIFT (positions) part
A   = [w1 / 2, (w1 + w2) / 2, (w2 + w1) / 2, w1 / 2]
# same length sequence for the KICK (velocities) part
B   = [w1, w2, w1]


def _compute_accels(bodies):
    """Return a list of accelerations (one vector per body)."""
    acc = []
    for i, b in enumerate(bodies):
        a = pygame.math.Vector2()
        for j, other in enumerate(bodies):
            if i == j:
                continue
            a += gravitational_acceleration(b, other)
        acc.append(a)
    return acc


# -----------------------------------------------------------------------------#
def update_physics_forest_ruth(bodies, dt):
    """
    Advance the system by one global time-step *dt* using the
    Forest–Ruth 4th-order symplectic scheme.

    The algorithm alternates:
        KICK  (update v) – coef from B
        DRIFT (update x) – coef from A
    keeping the map symplectic and time-reversible.
    """
    # initial acceleration
    acc = _compute_accels(bodies)

    # K-D-K-D-K-D-K pattern (lengths: B=3, A=4)
    for s in range(3):                       # 3 sub-kicks
        # ---- KICK -----------------------------------------------------------
        for b, a in zip(bodies, acc):
            b.vel += B[s] * dt * a

        # ---- DRIFT ----------------------------------------------------------
        for b in bodies:
            b.pos += A[s] * dt * b.vel

        # recompute acceleration except after last K
        acc = _compute_accels(bodies)

    # final DRIFT using A[3]
    for b in bodies:
        b.pos += A[3] * dt * b.vel

# -----------------------------------------------------------------------------#
def update_physics_velocity_verlet(bodies, dt: float) -> None:
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

# -----------------------------------------------------------------------------#
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

# -----------------------------------------------------------------------------#
def update_physics(bodies, dt: float) -> None:
    return update_physics_forest_ruth(bodies, dt)
