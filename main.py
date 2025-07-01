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
    screen_center = (res.width / 2, res.height / 2)
    font = pygame.font.Font(None, 32)
    game_over_text = font.render('Game over! Restart? (Y/N)', True, "white", None)
    game_over_textRect = game_over_text.get_rect()
    game_over_textRect.center = screen_center
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


    player = Player(screen_center[0], screen_center[1], (shots, updatable, drawable), updatable, drawable)
    _ = AsteroidField((updatable, asteroids, drawable), updatable)


    while running:
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(background, (0, 0))
        if not game_controller.paused:
            updatable.update(dt)
            game_controller.update(player, asteroids, shots, dt)
        for i in drawable:
            i.draw(screen)

        #Game over event
        if game_controller.event == 1:
            game_controller.paused = True
            screen.blit(game_over_text, game_over_textRect)
            if keys[pygame.K_y]:
                player.position = screen_center
                player.rotation = pygame.Vector2(0, 1)
                for asteroid in asteroids:
                    asteroid.kill()
                for shot in shots:
                    shot.kill()
                game_controller.event = 0
                game_controller.paused = False
            if keys[pygame.K_n]:
                running = False
                
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
