import unittest

from models.player import Player
from models.player_team import PlayerTeam
from models.player_group import PlayerGroup

class TestPlayerGroup(unittest.TestCase):
    def setUp(self):
        self.player_1 = Player("euros@gmail.com", "password1", "John", "Smith", "Hopp Suisse")

        self.player_team_1 = PlayerTeam(self.player_1, "France")
        self.player_team_1.group_info = {
            "played": 1,
            "won": 0,
            "drawn": 1,
            "lost": 0,
            "for": 2,
            "against": 2,
            "difference": 0,
            "points": 1,
            "rank": None
        }
        self.player_team_2 = PlayerTeam(self.player_1, "Germany")
        self.player_team_2.group_info = {
            "played": 1,
            "won": 0,
            "drawn": 1,
            "lost": 0,
            "for": 2,
            "against": 2,
            "difference": 0,
            "points": 1,
            "rank": None
        }
        self.player_team_3 = PlayerTeam(self.player_1, "Hungary")
        self.player_team_3.group_info = {
            "played": 1,
            "won": 0,
            "drawn": 0,
            "lost": 1,
            "for": 1,
            "against": 3,
            "difference": -2,
            "points": 0,
            "rank": None
        }
        self.player_team_4 = PlayerTeam(self.player_1, "Portugal")
        self.player_team_4.group_info = {
            "played": 1,
            "won": 1,
            "drawn": 0,
            "lost": 0,
            "for": 3,
            "against": 1,
            "difference": 2,
            "points": 3,
            "rank": None
        }

        self.group_1 = PlayerGroup(self.player_1, "F")
        self.group_1.player_teams = [self.player_team_1, self.player_team_2, self.player_team_3, self.player_team_4]

    def test_group_has_player(self):
        self.assertEqual("John", self.group_1.player.first_name)

    def test_group_has_name(self):
        self.assertEqual("F", self.group_1.name)

    def test_group_has_4_teams(self):
        self.assertEqual(4, len(self.group_1.player_teams))

    def test_rank_tiebreaker_sorts_by_points(self):
        self.group_1.assign_rank()

        self.assertEqual(2, self.player_team_1.group_info["rank"])
        self.assertEqual(3, self.player_team_2.group_info["rank"])
        self.assertEqual(4, self.player_team_3.group_info["rank"])
        self.assertEqual(1, self.player_team_4.group_info["rank"])
