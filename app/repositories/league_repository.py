from db.run_sql import run_sql
from models.league import League

# Create
def save(league):
    sql = "INSERT INTO leagues (name, join_code) VALUES (%s, %s) RETURNING id"
    values = [league.name, league.join_code]
    result = run_sql(sql, values)
    league.id = result[0]['id']
    return league

