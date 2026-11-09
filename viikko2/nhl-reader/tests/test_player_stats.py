import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

# pylint: disable=wrong-import-position
from player import Player
from player_stats import PlayerStats


class PlayerReaderStub:
    def __init__(self, players):
        self.players = players

    def get_players(self):
        return self.players


class TestPlayerStats(unittest.TestCase):
    def setUp(self):
        self.players = [
            Player({
                "name": "Player One",
                "nationality": "FIN",
                "team": "AAA",
                "goals": 10,
                "assists": 20,
            }),
            Player({
                "name": "Player Two",
                "nationality": "CAN",
                "team": "BBB",
                "goals": 30,
                "assists": 5,
            }),
            Player({
                "name": "Player Three",
                "nationality": "FIN",
                "team": "AAA",
                "goals": 15,
                "assists": 10,
            }),
        ]
        self.stats = PlayerStats(PlayerReaderStub(self.players))

    def test_top_scorers_by_nationality_returns_matching_players_by_points(self):
        result = self.stats.top_scorers_by_nationality("FIN")

        self.assertEqual(["Player One", "Player Three"],
                         [player.name for player in result])

    def test_top_scorers_by_team_returns_matching_players_by_points(self):
        result = self.stats.top_scorers_by_team("AAA")

        self.assertEqual(["Player One", "Player Three"],
                         [player.name for player in result])

    def test_top_goal_scorers_returns_requested_number_by_goals(self):
        result = self.stats.top_goal_scorers(2)

        self.assertEqual(["Player Two", "Player Three"],
                         [player.name for player in result])

    def test_top_goal_scorers_returns_empty_list_when_count_is_zero(self):
        self.assertEqual([], self.stats.top_goal_scorers(0))


if __name__ == "__main__":
    unittest.main()
