import pygame

from asteroids.controller import GameController
from asteroids.constants import FULLSCREEN
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
    # initialization
    game_controller = GameController(screen, res)
    game_controller.spawn_player()
    game_controller.spawn_asteroid_field()
    game_controller.ui_init()
    game_controller.systems_init()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(background, (0, 0))
        if not game_controller.update(dt):
            running = False
        game_controller.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
