import unittest
import datetime
from models.prediction import Prediction
from models.match import Match
from models.team import Team
from models.player import Player
from models.player_team import PlayerTeam

class TestPrediction(unittest.TestCase):
    def setUp(self):
        self.player_1 = Player("euros@gmail.com", "password1", "John", "Smith", "Hopp Suisse")

        self.team_1 = Team("France")
        self.team_2 = Team("Germany")

        self.player_team_1 = PlayerTeam(self.player_1, self.team_1, "France")
        self.player_team_2 = PlayerTeam(self.player_1, self.team_2, "Germany")

        self.match_1 = Match("1", datetime.datetime(2016, 6, 10, 20, 0), "Stade de France", "A", self.team_1, self.team_2)

        self.prediction_1 = Prediction(self.player_1, self.match_1, self.player_team_1, self.player_team_2)
        self.prediction_2 = Prediction(self.player_1, self.match_1, self.player_team_1, self.player_team_2)

    def test_prediction_has_match(self):
        self.assertEqual(self.match_1, self.prediction_1.match)

    def test_prediction_has_player(self):
        self.assertEqual(self.player_1, self.prediction_1.player)

    def test_prediciton_starts_with_no_goals(self):
        self.assertEqual(None, self.prediction_1.goals["home"])
        self.assertEqual(None, self.prediction_1.goals["away"])

    def test_can_set_prediction_goals(self):
        self.prediction_1.set_goals(3, 1)
        self.assertEqual(3, self.prediction_1.goals["home"])
        self.assertEqual(1, self.prediction_1.goals["away"])


    def test_player_team_goals__assigns_goals_and_played(self):
        self.prediction_1.goals["home"] = 2
        self.prediction_1.goals["away"] = 2
        self.prediction_1.team_goals()

        # Home player_team
        home_for = self.prediction_1.home_player_team.group_info["for"]
        home_against = self.prediction_1.home_player_team.group_info["against"]
        home_difference = self.prediction_1.home_player_team.group_info["difference"]
        home_played = self.prediction_1.home_player_team.group_info["played"]
        # Away player_team
        away_for = self.prediction_1.away_player_team.group_info["for"]
        away_against = self.prediction_1.away_player_team.group_info["against"]
        away_difference = self.prediction_1.away_player_team.group_info["difference"]
        away_played = self.prediction_1.away_player_team.group_info["played"]

        self.assertEqual(2, home_for)
        self.assertEqual(2, home_against)
        self.assertEqual(0, home_difference)
        self.assertEqual(1, home_played)
        self.assertEqual(2, away_for)
        self.assertEqual(2, away_against)
        self.assertEqual(0, away_difference)
        self.assertEqual(1, away_played)


    def test_player_team_result__assigns_1_point_each_for_draw(self):
        self.prediction_1.goals["home"] = 2
        self.prediction_1.goals["away"] = 2
        self.prediction_1.team_points()

        home_points = self.prediction_1.home_player_team.group_info["points"]
        home_won = self.prediction_1.home_player_team.group_info["won"]
        home_lost = self.prediction_1.home_player_team.group_info["lost"]
        home_drawn = self.prediction_1.home_player_team.group_info["drawn"]
        away_points = self.prediction_1.away_player_team.group_info["points"]
        away_won = self.prediction_1.away_player_team.group_info["won"]
        away_lost = self.prediction_1.away_player_team.group_info["lost"]
        away_drawn = self.prediction_1.away_player_team.group_info["drawn"]

        self.assertEqual(1, home_points)
        self.assertEqual(0, home_won)
        self.assertEqual(0, home_lost)
        self.assertEqual(1, home_drawn)
        self.assertEqual(1, away_points)
        self.assertEqual(0, away_won)
        self.assertEqual(0, away_lost)
        self.assertEqual(1, away_drawn)

    def test_update_team_stats__assigns_stats_for_home_win(self):
        self.prediction_2.goals["home"] = 3
        self.prediction_2.goals["away"] = 1
        self.prediction_2.update_team_stats()

        # Home player_team
        home_for = self.prediction_2.home_player_team.group_info["for"]
        home_against = self.prediction_2.home_player_team.group_info["against"]
        home_difference = self.prediction_2.home_player_team.group_info["difference"]
        home_played = self.prediction_2.home_player_team.group_info["played"]
        home_points = self.prediction_2.home_player_team.group_info["points"]
        home_won = self.prediction_2.home_player_team.group_info["won"]
        home_lost = self.prediction_2.home_player_team.group_info["lost"]
        home_drawn = self.prediction_2.home_player_team.group_info["drawn"]
        # Away player_team
        away_for = self.prediction_2.away_player_team.group_info["for"]
        away_against = self.prediction_2.away_player_team.group_info["against"]
        away_difference = self.prediction_2.away_player_team.group_info["difference"]
        away_played = self.prediction_2.away_player_team.group_info["played"]
        away_points = self.prediction_2.away_player_team.group_info["points"]
        away_won = self.prediction_2.away_player_team.group_info["won"]
        away_lost = self.prediction_2.away_player_team.group_info["lost"]
        away_drawn = self.prediction_2.away_player_team.group_info["drawn"]

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

# Outcome based points
    def test_predicted_outcome__returns_win(self):
        self.prediction_1.set_goals(2, 1)
        self.assertEqual("w", self.prediction_1.predicted_outcome())
    def test_predicted_outcome__returns_draw(self):
        self.prediction_1.set_goals(1, 1)
        self.assertEqual("d", self.prediction_1.predicted_outcome())
    def test_predicted_outcome__returns_loss(self):
        self.prediction_1.set_goals(1, 4)
        self.assertEqual("l", self.prediction_1.predicted_outcome())

    def test_actual_outcome__returns_win(self):
        self.prediction_1.match.set_goals(2, 1)
        self.assertEqual("w", self.prediction_1.actual_outcome())
    def test_actual_outcome__returns_draw(self):
        self.prediction_1.match.set_goals(1, 1)
        self.assertEqual("d", self.prediction_1.actual_outcome())
    def test_actual_outcome__returns_loss(self):
        self.prediction_1.match.set_goals(1, 4)
        self.assertEqual("l", self.prediction_1.actual_outcome())

    def test_outcome_points_assigns_prediction(self):
        self.prediction_1.set_goals(2, 2)
        self.prediction_1.match.set_goals(0, 0)
        self.prediction_1.outcome_points()
        self.assertEqual(3, self.player_1.points)

    # Goals based points
    def test_home_goals__returns_false(self):
        self.prediction_1.set_goals(4, 2)
        self.prediction_1.match.set_goals(2, 3)
        self.assertFalse(self.prediction_1.home_goals_correct())
    def test_home_goals__returns_true(self):
        self.prediction_1.set_goals(2, 2)
        self.prediction_1.match.set_goals(2, 3)
        self.assertTrue(self.prediction_1.home_goals_correct())
    
    def test_away_goals__returns_true(self):
        self.prediction_1.set_goals(2, 3)
        self.prediction_1.match.set_goals(3, 3)
        self.assertTrue(self.prediction_1.away_goals_correct())
    def test_away_goals__returns_false(self):
        self.prediction_1.set_goals(2, 2)
        self.prediction_1.match.set_goals(2, 3)
        self.assertFalse(self.prediction_1.away_goals_correct())

    def test_goals_points__awards_1_point(self):
        self.prediction_1.set_goals(2, 2)
        self.prediction_1.match.set_goals(2, 3)
        self.prediction_1.goals_points()
        self.assertEqual(1, self.player_1.points)
    def test_goals_points__awards_2_points(self):
        self.prediction_1.set_goals(2, 1)
        self.prediction_1.match.set_goals(2, 1)
        self.prediction_1.goals_points()
        self.assertEqual(2, self.player_1.points)

    # Award player points
    def test_award_points__awards_5_points(self):
        self.prediction_1.set_goals(2, 3)
        self.prediction_1.match.set_goals(2, 3)
        self.prediction_1.award_points()
        self.assertEqual(5, self.player_1.points)
    def test_award_points__awards_4_points(self):
        self.prediction_1.set_goals(2, 1)
        self.prediction_1.match.set_goals(2, 0)
        self.prediction_1.award_points()
        self.assertEqual(4, self.player_1.points)
    def test_award_points__awards_3_points(self):
        self.prediction_1.set_goals(2, 2)
        self.prediction_1.match.set_goals(0, 0)
        self.prediction_1.award_points()
        self.assertEqual(3, self.player_1.points)
    def test_award_points__awards_1_points(self):
        self.prediction_1.set_goals(2, 2)
        self.prediction_1.match.set_goals(2, 3)
        self.prediction_1.award_points()
        self.assertEqual(1, self.player_1.points)
    def test_award_points__awards_0_points(self):
        self.prediction_1.set_goals(1, 2)
        self.prediction_1.match.set_goals(2, 0)
        self.prediction_1.award_points()
        self.assertEqual(0, self.player_1.points)
    