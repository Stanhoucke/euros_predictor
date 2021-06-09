import sys
sys.path.append('/Users/stanleyhoucke/coding_projects/euros_predictor/app/')

import repositories.player_repository as player_repository
from api.fetch_results import fetch_results

def setup_new_player():
    print("This is the setup new player function")

def update_all_player_points():
    # Fetch latest results from api
    fetch_results()
    # Get all players
    all_players = player_repository.select_all()
    # For each player, get predictions
    for player in all_players:
        # reset points to 0
        player.points = 0
        predictions = player_repository.predictions(player)
        if len(predictions) > 0:
            for prediction in predictions: 
                if prediction.goals["home"] and prediction.goals["away"] and prediction.match.goals["home"] and prediction.match.goals["away"]:
                    # get points from each prediction
                    prediction.award_points()
            # Update player
            player_repository.update(player)

# update_all_player_points()