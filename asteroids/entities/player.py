import pygame

from asteroids.constants import (
    PLAYER_RADIUS,
    PLAYER_TURN_SPEED,
    PLAYER_SHOOT_SPEED,
    PLAYER_SHOOT_COOLDOWN,
    PLAYER_SPEED,
)
from .circleshape import CircleShape
from .shot import Shot

__all__ = ['Player']


class Player(CircleShape):
    """
    Player entity.
    """
    __slots__ = ['timer', 'shot_group']

    def __init__(self,
                 x: float, y: float,
                 shot_group: tuple[pygame.sprite.Group, ...],
                 *groups: pygame.sprite.Group):
        super().__init__(x, y, PLAYER_RADIUS, *groups)
        self.timer: float = 0
        """Player shooting cooldown timer"""
        self.shot_group = shot_group
        """Entity groups for bullet creation"""

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

    def shoot(self) -> None:
        """
        Shoots the bullet from the player.

        TODO: extract bullet creation from the player.
        TODO: Player should only know about itself
        TODO: Player may include reload timer and other shooting related info, but bullet creation must be outside.
        :return:
        """
        shot = Shot(self.position.x, self.position.y, *self.shot_group)
        shot.velocity = self.rotation * PLAYER_SHOOT_SPEED

    def update(self, delta_time: float) -> None:
        """
        Updates the player.
        :param delta_time:
        :return:
        """
        keys = pygame.key.get_pressed()
        self.timer -= delta_time

        # TODO: Extract controls to a settings object (may be global variable).
        if keys[pygame.K_a]:
            self.rotate(-delta_time)
        if keys[pygame.K_d]:
            self.rotate(delta_time)
        if keys[pygame.K_w]:
            self.move(delta_time)
        if keys[pygame.K_s]:
            self.move(-delta_time)
        # TODO: Extract shooting logic outside the player class.
        if keys[pygame.K_SPACE]:
            if self.timer <= 0:
                self.shoot()
                self.timer = PLAYER_SHOOT_COOLDOWN
