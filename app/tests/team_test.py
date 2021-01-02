import unittest

from models.team import Team

class TestTeam(unittest.TestCase):

    def setUp(self):
        self.team_1 = Team("France", 1)

    def test_team_has_name(self):
        self.assertEqual("France", self.team_1.name)

    def test_team_has_group_rank(self):
        self.assertEqual(1, self.team_1.group_rank)

    