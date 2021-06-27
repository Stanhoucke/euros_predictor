from db.run_sql import run_sql
from models.prediction import Prediction

import repositories.player_repository as player_repository
import repositories.match_repository as match_repository
import repositories.player_team_repository as player_team_repository

# Create
def save(prediction):
    sql = "INSERT INTO predictions (player_id, match_id, team_1_id, team_2_id, home_goals, away_goals, has_prediction) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id"
    
    if prediction.home_player_team == None and prediction.away_player_team == None:
        values = [prediction.player.id, prediction.match.id, None, None, prediction.goals["home"], prediction.goals["away"], prediction.has_prediction]
    else:
        values = [prediction.player.id, prediction.match.id, prediction.home_player_team.id, prediction.away_player_team.id, prediction.goals["home"], prediction.goals["away"], prediction.has_prediction]
    
    result = run_sql(sql, values)
    prediction.id = result[0]['id']
    return prediction

# Read
def select(id):
    prediction = None

    sql = "SELECT * FROM predictions WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        player = player_repository.select(result['player_id'])
        match = match_repository.select(result['match_id'])

        if result['team_1_id'] == None:
            home_player_team = None
        else:
            home_player_team = player_team_repository.select(result['team_1_id'])
        if result['team_2_id'] == None:
            away_player_team = None
        else:
            away_player_team = player_team_repository.select(result['team_2_id'])

        prediction = Prediction(player, match, home_player_team, away_player_team, result['id'])
        prediction.has_prediction = result['has_prediction']
        prediction.goals['home'] = result['home_goals']
        prediction.goals['away'] = result['away_goals']
    return prediction

def select_all():
    predictions = []

    sql = "SELECT * FROM predictions"
    results = run_sql(sql)

    for row in results:
        player = player_repository.select(row['player_id'])
        match = match_repository.select(row['match_id'])
        
        if row['team_1_id'] == None:
            home_player_team = None
        else:
            home_player_team = player_team_repository.select(row['team_1_id'])
        if row['team_2_id'] == None:
            away_player_team = None
        else:
            away_player_team = player_team_repository.select(row['team_2_id'])

        prediction = Prediction(player, match, home_player_team, away_player_team, row['id'])
        prediction.has_prediction = row['has_prediction']
        prediction.goals['home'] = row['home_goals']
        prediction.goals['away'] = row['away_goals']
        predictions.append(prediction)
    return predictions

# Update
def update(prediction):
    sql = "UPDATE predictions SET (team_1_id, team_2_id, home_goals, away_goals, has_prediction) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [prediction.home_player_team.id, prediction.away_player_team.id, prediction.goals["home"], prediction.goals["away"], prediction.has_prediction, prediction.id]
    run_sql(sql, values)

# Delete
def delete(id):
    sql = "DELETE FROM predictions WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM predictions"
    run_sql(sql)

