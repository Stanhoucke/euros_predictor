from flask import Flask, Blueprint, request, jsonify, make_response
from models.player import Player
import repositories.player_repository as player_repository

players_blueprint = Blueprint("players_blueprint", __name__)

@players_blueprint.route("/register", methods=['POST'])
def register_player():
    post_data = request.get_json()

    # Check if player already exists
        # create query by email

    # New player
        #TODO encrypt password
        # methods for encoding and decoding auth token
        
    player = Player(
        email=post_data.get('email'),
        password=post_data.get('password'),
        first_name=post_data.get('first_name'),
        last_name=post_data.get('last_name'),
        team_name=post_data.get('team_name')
    )
    player_repository.save(player)
    response = {
        'status': 'success',
        'message': 'Successfully registered.'
    }
    return make_response(jsonify(response)), 201