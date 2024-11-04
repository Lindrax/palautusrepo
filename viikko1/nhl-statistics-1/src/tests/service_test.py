import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_lsearch(self):
        result = self.stats.search('Lemieux')
        self.assertEqual(result.name, 'Lemieux')
    
    def test_searc_none(self):
        result = self.stats.search("Unknown")
        self.assertIsNone(result)
    
    def test_team(self):
        players = self.stats.team("EDM")
        names = [player.name for player in players]
        self.assertListEqual(names, ["Semenko", "Kurri", "Gretzky"])
    
    def test_goals(self):
        players = self.stats.top(3, SortBy.GOALS)
        names = [player.name for player in players]
        self.assertListEqual(names, ["Lemieux", "Yzerman", "Kurri"])

    def test_assists(self):
        players = self.stats.top(3, SortBy.ASSISTS)
        names = [player.name for player in players]
        self.assertListEqual(names, ["Gretzky", "Yzerman", "Lemieux"])

    def test_default(self):
        players = self.stats.top(3)
        names = [player.name for player in players]
        self.assertListEqual(names, ["Gretzky", "Lemieux", "Yzerman"])
    def test_default(self):
        players = self.stats.top(3)
        names = [player.name for player in players]
        self.assertListEqual(names, ["Gretzky", "Lemieux", "Yzerman"])

    def test_defa(self):
        players = self.stats.top(3, "lol")
        names = [player.name for player in players]
        self.assertListEqual(names, ["Gretzky", "Lemieux", "Yzerman"])