import pygame


class ScoreDisplay:
    """Score display"""

    def __init__(self):
        self.font = pygame.font.Font(None, 72)
        self.position: tuple[int, int] = (10, 10)

    def draw(self, screen: pygame.Surface, score: int) -> None:
        """
        Draws score on the screen
        """
        text = self.font.render(f"{score}", True, "white", None)
        screen.blit(text, self.position)
