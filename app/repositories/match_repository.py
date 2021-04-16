from db.run_sql import run_sql
from models.match import Match

# Create
def save(match):
    sql = "INSERT INTO matches (team_1_id, team_2_id) VALUES (%s, %s) RETURNING id"
    values = [match.team_1.id, match.team_2.id]
    result = run_sql(sql, values)
    match.id = result[0]['id']
    return match

# Read


# Update


# Delete


