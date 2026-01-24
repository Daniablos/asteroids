import pygame

from asteroids.resolution import Resolution
from asteroids.constants import FONT_SIZE

ALLOWED = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
MAX_LEN = 3

class HighScore:
    """
    Объект для записи нового рекорда.
    """
    def __init__(self, resolution: Resolution):
        self.font = pygame.font.Font(None, FONT_SIZE)
        self.resolution = resolution
        """Resolution info"""
        self.name = ""
        """Переменная для ввода имени"""
        self.done = False
        """Переменная для проверки нажатия return_button"""

    def draw(self, screen: pygame.Surface, score: int) -> None:
        """
        Отрисовывает текст с уведомлением о новом рекорде и ввод имени.
        """
        # заголовок
        header = self.font.render("NEW HIGH SCORE!", True, "gold")
        header_rect = header.get_rect(centerx=self.resolution.width//2, y=100)
        screen.blit(header, header_rect)

        # счёт
        score_img = self.font.render(f"Score: {score}", True, "white")
        score_rect = score_img.get_rect(centerx=self.resolution.width//2, y=160)
        screen.blit(score_img, score_rect)

        # строка ввода с мигающим курсором
        cursor = "_" if (pygame.time.get_ticks() // 500) % 2 else " "
        line = self.font.render(self.name + cursor, True, "green")
        line_rect = line.get_rect(center=(self.resolution.width//2, 240))
        screen.blit(line, line_rect)

        # подсказка
        prompt = self.font.render("Press ENTER when ready", True, "grey")
        prompt_rect = prompt.get_rect(centerx=self.resolution.width//2, y=280)
        screen.blit(prompt, prompt_rect)

    def update(self, events: list[pygame.event.Event]) -> None:
        """Обработка нажатия клавиш для написания имени игрока"""
        for event in events:
            if event.type != pygame.KEYDOWN:
                continue
            if event.key == pygame.K_BACKSPACE:
                self.name = self.name[:-1]
            elif event.key == pygame.K_RETURN:
                self.done = True
            else:
                ch = event.unicode.upper()
                if ch in ALLOWED and len(self.name) < MAX_LEN:
                    self.name += ch