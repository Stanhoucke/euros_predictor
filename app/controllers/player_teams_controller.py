from flask import Blueprint, request, make_response, jsonify
from controllers.auth_controller import login_required
from models.player_team import PlayerTeam
import repositories.player_team_repository as player_team_repository

player_teams_blueprint = Blueprint("player_teams_blueprint", __name__)

@player_teams_blueprint.route("/player_teams")
@login_required
def show_player_teams():
    player_teams = []
    selected_player_teams = player_team_repository.select_all()
    for player_team in selected_player_teams:
        player_team.player = player_team.player.__dict__
        player_team.player.pop("email")
        player_team.player.pop("password")

        player_team.team = player_team.team.__dict__

        player_teams.append(player_team.__dict__)
    return make_response(jsonify(player_teams)), 200