import pygame

from asteroids.controller import GameController
from asteroids.constants import FULLSCREEN
from asteroids.entities import AsteroidField, Player
from asteroids.resolution import Resolution


def main():
    pygame.init()
    res = Resolution.info()
    print("Starting Asteroids!")
    print(f"Screen width: {res.width}")
    print(f"Screen height: {res.height}")

    flags = 0
    if FULLSCREEN:
        flags |= pygame.SCALED | pygame.FULLSCREEN

    screen = pygame.display.set_mode(res.size, flags)
    background = pygame.image.load("./asteroids/assets/background_space.jpg")
    background = pygame.transform.smoothscale(background, res.size)
    clock = pygame.time.Clock()
    dt = 0
    running = True

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    game_controller = GameController()

    player = Player(res.width / 2, res.height / 2, (shots, updatable, drawable), updatable, drawable)
    _ = AsteroidField((updatable, asteroids, drawable), updatable)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(background, (0, 0))
        updatable.update(dt)
        for i in drawable:
            i.draw(screen)
        game_controller.update(player, asteroids, shots)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
