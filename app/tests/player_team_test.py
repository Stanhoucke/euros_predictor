import unittest

from models.player_team import PlayerTeam
from models.player import Player

class TestPlayerTeam(unittest.TestCase):

    def setUp(self):
        self.player_1 = Player("euros@gmail.com", "password1", "John", "Smith", "Hopp Suisse")

        self.team_1 = PlayerTeam(self.player_1, "France")

    def test_team_has_name(self):
        self.assertEqual("France", self.team_1.name)

    def test_team_has_player(self):
        self.assertEqual(self.player_1, self.team_1.player)