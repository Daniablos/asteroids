import pygame

from asteroids.resolution import Resolution


class LifeDisplay:
    """Player health display"""

    def __init__(self, resolution: Resolution):
        self.font = pygame.font.Font(None, 72)
        self.resolution = resolution

    def draw(self, screen: pygame.Surface, player_lifes: int):
        """
        Draws player health count on the screen
        :param screen:
        :param player_lifes:
        :return:
        """
        text = self.font.render(f"Health: {player_lifes}", True, "white", None)
        text_rect = text.get_rect(topright=(self.resolution.width - 10, 10))
        screen.blit(text, text_rect)
