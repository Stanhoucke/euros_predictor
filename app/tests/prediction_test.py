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
        goals_2 = {"home": 3, "away": 1}
        self.prediction_2 = Prediction(self.player_1, self.match_1, goals_2)

    def test_prediction_has_match(self):
        self.assertEqual(self.match_1, self.prediction_1.match)

    def test_prediction_has_player(self):
        self.assertEqual(self.player_1, self.prediction_1.player)

    def test_prediciton_has_goals(self):
        self.assertEqual(2, self.prediction_1.goals["home"])
        self.assertEqual(2, self.prediction_1.goals["away"])

    def test_team_goals__assigns_goals_and_played(self):
        self.prediction_1.team_goals()

        # Home team
        home_for = self.prediction_1.match.team_1.group_info["for"]
        home_against = self.prediction_1.match.team_1.group_info["against"]
        home_difference = self.prediction_1.match.team_1.group_info["difference"]
        home_played = self.prediction_1.match.team_1.group_info["played"]
        # Away team
        away_for = self.prediction_1.match.team_2.group_info["for"]
        away_against = self.prediction_1.match.team_2.group_info["against"]
        away_difference = self.prediction_1.match.team_2.group_info["difference"]
        away_played = self.prediction_1.match.team_2.group_info["played"]

        self.assertEqual(2, home_for)
        self.assertEqual(2, home_against)
        self.assertEqual(0, home_difference)
        self.assertEqual(1, home_played)
        self.assertEqual(2, away_for)
        self.assertEqual(2, away_against)
        self.assertEqual(0, away_difference)
        self.assertEqual(1, away_played)


    def test_team_result__assigns_1_point_each_for_draw(self):
        self.prediction_1.team_result()

        home_points = self.prediction_1.match.team_1.group_info["points"]
        home_won = self.prediction_1.match.team_1.group_info["won"]
        home_lost = self.prediction_1.match.team_1.group_info["lost"]
        home_drawn = self.prediction_1.match.team_1.group_info["drawn"]
        away_points = self.prediction_1.match.team_2.group_info["points"]
        away_won = self.prediction_1.match.team_2.group_info["won"]
        away_lost = self.prediction_1.match.team_2.group_info["lost"]
        away_drawn = self.prediction_1.match.team_2.group_info["drawn"]

        self.assertEqual(1, home_points)
        self.assertEqual(0, home_won)
        self.assertEqual(0, home_lost)
        self.assertEqual(1, home_drawn)
        self.assertEqual(1, away_points)
        self.assertEqual(0, away_won)
        self.assertEqual(0, away_lost)
        self.assertEqual(1, away_drawn)

    def test_play_match__assigns_stats_for_home_win(self):
        self.prediction_2.play_match()

        # Home team
        home_for = self.prediction_2.match.team_1.group_info["for"]
        home_against = self.prediction_2.match.team_1.group_info["against"]
        home_difference = self.prediction_2.match.team_1.group_info["difference"]
        home_played = self.prediction_2.match.team_1.group_info["played"]
        home_points = self.prediction_2.match.team_1.group_info["points"]
        home_won = self.prediction_2.match.team_1.group_info["won"]
        home_lost = self.prediction_2.match.team_1.group_info["lost"]
        home_drawn = self.prediction_2.match.team_1.group_info["drawn"]
        # Away team
        away_for = self.prediction_2.match.team_2.group_info["for"]
        away_against = self.prediction_2.match.team_2.group_info["against"]
        away_difference = self.prediction_2.match.team_2.group_info["difference"]
        away_played = self.prediction_2.match.team_2.group_info["played"]
        away_points = self.prediction_2.match.team_2.group_info["points"]
        away_won = self.prediction_2.match.team_2.group_info["won"]
        away_lost = self.prediction_2.match.team_2.group_info["lost"]
        away_drawn = self.prediction_2.match.team_2.group_info["drawn"]

        self.assertEqual(3, home_for)
        self.assertEqual(1, home_against)
        self.assertEqual(2, home_difference)
        self.assertEqual(1, home_played)
        self.assertEqual(1, away_for)
        self.assertEqual(3, away_against)
        self.assertEqual(-2, away_difference)
        self.assertEqual(1, away_played)

        self.assertEqual(3, home_points)
        self.assertEqual(1, home_won)
        self.assertEqual(0, home_lost)
        self.assertEqual(0, home_drawn)
        self.assertEqual(0, away_points)
        self.assertEqual(0, away_won)
        self.assertEqual(1, away_lost)
        self.assertEqual(0, away_drawn)
