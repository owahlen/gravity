"""
Run the gravity simulation (Pygame main loop).

Key bindings
------------
LMB – pause / resume
Esc – quit
F11 – toggle fullscreen
"""

from __future__ import annotations

import pygame

from body import Body
from constants import WIDTH, HEIGHT, FPS, SCALE, TIME_STEP
from events import handle_events
from integrator import update_physics
from renderer import render_frame
from state import AppState


# ────────────────────────────────────────────────────────────────────────────────
#  Helpers
# ────────────────────────────────────────────────────────────────────────────────
def create_bodies() -> list[Body]:
    """Return two stars in a mildly elliptical orbit."""
    return [
        Body(  # Sun-like
            2.0e30,  # kg (≈ Sun)
            (-7.5e10, 0),  # m
            (0, -14_000),  # m/s
            (255, 200, 0),  # yellow-orange
            10
        ),
        Body(  # 0.5 M☉
            1.0e30,  # kg (≈ 0.5 M☉)
            (7.5e10, 0),  # m
            (0, 28_000),  # m/s
            (0, 180, 255),  # blue
            8
        ),
    ]


# ---------------------------------------------------------------------
def main() -> None:
    pygame.init()

    bodies = create_bodies()
    state = AppState(WIDTH, HEIGHT, pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE))
    clock = pygame.time.Clock()

    while True:
        # 1) Handle input / window events
        state = handle_events(state)

        # 2) Update physics
        if not state.paused:
            update_physics(bodies, TIME_STEP)

        # 3) Render
        render_frame(
            state.screen,
            bodies,
            state.width,
            state.height,
            SCALE,
            f"Pause: LMB | Δt={TIME_STEP}s | FPS={int(clock.get_fps())}"
        )

        clock.tick(FPS)


# ---------------------------------------------------------------------
if __name__ == "__main__":
    main()
