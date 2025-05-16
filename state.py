from __future__ import annotations
from dataclasses import dataclass
import pygame


@dataclass
class AppState:
    """All mutable UI state the event handler touches."""
    width: int
    height: int
    screen: pygame.Surface           # current render surface
    paused: bool = False
    fullscreen: bool = False
