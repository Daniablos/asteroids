class Scoring:
    """Score system"""

    def __init__(self):
        """Score counter"""
        self.score: int = 0

        """Timer for adding points"""
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
        self.score += 100

    def get_score(self) -> int:
        """
        Returns score
        :return:
        """
        return self.score
