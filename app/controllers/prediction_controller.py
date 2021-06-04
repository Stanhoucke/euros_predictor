from flask import Blueprint, request, jsonify, make_response
from controllers.auth_controller import login_required
import repositories.prediction_repository as prediction_repository
import repositories.player_team_repository as player_team_repository
import repositories.player_repository as player_repository
import repositories.player_group_repository as player_group_repository

prediction_blueprint = Blueprint("prediction_blueprint", __name__)

def prediction_json(prediction):
    del prediction.player.password
    del prediction.player.email
    del prediction.home_player_team.player
    del prediction.home_player_team.team
    del prediction.home_player_team.group_info
    del prediction.away_player_team.player
    del prediction.away_player_team.team
    del prediction.away_player_team.group_info
    del prediction.match.team_1.group_info
    del prediction.match.team_2.group_info
    prediction.player = prediction.player.__dict__
    prediction.match.team_1 = prediction.match.team_1.__dict__
    prediction.match.team_2 = prediction.match.team_2.__dict__
    prediction.match = prediction.match.__dict__
    prediction.home_player_team = prediction.home_player_team.__dict__
    prediction.away_player_team = prediction.away_player_team.__dict__

    return prediction.__dict__

@prediction_blueprint.route("/predictions", methods=['GET'])
def show_predictions():
    predictions = []
    selected_predictions = prediction_repository.select_all()
    for prediction in selected_predictions:
        predictions.append(prediction_json(prediction))

    return make_response(jsonify(predictions)), 200

@prediction_blueprint.route("/predictions/<id>", methods=['GET'])
def show_prediction(id):
    selected_prediction = prediction_repository.select(id)
    prediction = prediction_json(selected_prediction)
    return make_response(jsonify(prediction)), 200

@prediction_blueprint.route("/predictions", methods=['PUT'])
@login_required
def update_predictions():
    player_id = update_predictions.user_id
    put_data = request.get_json()
    if not isinstance(player_id, str):
        try:
            for id, goals in put_data.items():
                prediction = prediction_repository.select(id)
                prediction.set_goals(goals["home"], goals["away"])
                player_team_repository.update(prediction.home_player_team)
                player_team_repository.update(prediction.away_player_team)
                prediction_repository.update(prediction)

            active_player = player_repository.select(player_id)
            player_groups = player_repository.player_groups(active_player)
            player_group_repository.update_all(player_groups)

            response = {
                            'status': 'success',
                            'message': 'Your predictions have been saved successfully!'
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


