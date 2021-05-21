from flask import Flask, Blueprint, request, jsonify, make_response
from models.player import Player
import repositories.player_repository as player_repository

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