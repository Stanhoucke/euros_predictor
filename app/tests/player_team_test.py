import unittest

from models.player import Player
from models.player_team import PlayerTeam

class TestPlayerTeam(unittest.TestCase):

    def setUp(self):
        self.player_1 = Player("euros@gmail.com", "password1", "John", "Smith", "Hopp Suisse")

        self.player_team_1 = PlayerTeam(self.player_1, "Germany")

        self.group_info = {
            "played": 0,
            "won": 0,
            "drawn": 0,
            "lost": 0,
            "for": 0,
            "against": 0,
            "difference": 0,
            "points": 0,
            "rank": None
        }

    def test_player_team_has_player(self):
        self.assertEqual(self.player_1, self.player_team_1.player)

    def test_player_team_has_name(self):
        self.assertEqual("Germany", self.player_team_1.name)

    def test_player_team_has_group_info(self):
        self.assertEqual(self.group_info, self.player_team_1.group_info)