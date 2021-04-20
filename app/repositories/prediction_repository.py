from db.run_sql import run_sql
from models.prediction import Prediction

import repositories.player_repository as player_repository
import repositories.match_repository as match_repository

# Create
def save(prediction):
    sql = "INSERT INTO predictions (player_id, match_id, home_goals, away_goals) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [prediction.player.id, prediction.match.id, prediction.goals["home"], prediction.goals["away"]]
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
        prediction = Prediction(player, match, result['id'])
        prediction.set_goals(result['home_goals'], result['away_goals'])
    return prediction

def select_all():
    predictions = []

    sql = "SELECT * FROM predictions"
    results = run_sql(sql)

    for row in results:
        player = player_repository.select(row['player_id'])
        match = match_repository.select(row['match_id'])
        prediction = Prediction(player, match, row['id'])
        prediction.set_goals(row['home_goals'], row['away_goals'])
        predictions.append(prediction)
    return predictions

# Update
def update(prediction):
    sql = "UPDATE predictions SET (home_goals, away_goals) = (%s, %s) WHERE id = %s"
    values = [prediction.goals["home"], prediction.goals["away"], prediction.id]
    run_sql(sql, values)

# Delete
def delete(id):
    sql = "DELETE FROM predictions WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM predictions"
    run_sql(sql)

