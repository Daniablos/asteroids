"""Главный модуль игры Asteroids: инициализация pygame и запуск игрового цикла."""

import pygame

from asteroids.controller import GameController
from asteroids.constants import FULLSCREEN
from asteroids.resolution import Resolution


def main():
    """
    Главная функция игры Asteroids.

    Выполняет:
    - инициализацию pygame;
    - получение и вывод информации о разрешении экрана;
    - настройку окна (оконный или полноэкранный режим);
    - загрузку и масштабирование фонового изображения;
    - создание игрового контроллера и запуск игрового цикла.

    Во время работы цикла:
    - обрабатываются события (например, закрытие окна);
    - обновляется состояние игры;
    - отрисовываются кадры с частотой 60 FPS.

    При выходе из цикла игра корректно завершается.
    """
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
    game_controller.start()

    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
        screen.blit(background, (0, 0))
        if not game_controller.update(dt, events):
            running = False
        game_controller.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
