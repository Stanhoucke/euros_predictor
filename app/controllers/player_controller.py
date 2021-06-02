from flask import Blueprint, json, request, jsonify, make_response
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

    player = player.__dict__
    player.pop("email")
    player.pop("password")

    player["leagues"] = player_info["leagues"]
    player["player_teams"] = player_info["player_teams"]
    player["predictions"] = player_info["predictions"]

    return player


@player_blueprint.route("/players", methods=['GET'])
def show_players():
    players = []
    selected_players = player_repository.select_all()
    for player in selected_players:
        players.append(get_player_info(player))
    
    return make_response(jsonify(players)), 200

@player_blueprint.route("/players/<id>", methods=['GET'])
def show_player(id):
    selected_player = player_repository.select(id)
    player = get_player_info(selected_player)
    return make_response(jsonify(player)), 200

@player_blueprint.route("/player", methods=['GET'])
@login_required
def show_active_player():
    player_id = show_active_player.user_id
    print(player_id)
    if not isinstance(player_id, str):
        try:
            active_player = player_repository.select(player_id)
            player = get_player_info(active_player)
            return make_response(jsonify(player)), 200
        except Exception as e:
                response = {
                    'status': 'fail',
                    'message': e
                }
                return make_response(jsonify(response)), 200
    else:
        response = {
            'status': 'fail',
            'message': player_id
        }
        return make_response(jsonify(response)), 401
