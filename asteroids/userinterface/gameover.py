import pygame

from asteroids.resolution import Resolution
from asteroids.constants import FONT_SIZE


class GameOver:
    """Game over display"""

    def __init__(self, resolution: Resolution):
        self.font = pygame.font.Font(None, FONT_SIZE)
        self.resolution = resolution
        """Resolution info"""

    def draw(self, screen: pygame.Surface, score) -> None:
        """
        Draws 'game over' text
        :param screen:
        :param score:
        :return:
        """
        text = self.font.render(
            f"Game over! Your score is {score}! Restart? (Y/N)", True, "Grey", None
        )
        textRect = text.get_rect(center=(self.resolution.width / 2, self.resolution.height / 2))
        screen.blit(text, textRect)
