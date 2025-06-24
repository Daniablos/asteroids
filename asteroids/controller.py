import typing
import random

from asteroids import entities
from asteroids.entities import Asteroid
from asteroids.constants import ASTEROID_MIN_RADIUS


class GameController:
    def __init__(self):
        pass

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

    def update(
        self,
        player: entities.Player,
        asteroids: typing.Iterable[entities.Asteroid],
        shots: typing.Iterable[entities.Shot],
    ) -> None:
        """
        Checks for collisions between asteroids, players and shots.
        :param player:
        :param asteroids:
        :param shots:
        :return:
        """
        for asteroid in asteroids:
            for shot in shots:
                if shot.collision(asteroid):
                    self.on_asteroid_kill(asteroid, shot)
            if asteroid.collision(player):
                # TODO: Introduce graceful shutdown/exit.
                raise SystemExit("Game over!")
