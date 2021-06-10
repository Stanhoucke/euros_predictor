from flask import Blueprint, request, jsonify, make_response
from models.league import League
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
    selected_players = league_repository.players(league)
    players = []
    for player in selected_players:
        del player.email
        del player.password
        players.append(player.__dict__)
    
    league = league.__dict__
    league["players"] = players
    return make_response(jsonify(league))

@league_blueprint.route("/leagues", methods=['POST'])
def new_league():
    post_data = request.get_json()
    league = League(post_data.get('name'))
    league_repository.save(league)
    return make_response(jsonify(league.__dict__)), 201