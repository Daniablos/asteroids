"""
Модуль системы подсчета очков и хранения рекордов.

Обеспечивает отслеживание текущего счета игрока, логику начисления баллов 
за время и уничтожение целей, а также взаимодействие с SQLite базой данных 
для хранения таблицы лидеров.
"""

import sqlite3


class Scoring:
    """Score system"""

    def __init__(self) -> None:
        self.score: int = 0
        """Score counter"""
        self.time: float = 0
        """Timer for adding points"""
        self.conn_db = sqlite3.connect("game_data.db")
        """Создает и/или соединяется с базой данных."""
        self.cursor = self.conn_db.cursor()
        """Инструмент для ввода SQL команд."""
        #Инициализация таблицы
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS high_scores (
                player_name TEXT NOT NULL,
                score INTEGER NOT NULL
            )
        """)

        self.conn_db.commit()

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

    def add_high_score(self, name: str, score: int) -> None:
        """
        Добавление рекорда в таблицу рекордов
        """
        self.cursor.execute(
            "INSERT INTO high_scores (player_name, score) VALUES (?, ?)", (name, score)
        )
        self.conn_db.commit()

    def get_highest_score(self) -> int:
        """
        Извлечение лучшего результата из таблицы рекордов
        """
        self.cursor.execute("SELECT score FROM high_scores ORDER BY score DESC LIMIT 1")
        result = self.cursor.fetchall()
        return result[0][0] if result else 0

    def get_leaderboard(self, limit=3) -> list[tuple]:
        """
        Извлечение лучших результатов из таблицы рекордов
        """
        self.cursor.execute(
            "SELECT player_name, score FROM high_scores ORDER BY score DESC LIMIT ?",
            (limit,),
        )
        return self.cursor.fetchall()
