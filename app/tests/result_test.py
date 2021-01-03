import unittest
from models.result import Result
from models.match import Match
from models.team import Team

class TestResult(unittest.TestCase):
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
        self.result_1 = Result(self.match_1, 2, 2)

    def test_result_has_match(self):
        self.assertEqual(self.match_1, self.result_1.match)

    def test_result_has_two_scores(self):
        self.assertEqual(2, self.result_1.team_1_goals)
        self.assertEqual(2, self.result_1.team_2_goals)