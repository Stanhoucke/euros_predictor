import unittest

from models.team import Team

class TestTeam(unittest.TestCase):

    def setUp(self):
        self.team_1 = Team("France")

    def test_team_has_name(self):
        self.assertEqual("France", self.team_1.name)

    def test_team_has_group_info(self):
        group_info = {
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
        self.assertEqual(group_info, self.team_1.group_info)