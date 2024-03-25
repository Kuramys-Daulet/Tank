class Stats():
    """Статистика"""

    def __init__(self):
        """Статистиканы іске қосатын функция"""
        self.reset_stats()
        self.run_game = True
        with open('highscore.txt', 'r') as f:
            self.high_score = int(f.readline())

    def reset_stats(self):
        """Ойын кезінде өзгеретін статистика"""
        self.tanks_left = 2
        self.score = 0

