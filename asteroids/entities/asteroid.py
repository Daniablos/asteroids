import random

import pygame

from asteroids.constants import ASTEROID_MIN_RADIUS
from .circleshape import CircleShape

__all__ = ['Asteroid']


class Asteroid(CircleShape):
    """
    Asteroid entity.
    """
    __slots__ = ['velocity']

    def __init__(self, x: float, y: float, radius: float, *groups: pygame.sprite.Group):
        super().__init__(x, y, radius, *groups)
        self.velocity = pygame.Vector2(0, 0)
        """Speed and direction of an asteroid"""

    def split(self):
        """
        Destroys the asteroid and creates asteroid shards.
        TODO: Extract asteroid creation outside the asteroid entity class.
        TODO: Asteroid should not know how to spawn another object.
        TODO: Asteroid may contain information that would be helpful for Controller objects to reason about splitting.
        :return:
        """
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)
        angle1 = self.velocity.rotate(random_angle)
        angle2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

        asteroid1.velocity = angle1 * 1.2
        asteroid2.velocity = angle2 * 1.2

    def draw(self, screen: pygame.Surface) -> None:
        """
        Draws the asteroid on the screen.
        :param screen:
        :return:
        """
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, delta_time: float) -> None:
        """
        Updates the asteroid.
        :param delta_time:
        :return:
        """
        self.position += self.velocity * delta_time
