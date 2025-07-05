import pygame

from asteroids.resolution import Resolution
from asteroids.constants import FONT_SIZE


class HealthDisplay:
    """Player health display"""

    def __init__(self, resolution: Resolution):
        self.font = pygame.font.Font(None, FONT_SIZE)
        self.resolution = resolution
        """Resolution info"""

    def draw(self, screen: pygame.Surface, player_health: int):
        """
        Draws player health count on the screen
        :param screen:
        :param player_lifes:
        :return:
        """
        text = self.font.render(f"Health: {player_health}", True, "white", None)
        text_rect = text.get_rect(topright=(self.resolution.width - 10, 10))
        screen.blit(text, text_rect)
