import unittest
from models.prediction import Prediction
from models.match import Match
from models.player import Player
from models.team import Team

class TestPrediction(unittest.TestCase):
    def setUp(self):
        self.player_1 = Player("euros@gmail.com", "password1", "John", "Smith", "Hopp Suisse")

        self.team_1 = Team(self.player_1, "France", {
            "played": 0,
            "won": 0,
            "drawn": 0,
            "lost": 0,
            "for": 0,
            "against": 0,
            "difference": 0,
            "points": 0,
            "rank": None
        })
        self.team_2 = Team(self.player_1, "Germany", {
            "played": 0,
            "won": 0,
            "drawn": 0,
            "lost": 0,
            "for": 0,
            "against": 0,
            "difference": 0,
            "points": 0,
            "rank": None
        })

        self.match_1 = Match(self.team_1, self.team_2)

        goals_1 = {"home": 2, "away": 2}
        self.prediction_1 = Prediction(self.player_1, self.match_1, goals_1)

    def test_prediction_has_match(self):
        self.assertEqual(self.match_1, self.prediction_1.match)

    def test_prediction_has_player(self):
        self.assertEqual(self.player_1, self.prediction_1.player)

    def test_prediciton_has_goals(self):
        self.assertEqual(2, self.prediction_1.goals["home"])
        self.assertEqual(2, self.prediction_1.goals["away"])

    def test_team_points__returns_1_point_each_for_draw(self):
        self.prediction_1.team_points()
        home_points = self.prediction_1.match.team_1.group_info["points"]
        away_points = self.prediction_1.match.team_2.group_info["points"]
        self.assertEqual(1, home_points)
        self.assertEqual(1, away_points)