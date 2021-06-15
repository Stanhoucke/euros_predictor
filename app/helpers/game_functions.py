import sys
sys.path.append('/Users/stanleyhoucke/coding_projects/euros_predictor/app/')

from datetime import datetime
import csv

import repositories.player_repository as player_repository
import repositories.team_repository as team_repository
import repositories.group_repository as group_repository
import repositories.match_repository as match_repository
import repositories.league_repository as league_repository
import repositories.prediction_repository as prediction_repository
import repositories.player_group_repository as player_group_repository
import repositories.player_team_repository as player_team_repository
import repositories.player_league_repository as player_league_repository
from models.player_team import PlayerTeam
from models.player_league import PlayerLeague
from models.player_group import PlayerGroup
from models.prediction import Prediction
from models.team import Team
from models.match import Match
from api.fetch_results import fetch_results

def add_to_overall_league(player):
    overall_league = league_repository.select(1)
    player_league_repository.save(PlayerLeague(overall_league, player))

def setup_new_player(player):
    add_to_overall_league(player)

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
                if prediction.has_prediction and prediction.match.goals["home"] is not None and prediction.match.goals["away"] is not None:
                    prediction.award_points()

            player_repository.update(player)

def populate_matches():
    with open('/Users/stanleyhoucke/coding_projects/euros_predictor/app/db/euro2020-matches.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            date = datetime.strptime(row["Date"], '%d/%m/%Y %H:%M')
            if len(row["Round Number"]) == 1:
                team_1 = team_repository.select_by_name(row["Home Team"])
                team_2 = team_repository.select_by_name(row["Away Team"])
                match = Match(row["Round Number"], date, row["Location"], row["Group"], team_1, team_2)
                match_repository.save(match)
            else:
                match = Match(row["Round Number"], date, row["Location"], row["Group"], None, None)
                match_repository.save(match)
    csv_file.close()

def create_predictions_for_knockout_matches():
    for player in player_repository.select_all():
        # Predictions
        for match in match_repository.select_all():
            if match.id > 36:
                if match.team_1 != None and match.team_2 != None:
                    home_player_team = player_team_repository.select_by_player_and_team(player, match.team_1)
                    away_player_team = player_team_repository.select_by_player_and_team(player, match.team_2)
                    prediction_repository.save(Prediction(player, match, home_player_team, away_player_team))
                else:
                    prediction_repository.save(Prediction(player, match, None, None))



# update_all_player_points()