import unittest

from models.team import Team

class TestTeam(unittest.TestCase):

    def setUp(self):
        self.team_1 = Team("France")

    def test_team_has_name(self):
        self.assertEqual("France", self.team_1.name)

    