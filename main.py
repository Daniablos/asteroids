import pygame
from asteroids.entities.player import Player
from asteroids.entities.asteroidfield import AsteroidField
from asteroids.resolution import Resolution
from asteroids.constants import FULLSCREEN
from asteroids.collision import handle_collisions


def main():
    pygame.init()
    res = Resolution.info()
    print("Starting Asteroids!")
    print(f"Screen width: {res.width}")
    print(f"Screen height: {res.height}")

    if FULLSCREEN:
        flags = pygame.SCALED | pygame.FULLSCREEN
    else:
        flags = 0

    screen = pygame.display.set_mode((res.width, res.height), flags)
    background = pygame.image.load("./asteroids/assets/background_space.jpg")
    background = pygame.transform.smoothscale(background, (res.width, res.height))
    clock = pygame.time.Clock()
    dt = 0
    running = True

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    player = Player(res.width / 2, res.height / 2, (shots, updatable, drawable), updatable, drawable)
    AsteroidField((updatable, asteroids, drawable), updatable)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(background, (0, 0))
        updatable.update(dt)
        for i in drawable:
            i.draw(screen)
        handle_collisions(player, asteroids, shots)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
