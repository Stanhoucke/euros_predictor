from db.run_sql import run_sql
from models.league import League
from models.player import Player

# Create
def save(league):
    sql = "INSERT INTO leagues (name, join_code) VALUES (%s, %s) RETURNING id"
    values = [league.name, league.join_code]
    result = run_sql(sql, values)
    league.id = result[0]['id']
    return league

# Read
def select(id):
    league = None

    sql = "SELECT * FROM leagues WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        league = League(result['name'], result['id'])
        league.join_code = result['join_code']
    return league

def select_all():
    leagues = []

    sql = "SELECT * FROM leagues"
    results = run_sql(sql)

    for row in results:
        league = League(row['name'], row['id'])
        league.join_code = row['join_code']
        leagues.append(league)
    return leagues

def players(league):
    players = []

    sql = "SELECT players.* FROM players INNER JOIN player_leagues ON player_leagues.player_id = players.id WHERE player_leagues.league_id = %s ORDER BY points DESC"
    values = [league.id]
    results = run_sql(sql, values)

    for row in results:
        player = Player (row['email'], row['password'], row['first_name'], row['last_name'], row['team_name'], row['points'], row['id'])
        players.append(player)
    return players

def select_by_join_code(join_code):
    league = None

    sql = "SELECT * FROM leagues WHERE join_code = %s"
    values = [join_code]
    result = run_sql(sql, values)[0]

    if result is not None:
        league = League(result['name'], result['id'])
        league.join_code = result['join_code']
    return league

# Update
def update(league):
    sql = "UPDATE leagues SET name = %s WHERE id = %s"
    values = [league.name, league.id]
    run_sql(sql, values)

# Delete
def delete(id):
    sql = "DELETE FROM leagues WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM leagues"
    run_sql(sql)

