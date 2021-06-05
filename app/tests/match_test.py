import unittest
import datetime
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

        self.match_1 = Match("1", datetime.datetime(2016, 6, 10, 20, 0), "Stade de France", "A", self.team_1, self.team_2)
        self.match_2 = Match("Round of 16", datetime.datetime(2016, 6, 25, 14, 0), "Parc des Princes", None, self.team_1, self.team_2)

    def test_match_has_two_teams(self):
        self.assertEqual(self.team_1, self.match_1.team_1)
        self.assertEqual(self.team_2, self.match_1.team_2)

    def test_match_starts_with_no_goals(self):
        self.assertEqual(None, self.match_1.goals["home"])
        self.assertEqual(None, self.match_1.goals["away"])

    def test_can_set_match_goals(self):
        self.match_2.set_goals(2, 1)
        self.assertEqual(2, self.match_2.goals["home"])
        self.assertEqual(1, self.match_2.goals["away"])

    def test_has_round_number(self):
        self.assertEqual("1", self.match_1.round_number)

    def test_has_date(self):
        self.assertEqual(datetime.datetime(2016, 6, 10, 20, 0), self.match_1.date)

    def test_has_location(self):
        self.assertEqual("Stade de France", self.match_1.location)

    def test_has_group_name(self):
        self.assertEqual("A", self.match_1.group_name)
    