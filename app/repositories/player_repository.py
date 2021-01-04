from db.run_sql import run_sql
from models.player import Player

# Create
def save(player):
    sql = "INSERT INTO players (email, password, first_name, last_name, team_name, points) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"
    values = [player.email, player.password, player.first_name, player.last_name, player.team_name, player.points]
    result = run_sql(sql, values)
    player.id = result[0]['id']
    return player

# Read
def select(id):
    player = None

    sql = "SELECT * FROM players WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        player = Player(result['email'], result['password'], result['first_name'], result['last_name'], result['team_name'], result['points'])
    return player

def select_all():
    players = []

    sql = "SELECT * FROM players"
    results = run_sql(sql)

    for row in results:
        player = Player (row['email'], row['password'], row['first_name'], row['last_name'], row['team_name'], row['points'])
        players.append(player)
    return players

# Update
def update(player):
    sql = "UPDATE players SET (email, password, first_name, last_name, team_name, points) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [player.email, player.password, player.first_name, player.last_name, player.team_name, player.points, player.id]
    run_sql(sql, values)

# Delete
def delete(id):
    sql = "DELETE FROM players WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM players"
    run_sql(sql)

