from flask import Blueprint, request, jsonify, make_response
import repositories.league_repository as league_repository

league_blueprint = Blueprint("league_blueprint", __name__)

@league_blueprint.route("/leagues", methods=['GET'])
def show_leagues():
    leagues = []
    selected_leagues = league_repository.select_all()
    for league in selected_leagues:
        leagues.append(league.__dict__)
    
    return make_response(jsonify(leagues)), 200

@league_blueprint.route("/leagues/<id>", methods=['GET'])
def show_league(id):
    league = league_repository.select(id)
    return make_response(jsonify(league.__dict__))