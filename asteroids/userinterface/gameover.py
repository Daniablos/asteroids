import pygame

from asteroids.resolution import Resolution
from asteroids.constants import FONT_SIZE


class GameOver:
    """Game over display"""

    def __init__(self, resolution: Resolution, leaderboard: list[tuple]):
        self.font = pygame.font.Font(None, FONT_SIZE)
        self.resolution = resolution
        """Resolution info"""
        self.leaderboard = leaderboard
        """Таблица рекордов"""

    def draw(self, screen: pygame.Surface, score: int) -> None:
        """
        Отрисовывает экран game over с таблицей рекордов
        :param screen:
        :param score:
        :return:
        """
        text = self.font.render(
            f"Game over! Your score is {score}! Restart? (Y/N)", True, "white", None
        )
        textRect = text.get_rect(center=(self.resolution.width / 2, self.resolution.height / 2 - 60))
        screen.blit(text, textRect)

        header = self.font.render("HIGH SCORES", True, "gold")
        header_rect = header.get_rect(centerx=self.resolution.width//2, y=textRect.bottom + 20)
        screen.blit(header, header_rect)

        line_h = self.font.get_linesize() + 2
        y = header_rect.bottom + 10
        for idx, (name, sc) in enumerate(self.leaderboard, 1):
            line = f"{idx}. {name:<12} {sc}"
            img  = self.font.render(line, True, "white")
            rect = img.get_rect(centerx=self.resolution.width//2, y=y)
            screen.blit(img, rect)
            y += line_h
