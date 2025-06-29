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
        self.groups = groups
        """Speed and direction of an asteroid"""

    def split(self) -> bool:
        """
        Destroys the asteroid and checks asteroid radius.
        :return:
        """
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return False
        return True

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
