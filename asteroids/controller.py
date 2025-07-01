import typing
import random
import pygame

from asteroids import entities
from asteroids.entities import Asteroid
from asteroids.constants import ASTEROID_MIN_RADIUS, PLAYER_SHOOT_SPEED
from .entities import Shot


class GameController:
    def __init__(self):
        self.event = 0
        self.paused = False

    def on_asteroid_kill(
        self, asteroid: entities.Asteroid, shot: entities.Shot
    ) -> None:
        """
        Checks for asteroid splitting and creates asteroid shards.
        :param asteroid:
        :param shot:
        :return:
        """
        if asteroid.split():
            random_angle = random.uniform(20, 50)
            angle1 = asteroid.velocity.rotate(random_angle)
            angle2 = asteroid.velocity.rotate(-random_angle)
            new_radius = asteroid.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(
                asteroid.position.x, asteroid.position.y, new_radius, asteroid.groups
            )
            asteroid2 = Asteroid(
                asteroid.position.x, asteroid.position.y, new_radius, asteroid.groups
            )
            asteroid1.velocity = angle1 * 1.2
            asteroid2.velocity = angle2 * 1.2
        shot.kill()

    def on_shoot(self, player: entities.Player):
        """
        Creates shot.
        :param player:
        :return:
        """
        shot = Shot(player.position.x, player.position.y, *player.shot_group)
        shot.velocity = player.rotation * PLAYER_SHOOT_SPEED

    def update(
        self,
        player: entities.Player,
        asteroids: typing.Iterable[entities.Asteroid],
        shots: typing.Iterable[entities.Shot],
        delta_time: float
    ) -> None:
        """
        Checks for collisions between asteroids, players, shots and keystrokes.
        :param player:
        :param asteroids:
        :param shots:
        :param delta_time:
        :return:
        """
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_a]:
            player.rotate(-delta_time)
        if keys[pygame.K_d]:
            player.rotate(delta_time)
        if keys[pygame.K_w]:
            player.move(delta_time)
        if keys[pygame.K_s]:
            player.move(-delta_time)
        if keys[pygame.K_SPACE]:
            if player.shoot():
                self.on_shoot(player)

        for asteroid in asteroids:
            for shot in shots:
                if shot.collision(asteroid):
                    self.on_asteroid_kill(asteroid, shot)
            if asteroid.collision(player):
                self.event = 1
