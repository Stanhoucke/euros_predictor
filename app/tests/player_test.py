import unittest
from models.player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player_1 = Player("euros@gmail.com", "password1", "John", "Smith", "Hopp Suisse")

    def test_player_has_email(self):
        self.assertEqual("euros@gmail.com", self.player_1.email)

    def test_player_has_password(self):
        self.assertEqual(102, len(self.player_1.password))

    def test_player_has_first_name(self):
        self.assertEqual("John", self.player_1.first_name)

    def test_player_has_last_name(self):
        self.assertEqual("Smith", self.player_1.last_name)

    def test_player_has_team_name(self):
        self.assertEqual("Hopp Suisse", self.player_1.team_name)

    def test_player_can_encode_jwt(self):
        auth_token = self.player_1.encode_jwt(1)
        self.assertTrue(isinstance(auth_token, str))

    def test_player_can_decode_jwt(self):
        auth_token = self.player_1.encode_jwt(1)
        player_id = self.player_1.decode_jwt(auth_token)
        self.assertEqual(1, player_id)

