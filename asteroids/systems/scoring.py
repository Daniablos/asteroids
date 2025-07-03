import pygame


class Scoring():
    """Score system"""
    def __init__(self):
        self.score: int = 0
        self.font = pygame.font.Font(None, 72)
        self.time: float = 0

    def update(self, delta_time: float) -> None:
        """
        Updates score by time
        :param delta_time:
        :return:
        """
        self.time += delta_time
        if self.time >= 1:
            self.time = 0
            self.score += 10
        

    def add_points_kill(self) -> None:
        """
        Adds points
        :return:
        """
        self.score +=100

    def draw(self, screen: pygame.Surface) -> None:
        """
        Draws score on the screen
        :param screen:
        :return:
        """
        self.text = self.font.render(
            f"{round(self.score)}", True, "white", None
        )
        screen.blit(self.text, (0, 0))

        
