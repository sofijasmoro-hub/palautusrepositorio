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
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_loytaa_pelaajan(self):
        self.assertEqual(self.stats.search("Kurri").name, "Kurri")

    def test_search_palauttaa_none_jos_ei_loydy(self):
        self.assertIsNone(self.stats.search("Selanne"))

    def test_team_palauttaa_joukkueen_pelaajat(self):
        names = [p.name for p in self.stats.team("EDM")]
        self.assertEqual(sorted(names), ["Gretzky", "Kurri", "Semenko"])

    def test_top_oletuksena_pisteiden_mukaan(self):
        self.assertEqual(self.stats.top(1)[0].name, "Gretzky")

    def test_top_pisteiden_mukaan(self):
        self.assertEqual(self.stats.top(1, SortBy.POINTS)[0].name, "Gretzky")

    def test_top_maalien_mukaan(self):
        self.assertEqual(self.stats.top(1, SortBy.GOALS)[0].name, "Lemieux")

    def test_top_syottojen_mukaan(self):
        self.assertEqual(self.stats.top(1, SortBy.ASSISTS)[0].name, "Gretzky")
