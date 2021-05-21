from flask import Flask, Blueprint, request, jsonify, make_response
from models.team import Team
import repositories.team_repository as team_repository

teams_blueprint = Blueprint("teams_blueprint", __name__)

@teams_blueprint.route("/teams")
def show_teams():
    teams = []
    selected_teams = team_repository.select_all()
    for team in selected_teams:
        teams.append(team.__dict__)
    return make_response(jsonify(teams)), 200

@teams_blueprint.route("/teams/<id>")
def show_team(id):
    team = team_repository.select(id)
    return make_response(jsonify(team.__dict__)), 200

@teams_blueprint.route("/teams", methods=['POST'])
def new_team():
    post_data = request.get_json()
    team = Team(post_data.get('name'))
    team_repository.save(team)
    return make_response(jsonify(team.__dict__)), 201

