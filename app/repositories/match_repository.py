from db.run_sql import run_sql
from models.match import Match
from models.team import Team

import repositories.team_repository as team_repository

# Create
def save(match):
    sql = "INSERT INTO matches (team_1_id, team_2_id, home_goals, away_goals) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [match.team_1.id, match.team_2.id, match.goals["home"], match.goals["away"]]
    result = run_sql(sql, values)
    match.id = result[0]['id']
    return match

# Read
def select(id):
    match = None

    sql = "SELECT * FROM matches WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        team_1 = team_repository.select(result['team_1_id'])
        team_2 = team_repository.select(result['team_2_id'])
        match = Match(team_1, team_2, result['id'])
        match.set_goals(result['home_goals'], result['away_goals'])
    return match

def select_all():
    matches = []

    sql = "SELECT * FROM matches"
    results = run_sql(sql)

    for row in results:
        team_1 = team_repository.select(row['team_1_id'])
        team_2 = team_repository.select(row['team_2_id'])
        match = Match(team_1, team_2, row['id'])
        match.set_goals(row['home_goals'], row["away_goals"])
        matches.append(match)
    return matches

# Update
def update(match):
    sql = "UPDATE matches SET (team_1_id, team_2_id, home_goals, away_goals) = (%s, %s, %s, %s) WHERE id = %s"
    values = [match.team_1.id, match.team_2.id, match.goals["home"], match.goals["away"], match.id]
    run_sql(sql, values)

# Delete
def delete(id):
    sql = "DELETE FROM matches WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM matches"
    run_sql(sql)

