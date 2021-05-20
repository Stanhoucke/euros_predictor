from flask import Flask, Blueprint, jsonify, make_response
from models.team import Team
import repositories.team_repository as team_repository

teams_blueprint = Blueprint("teams_blueprint", __name__)

@teams_blueprint.route("/teams")
def get_teams():
    teams = []
    selected_teams = team_repository.select_all()
    for team in selected_teams:
        teams.append(team.__dict__)
    return make_response(jsonify(teams)), 200