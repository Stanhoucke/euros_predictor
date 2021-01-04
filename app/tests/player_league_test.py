import unittest
from models.player import Player
from models.league import League
from models.player_league import PlayerLeague

class TestPlayerLeague(unittest.TestCase):
    def setUp(self):
        self.player_1 = Player("euros@gmail.com", "password1", "John", "Smith", "Hopp Suisse")
        self.league_1 = League("Wilton Wanderers", "1234-5678")

        self.player_league_1 = PlayerLeague(self.league_1, self.player_1)

    def test_player_league_has_player(self):
        self.assertEqual(self.player_1, self.player_league_1.player)

    def test_player_league_has_league(self):
        self.assertEqual(self.league_1, self.player_league_1.league)