import unittest

from models.player import Player
from models.team import Team
from models.group import Group

class TestGroup(unittest.TestCase):
    def setUp(self):
        self.player_1 = Player("euros@gmail.com", "password1", "John", "Smith", "Hopp Suisse")

        self.team_1 = Team(self.player_1, "France", {
            "played": 1,
            "won": 0,
            "drawn": 1,
            "lost": 0,
            "for": 2,
            "against": 2,
            "difference": 0,
            "points": 1,
            "rank": None
        })
        self.team_2 = Team(self.player_1, "Germany", {
            "played": 1,
            "won": 0,
            "drawn": 1,
            "lost": 0,
            "for": 2,
            "against": 2,
            "difference": 0,
            "points": 1,
            "rank": None
        })
        self.team_3 = Team(self.player_1, "Hungary", {
            "played": 1,
            "won": 0,
            "drawn": 0,
            "lost": 1,
            "for": 1,
            "against": 3,
            "difference": -2,
            "points": 0,
            "rank": None
        })
        self.team_4 = Team(self.player_1, "Portugal", {
            "played": 1,
            "won": 1,
            "drawn": 0,
            "lost": 0,
            "for": 3,
            "against": 1,
            "difference": 2,
            "points": 3,
            "rank": None
        })

        self.group_1 = Group("F")
        self.group_1.teams = [self.team_1, self.team_2, self.team_3, self.team_4]

    def test_group_has_name(self):
        self.assertEqual("F", self.group_1.name)

    def test_group_has_4_teams(self):
        self.assertEqual(4, len(self.group_1.teams))

    def test_rank_tiebreaker_sorts_by_points(self):
        self.group_1.assign_rank()

        self.assertEqual(2, self.team_1.group_info["rank"])
        self.assertEqual(3, self.team_2.group_info["rank"])
        self.assertEqual(4, self.team_3.group_info["rank"])
        self.assertEqual(1, self.team_4.group_info["rank"])
