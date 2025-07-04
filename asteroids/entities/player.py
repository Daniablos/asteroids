import pygame

from asteroids.constants import (
    PLAYER_RADIUS,
    PLAYER_TURN_SPEED,
    PLAYER_SHOOT_COOLDOWN,
    PLAYER_SPEED,
)
from .circleshape import CircleShape

__all__ = ["Player"]


class Player(CircleShape):
    """
    Player entity.
    """

    __slots__ = ["timer", "shot_group"]

    def __init__(
        self,
        x: float,
        y: float,
        shot_group: tuple[pygame.sprite.Group, ...],
        *groups: pygame.sprite.Group,
    ):
        super().__init__(x, y, PLAYER_RADIUS, *groups)
        self.timer: float = 0
        """Player shooting cooldown timer"""
        self.shot_group = shot_group
        """Entity groups for bullet creation"""
        self.life = 3
        """Player's life count"""

    def triangle(self) -> tuple[pygame.Vector2, pygame.Vector2, pygame.Vector2]:
        """
        Calculates vertices of the triangle shape representing the player.
        :return:
        """
        forward = self.rotation
        right = self.rotation.rotate(90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right

        return a, b, c

    def get_life(self) -> int:
        """
        Returns player health
        :return:
        """
        return self.life

    def lose_life(self) -> None:
        """
        Substracts player health
        :return:
        """
        self.life -= 1

    def is_alive(self) -> bool:
        """
        Check player health
        :return:
        """
        if self.life == 0:
            return False
        return True

    def draw(self, screen: pygame.Surface) -> None:
        """
        Draws the player on the screen.
        :param screen:
        :return:
        """
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, delta_time: float) -> None:
        """
        Rotates the player direction.
        :param delta_time:
        :return:
        """
        self.rotation = self.rotation.rotate(PLAYER_TURN_SPEED * delta_time)

    def move(self, delta_time: float) -> None:
        """
        Moves the player.
        :param delta_time:
        :return:
        """
        forward = self.rotation
        self.position += forward * PLAYER_SPEED * delta_time

    def shoot(self) -> bool:
        """
        Checks and updates the player timer.
        :return:
        """
        if self.timer == 0:
            self.timer = PLAYER_SHOOT_COOLDOWN
            return True
        return False

    def update(self, delta_time: float) -> None:
        """
        Updates the player timer.
        :param delta_time:
        :return:
        """
        self.timer = max(self.timer - delta_time, 0)
