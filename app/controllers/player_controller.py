from flask import Blueprint, json, request, jsonify, make_response
from models.player import Player
from controllers.auth_controller import login_required
import repositories.player_repository as player_repository
import repositories.league_repository as league_repository

player_blueprint = Blueprint("player_blueprint", __name__)

def get_player_info(player):
    player_info = {
        "leagues": [],
        "player_teams": [],
        "player_groups": [],
        "predictions": {
            "1": [],
            "2": [],
            "3": [],
            "Round of 16": [],
            "Quarter Finals": [],
            "Semi Finals": [],
            "Final":[]
        }
    }
    for league in player_repository.leagues(player):
        selected_players = league_repository.players(league)
        players = []
        for selected_player in selected_players:
            del selected_player.email
            del selected_player.password
            players.append(selected_player.__dict__)
        
        league = league.__dict__
        league["players"] = players

        player_info["leagues"].append(league)

    for player_team in player_repository.player_teams(player):
        del player_team.player
        del player_team.team.group_info
        player_team.team = player_team.team.__dict__
        player_info["player_teams"].append(player_team.__dict__)

    for player_group in player_repository.player_groups(player):
        del player_group.player
        player_teams = []
        for player_team in player_group.player_teams:
            del player_team.player
            del player_team.team.group_info
            player_team.team = player_team.team.__dict__
            player_teams.append(player_team.__dict__)
        player_group.player_teams = player_teams
        player_info["player_groups"].append(player_group.__dict__)

    for prediction in player_repository.predictions(player):
        del prediction.player

        if prediction.match.team_1 and prediction.match.team_2:
            del prediction.match.team_1.group_info
            del prediction.match.team_2.group_info
            prediction.match.team_1 = prediction.match.team_1.__dict__
            prediction.match.team_2 = prediction.match.team_2.__dict__
            
        prediction.match = prediction.match.__dict__
        del prediction.home_player_team
        del prediction.away_player_team
        player_info["predictions"][prediction.match["round_number"]].append(prediction.__dict__)

    player = player.__dict__
    player.pop("email")
    player.pop("password")

    player["leagues"] = player_info["leagues"]
    player["player_teams"] = player_info["player_teams"]
    player["player_groups"] = player_info["player_groups"]
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

