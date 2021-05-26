from flask import Flask, Blueprint, request, jsonify, make_response
from models.blacklist import Blacklist
from models.player import Player
import repositories.player_repository as player_repository
import repositories.blacklist_token_repository as blacklist_token_repository

players_blueprint = Blueprint("players_blueprint", __name__)

@players_blueprint.route("/register", methods=['POST'])
def register_player():
    post_data = request.get_json()

    # Check if player already exists
    player = player_repository.select_by_email(post_data.get('email'))
    if not player:
        try:
            # New player
            player = Player(
                email=post_data.get('email'),
                password=post_data.get('password'),
                first_name=post_data.get('first_name'),
                last_name=post_data.get('last_name'),
                team_name=post_data.get('team_name')
            )
            player_repository.save(player)

            auth_token = player.encode_jwt(player.id)
            response = {
                'status': 'success',
                'message': 'Successfully registered.',
                'auth_token': auth_token
            }
            return make_response(jsonify(response)), 201
        except Exception as e:
            response = {
                'status': 'fail',
                'message': 'Something went wrong. Please try again.'
            }
            return make_response(jsonify(response)), 401
    else:
        response = {
                'status': 'fail',
                'message': 'User already exists. Please log in.'
        }
        return make_response(jsonify(response)), 202

@players_blueprint.route("/login", methods=['POST'])
def login_player():
    post_data = request.get_json()
    try:
        player = player_repository.select_by_email(post_data.get('email'))
        if player and player is not None and player.check_password(post_data.get('password')):
            auth_token = player.encode_jwt(player.id)
            response = {
                'status': 'success',
                'message': 'Successfully logged in.',
                'auth_token': auth_token,
                'data': {
                    "email": player.email,
	                "first_name": player.first_name,
	                "last_name": player.last_name,
                    "full_name": player.full_name(),
	                "team_name": player.team_name,
                    "player_points": player.points
                }
            }
            headers = {'Authorization': auth_token}
            return make_response(jsonify(response), 200, headers)
        else:
            response = {
                    'status': 'fail',
                    'message': 'User does not exist.'
                }
            return make_response(jsonify(response)), 404
    except Exception as e:
        print(e)
        response = {
            'status': 'fail',
            'message': 'Try again'
        }
        return make_response(jsonify(response)), 500

@players_blueprint.route("/logout", methods=['POST'])
def logout():
    auth_header = request.headers.get('Authorization')
    if auth_header:
        auth_token = auth_header.split(" ")[1]
    else: auth_token = ''

    if auth_token:
        user = Player.decode_jwt(auth_token)
        if not isinstance(user, str):
            blacklist_token = Blacklist(auth_token)
            try: 
                blacklist_token_repository.save(blacklist_token)
                response = {
                    'status': 'success',
                    'message': 'Logged out successfully'
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
                    'message': user
                }
                return make_response(jsonify(response)), 401
    else:
        response = {
                    'status': 'fail',
                    'message': 'Invalid token provided.'
        }
        return make_response(jsonify(response)), 403


