import pygame

from asteroids.resolution import Resolution


class GameOver:
    """Game over display"""

    def __init__(self, resolution: Resolution):
        self.font = pygame.font.Font(None, 50)
        """Resolution info"""
        self.resolution = resolution

    def draw(self, screen: pygame.Surface, score) -> None:
        """
        Draws 'game over' text
        :param screen:
        :param score:
        :return:
        """
        self.text = self.font.render(
            f"Game over! Your score is {score}! Restart? (Y/N)", True, "Grey", None
        )
        self.textRect = self.text.get_rect(
            center=(self.resolution.width / 2, self.resolution.height / 2)
        )

        screen.blit(self.text, self.textRect)
