"""Handle all user or window events for the simulation."""

import sys

import pygame

from state import AppState


# ---------------------------------------------------------------------
def handle_events(state: AppState) -> AppState:
    """Return a *new* state instance (or mutate in place—your choice)."""
    for event in pygame.event.get():
        # Quit
        if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
        ):
            pygame.quit()
            sys.exit()

        # Pause toggle
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            state.paused = not state.paused

        # Window resize
        if event.type == pygame.VIDEORESIZE:
            state.width, state.height = event.w, event.h
            state.screen = pygame.display.set_mode(
                (state.width, state.height), pygame.RESIZABLE
            )

        # Full‑screen toggle (F11)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
            state.fullscreen = not state.fullscreen
            if state.fullscreen:
                state.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            else:
                state.screen = pygame.display.set_mode(
                    (state.width, state.height), pygame.RESIZABLE
                )

    return state
