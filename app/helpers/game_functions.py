import sys
sys.path.append('/Users/stanleyhoucke/coding_projects/euros_predictor/app/')

import repositories.player_repository as player_repository
import repositories.team_repository as team_repository
import repositories.group_repository as group_repository
import repositories.match_repository as match_repository
import repositories.prediction_repository as prediction_repository
import repositories.player_group_repository as player_group_repository
import repositories.player_team_repository as player_team_repository
from models.player_team import PlayerTeam
from models.player_group import PlayerGroup
from models.prediction import Prediction
from api.fetch_results import fetch_results

def setup_new_player(player):
    # Player Teams
    for team in team_repository.select_all():
        player_team_repository.save(PlayerTeam(player, team))

    # Player Groups
    for group in group_repository.select_all():
        player_teams = []
        for team in group.teams:
            player_teams.append(player_team_repository.select_by_player_and_team(player, team))
        player_group_repository.save(PlayerGroup(player, group.name, player_teams))

    # Predictions
    for match in match_repository.select_all():
        home_player_team = player_team_repository.select_by_player_and_team(player, match.team_1)
        away_player_team = player_team_repository.select_by_player_and_team(player, match.team_2)
        prediction_repository.save(Prediction(player, match, home_player_team, away_player_team))

def update_all_player_points():
    fetch_results()

    all_players = player_repository.select_all()

    for player in all_players:
        player.points = 0
        predictions = player_repository.predictions(player)
        
        if len(predictions) > 0:
            for prediction in predictions: 
                if prediction.goals["home"] and prediction.goals["away"] and prediction.match.goals["home"] and prediction.match.goals["away"]:
                    prediction.award_points()

            player_repository.update(player)

# update_all_player_points()