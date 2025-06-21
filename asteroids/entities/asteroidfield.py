import random
import typing

import pygame

from asteroids.constants import (
    ASTEROID_MAX_RADIUS,
    ASTEROID_MIN_RADIUS,
    ASTEROID_SPAWN_RATE,
    ASTEROID_KINDS,
)
from asteroids.resolution import Resolution
from .asteroid import Asteroid

__all__ = ['AsteroidField']


class AsteroidField(pygame.sprite.Sprite):
    """
    Controller that spawns and destroys asteroids withing the set BB.
    """
    __slots__ = ['asteroid_group', 'spawn_timer', 'edges']

    def __init__(self, asteroid_group: tuple[pygame.sprite.Group, ...], *field_groups: pygame.sprite.Group):
        super().__init__(*field_groups)
        res = Resolution.info()
        self.asteroid_group = asteroid_group
        """Entity group for asteroid creation"""
        self.spawn_timer = 0.0
        """Cooldown timer for asteroid creation"""
        self.edges: list[tuple[pygame.Vector2, typing.Callable[[float], pygame.Vector2]]] = [
            (
                pygame.Vector2(1, 0),
                lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * res.height),
            ),
            (
                pygame.Vector2(-1, 0),
                lambda y: pygame.Vector2(res.width + ASTEROID_MAX_RADIUS, y * res.height),
            ),
            (
                pygame.Vector2(0, 1),
                lambda x: pygame.Vector2(x * res.width, -ASTEROID_MAX_RADIUS),
            ),
            (
                pygame.Vector2(0, -1),
                lambda x: pygame.Vector2(x * res.width, res.height + ASTEROID_MAX_RADIUS),
            ),
        ]
        """List of spawn positions and velocities for asteroid creation"""

    def spawn(self, radius: float, position: pygame.Vector2, velocity: pygame.Vector2) -> None:
        """
        Spawns a new asteroid.
        :param radius:
        :param position:
        :param velocity:
        :return:
        """
        asteroid = Asteroid(position.x, position.y, radius, *self.asteroid_group)
        asteroid.velocity = velocity

    def update(self, delta_time: float) -> None:
        """
        Updates the asteroid field by spawning the asteroids.
        :param delta_time:
        :return:
        """
        self.spawn_timer += delta_time
        if self.spawn_timer <= ASTEROID_SPAWN_RATE:
            return

        self.spawn_timer = 0

        # spawn a new asteroid at a random edge
        edge: tuple[pygame.Vector2, typing.Callable[[float], pygame.Vector2]] = random.choice(self.edges)
        speed = random.randint(40, 100)
        velocity = edge[0] * speed
        velocity = velocity.rotate(random.randint(-30, 30))
        position = edge[1](random.uniform(0, 1))
        kind = random.randint(1, ASTEROID_KINDS)
        self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity)
