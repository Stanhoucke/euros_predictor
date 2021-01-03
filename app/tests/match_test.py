import unittest
from models.match import Match
from models.team import Team

class TestMatch(unittest.TestCase):
    def setUp(self):
        self.team_1 = Team("France", {
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
        self.team_2 = Team("Germany", {
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

        self.match_1 = Match(self.team_1, self.team_2)

    def test_match_has_two_teams(self):
        self.assertEqual(self.team_1, self.match_1.team_1)
        self.assertEqual(self.team_2, self.match_1.team_2)

    