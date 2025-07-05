class Scoring:
    """Score system"""

    def __init__(self):      
        self.score: int = 0
        """Score counter"""
        self.time: float = 0
        """Timer for adding points"""

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
        Adds points for destroying asteroids to the score counter.
        :return:
        """
        self.score += 100

