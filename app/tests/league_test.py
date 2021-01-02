import unittest

from models.league import League

class TestLeague(unittest.TestCase):
    def setUp(self):
        self.league_1 = League("Wilton Wanderers", "1234-5678")

    def test_league_has_name(self):
        self.assertEqual("Wilton Wanderers", self.league_1.name)

    def test_league_has_join_code(self):
        self.assertEqual("1234-5678", self.league_1.join_code)

    def test_generate_join_code_method(self):
        code = self.league_1.generate_join_code()
        self.assertEqual(9, len(code))
