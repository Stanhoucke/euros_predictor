from flask import Flask, Blueprint, request, jsonify, make_response
from models.group import Group
import repositories.group_repository as group_repository

groups_blueprint = Blueprint("groups_blueprint", __name__)

@groups_blueprint.route("/groups")
def show_groups():
    groups = []
    selected_groups = group_repository.select_all()
    for group in selected_groups:
        teams = []
        for team in group.teams:
            teams.append(team.__dict__)
        group.teams = teams
        groups.append(group.__dict__)
    return make_response(jsonify(groups)), 200
