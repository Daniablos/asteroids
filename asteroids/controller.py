import random
import pygame

from asteroids.resolution import Resolution
from asteroids import entities
from asteroids.entities import Asteroid
from asteroids.constants import ASTEROID_MIN_RADIUS, PLAYER_SHOOT_SPEED
from .entities import Shot, Player, AsteroidField
from .systems import Scoring
from .userinterface import GameOver, ScoreDisplay, LifeDisplay

GAME_RUNNING_STATE = 0
GAME_OVER_STATE = 1


class GameController:
    def __init__(self, screen: pygame.Surface, resolution: Resolution):
        self.init()
        self.screen = screen
        self.resolution = resolution


    def init(self):
        """Groups for game objects"""
        self.updatable = pygame.sprite.Group()
        self.drawable = pygame.sprite.Group()
        self.asteroids = pygame.sprite.Group()
        self.shots = pygame.sprite.Group()
        """State of the game"""
        self.state = GAME_RUNNING_STATE

    def ui_init(self):
        """
        User interface initialization
        :return:
        """
        self.score_display = ScoreDisplay()
        self.game_over = GameOver(self.resolution)
        self.life_display = LifeDisplay(self.resolution)


    def systems_init(self) -> None:
        """
        Score system initialization
        :return:
        """
        self.scoring = Scoring()


    def spawn_player(self) -> None:
        """
        Spawns player at center of screen
        :return:
        """
        self.player = Player(
            self.resolution.width / 2,
            self.resolution.height / 2,
            (self.shots, self.updatable, self.drawable),
            self.updatable,
            self.drawable,
        )

    def spawn_asteroid_field(self) -> None:
        """
        Spawns asteroid field
        :return:
        """
        self.asteroid_field = AsteroidField(
            (self.updatable, self.asteroids, self.drawable), self.updatable
        )

    def clear(self) -> None:
        """
        Clears screen from entities and resets score
        :return:
        """
        self.scoring.score = 0
        self.player.kill()
        for asteroid in self.asteroids:
            asteroid.kill()
        for shot in self.shots:
            shot.kill()

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

    def on_shoot(self, player: entities.Player) -> None:
        """
        Creates shot.
        :param player:
        :return:
        """
        shot = Shot(player.position.x, player.position.y, *player.shot_group)
        shot.velocity = player.rotation * PLAYER_SHOOT_SPEED

    def draw(self, screen: pygame.Surface) -> None:
        """
        Draws entities and UI on the screen
        :param screen:
        :return:
        """
        self.life_display.draw(screen, self.player.get_life())
        self.score_display.draw(screen, self.scoring.get_score())
        for entity in self.drawable:
            entity.draw(screen)

        if self.state == GAME_OVER_STATE:
            self.game_over.draw(screen, self.scoring.score)
            

    def update(self, delta_time: float) -> bool:
        """
        Updates entities, entity collision, systems and game state
        :param delta_time:
        :return:
        """

        keys = pygame.key.get_pressed()

        if self.state == GAME_RUNNING_STATE:
            self.scoring.update(delta_time)
            # player movement and shooting
            self.updatable.update(delta_time)
            if keys[pygame.K_a]:
                self.player.rotate(-delta_time)
            if keys[pygame.K_d]:
                self.player.rotate(delta_time)
            if keys[pygame.K_w]:
                self.player.move(delta_time)
            if keys[pygame.K_s]:
                self.player.move(-delta_time)
            if keys[pygame.K_SPACE]:
                if self.player.shoot():
                    self.on_shoot(self.player)

            # collision detection
            for asteroid in self.asteroids:
                for shot in self.shots:
                    if shot.collision(asteroid):
                        self.scoring.add_points_kill()
                        self.on_asteroid_kill(asteroid, shot)
                if asteroid.collision(self.player):             
                    if self.player.is_alive():
                        self.player.lose_life()
                        asteroid.kill()
                    else: 
                        self.state = GAME_OVER_STATE

        if self.state == GAME_OVER_STATE:
            # restart
            if keys[pygame.K_y]:
                self.clear()
                self.spawn_player()
                self.state = GAME_RUNNING_STATE

            # quit
            if keys[pygame.K_n]:
                return False
        return True
