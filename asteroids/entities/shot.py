import pygame

from asteroids.constants import SHOT_RADIUS
from .circleshape import CircleShape

__all__ = ['Shot']


class Shot(CircleShape):
    """
    Bullet entity.
    """
    __slots__ = ['velocity']

    def __init__(self, x: float, y: float, *groups: pygame.sprite.Group):
        super().__init__(x, y, SHOT_RADIUS, *groups)
        self.velocity = pygame.Vector2(0, 1)
        """Direction and speed of a bullet"""

    def draw(self, screen: pygame.Surface) -> None:
        """
        Draw the shot.
        :param screen:
        :return:
        """
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, delta_time: float) -> None:
        """
        Update the shot.
        :param delta_time:
        :return:
        """
        self.position += self.velocity * delta_time
