import typing

from asteroids import entities


class GameController:
    def __init__(self):
        pass
        

    def update(
            player: entities.Player,
            asteroids: typing.Iterable[entities.Asteroid],
            shots: typing.Iterable[entities.Shot]) -> None:
        """
        Checks for collisions between asteroids, players and shots.
        :param player:
        :param asteroids:
        :param shots:
        :return:
        """
        for a in asteroids:
            for s in shots:
                if s.collision(a):
                    a.split()
                    s.kill()
            if a.collision(player):
                # TODO: Introduce graceful shutdown/exit.
                raise SystemExit("Game over!")
