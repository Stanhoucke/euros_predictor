from flask import Blueprint, request, jsonify, make_response
import repositories.player_league_repository as player_league_repository

player_league_blueprint = Blueprint("player_league_blueprint", __name__)

@player_league_blueprint.route("/player_leagues", methods=['GET'])
def show_player_leagues():
    player_leagues = []
    selected_player_leagues = player_league_repository.select_all()
    for player_league in selected_player_leagues:
        del player_league.player.email
        del player_league.player.password
        player_league.player = player_league.player.__dict__
        player_league.league = player_league.league.__dict__

        player_leagues.append(player_league.__dict__)
    
    return make_response(jsonify(player_leagues)), 200

@player_league_blueprint.route("/player_leagues/<id>", methods=['GET'])
def show_player_league(id):
    player_league = player_league_repository.select(id)
    del player_league.player.email
    del player_league.player.password
    player_league.player = player_league.player.__dict__
    player_league.league = player_league.league.__dict__
    return make_response(jsonify(player_league.__dict__))