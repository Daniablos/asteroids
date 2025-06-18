import pygame
import random
from asteroids.entities.asteroid import Asteroid
from asteroids.constants import (
    ASTEROID_MAX_RADIUS,
    ASTEROID_MIN_RADIUS,
    ASTEROID_SPAWN_RATE,
    ASTEROID_KINDS,
)
from asteroids.resolution import Resolution


class AsteroidField(pygame.sprite.Sprite):
    def __init__(self, asteroid_groupe, *field_groups):
        super().__init__(*field_groups) 
        self.asteroid_groupe = asteroid_groupe       
        res = Resolution.info()
        self.spawn_timer = 0.0
        self.edges = [
            [
                pygame.Vector2(1, 0),
                lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * res.height),
            ],
            [
                pygame.Vector2(-1, 0),
                lambda y: pygame.Vector2(
                    res.width + ASTEROID_MAX_RADIUS, y * res.height
                ),
            ],
            [
                pygame.Vector2(0, 1),
                lambda x: pygame.Vector2(x * res.width, -ASTEROID_MAX_RADIUS),
            ],
            [
                pygame.Vector2(0, -1),
                lambda x: pygame.Vector2(
                    x * res.width, res.height + ASTEROID_MAX_RADIUS
                ),
            ],
        ]

    def spawn(self, radius, position, velocity):
        asteroid = Asteroid(position.x, position.y, radius, self.asteroid_groupe)
        asteroid.velocity = velocity

    def update(self, dt):
        self.spawn_timer += dt
        if self.spawn_timer > ASTEROID_SPAWN_RATE:
            self.spawn_timer = 0

            # spawn a new asteroid at a random edge
            edge = random.choice(self.edges)
            speed = random.randint(40, 100)
            velocity = edge[0] * speed
            velocity = velocity.rotate(random.randint(-30, 30))
            position = edge[1](random.uniform(0, 1))
            kind = random.randint(1, ASTEROID_KINDS)
            self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity)
