import pygame

from asteroids.constants import FONT_SIZE

class ScoreDisplay:
    """Score display"""

    def __init__(self):
        self.font = pygame.font.Font(None, FONT_SIZE)
        self.position: tuple[int, int] = (10, 10)

    def draw(self, screen: pygame.Surface, score: int) -> None:
        """
        Draws score on the screen
        :param screen:
        :param score:
        :return:
        """
        text = self.font.render(f"{score}", True, "white", None)
        screen.blit(text, self.position)
