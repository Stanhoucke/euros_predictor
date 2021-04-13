import unittest

from models.player_points import PlayerPoints
from models.prediction import Prediction
from models.result import Result
from models.team import Team
from models.match import Match
from models.player import Player

class TestPlayerPoints(unittest.TestCase):
    def setUp(self):

        self.player_1 = Player("euros@gmail.com", "password1", "John", "Smith", "Hopp Suisse")

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

        goals_1 = {"home": 3, "away": 1}
        self.prediction_1 = Prediction(self.player_1, self.match_1, goals_1)
        goals_2 = {"home": 2, "away": 1}
        self.result_1 = Result(self.match_1, goals_2)

        self.player_points_1 = PlayerPoints(self.prediction_1, self.result_1)
    
    def test_player_points_has_prediction(self):
        self.assertEqual(self.prediction_1, self.player_points_1.prediction)

    def test_player_points_has_result(self):
        self.assertEqual(self.result_1, self.player_points_1.result)

    def test_predicted_outcome__returns_win(self):
        self.assertEqual("w", self.player_points_1.predicted_outcome())
    def test_predicted_outcome__returns_draw(self):
        goals_3 = {"home": 1, "away": 1}
        self.player_points_1.prediction.goals = goals_3
        self.assertEqual("d", self.player_points_1.predicted_outcome())
    def test_predicted_outcome__returns_loss(self):
        goals_4 = {"home": 1, "away": 4}
        self.player_points_1.prediction.goals = goals_4
        self.assertEqual("l", self.player_points_1.predicted_outcome())

    def test_actual_outcome__returns_win(self):
        self.assertEqual("w", self.player_points_1.actual_outcome())
    def test_actual_outcome__returns_draw(self):
        goals_3 = {"home": 1, "away": 1}
        self.player_points_1.result.goals = goals_3
        self.assertEqual("d", self.player_points_1.actual_outcome())
    def test_actual_outcome__returns_loss(self):
        goals_3 = {"home": 1, "away": 4}
        self.player_points_1.result.goals = goals_3
        self.assertEqual("l", self.player_points_1.actual_outcome())

    def outcome_points_assigns_player_points(self):
        self.player_points_1.outcome_points()
        self.assertEqual(3, self.player_1.points)