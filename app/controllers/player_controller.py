from flask import Blueprint, request, jsonify, make_response
from models.player import Player
from controllers.auth_controller import login_required
import repositories.player_repository as player_repository

player_blueprint = Blueprint("player_blueprint", __name__)

def get_player_info(player):
    player_info = {
        "leagues": [],
        "player_teams": [],
        "predictions": []
    }
    for league in player_repository.leagues(player):
        player_info["leagues"].append(league.__dict__)

    for player_team in player_repository.player_teams(player):
        del player_team.player
        player_team.team = player_team.team.__dict__
        player_info["player_teams"].append(player_team.__dict__)

    for prediction in player_repository.predictions(player):
        del prediction.player
        del prediction.match.team_1.group_info
        del prediction.match.team_2.group_info
        prediction.match.team_1 = prediction.match.team_1.__dict__
        prediction.match.team_2 = prediction.match.team_2.__dict__
        prediction.match = prediction.match.__dict__
        player_info["predictions"].append(prediction.__dict__)

    return player_info

@player_blueprint.route("/players", methods=['GET'])
# @login_required
def show_players():
    players = []
    selected_players = player_repository.select_all()
    for player in selected_players:
        player_info = get_player_info(player)

        player = player.__dict__
        player.pop("email")
        player.pop("password")

        player["leagues"] = player_info["leagues"]
        player["player_teams"] = player_info["player_teams"]
        player["predictions"] = player_info["predictions"]

        players.append(player)
    
    return make_response(jsonify(players)), 200
