from flask import Blueprint, request, jsonify, make_response
from controllers.auth_controller import login_required
from models.league import League
from models.player_league import PlayerLeague
import repositories.player_league_repository as player_league_repository
import repositories.league_repository as league_repository
import repositories.player_repository as player_repository

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

@player_league_blueprint.route("/player_leagues", methods=['POST'])
@login_required
def new_player_league():
    player_id = new_player_league.user_id
    post_data = request.get_json()
    if not isinstance(player_id, str):
        try:
            active_player = player_repository.select(player_id)
            league = League(post_data.get('name'))
            league_repository.save(league)
            player_league = PlayerLeague(league, active_player)
            player_league_repository.save(player_league)

            response = {
                'status': 'success',
                'message': league.name + ' code: ' + league.join_code
            }

            return make_response(jsonify(response)), 201
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

@player_league_blueprint.route("/player_leagues/join", methods=['POST'])
@login_required
def join_player_league():
    player_id = join_player_league.user_id
    post_data = request.get_json()
    if not isinstance(player_id, str):
        try:
            active_player = player_repository.select(player_id)
            league = league_repository.select_by_join_code(post_data.get('join_code'))
            player_league = PlayerLeague(league, active_player)
            player_league_repository.save(player_league)

            response = {
                    'status': 'success',
                    'message': 'Successfully joined the ' + league.name + ' league!'
            }

            return make_response(jsonify(response)), 200
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


