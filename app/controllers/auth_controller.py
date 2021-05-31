from flask import Blueprint, request, jsonify, make_response
from functools import wraps
from models.blacklist import Blacklist
from models.player import Player
import repositories.player_repository as player_repository
import repositories.blacklist_token_repository as blacklist_token_repository

auth_blueprint = Blueprint("players_blueprint", __name__)

@auth_blueprint.route("/register", methods=['POST'])
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
                first_name=post_data.get('firstName'),
                last_name=post_data.get('lastName'),
                team_name=post_data.get('teamName')
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

@auth_blueprint.route("/login", methods=['POST'])
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
            return make_response(jsonify(response)), 200
        else:
            response = {
                    'status': 'fail',
                    'message': 'Incorrect username or password.'
                }
            return make_response(jsonify(response)), 401
    except Exception as e:
        print(e)
        response = {
            'status': 'fail',
            'message': 'Try again'
        }
        return make_response(jsonify(response)), 500


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if auth_header:
            auth_token = auth_header.split(" ")[1]
        else: auth_token = ''

        if auth_token:
            user_id = Player.decode_jwt(auth_token)
            setattr(decorated_function, "user_id", user_id)
            setattr(decorated_function, "auth_token", auth_token)
        else:
            response = {
                    'status': 'fail',
                    'message': 'Invalid token provided.'
            }
            return make_response(jsonify(response)), 403

        return f(*args, **kwargs)
    return decorated_function

@auth_blueprint.route("/logout", methods=['POST'])
@login_required
def logout():
        user = logout.user_id
        if not isinstance(user, str):
            blacklist_token = Blacklist(logout.auth_token)
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
