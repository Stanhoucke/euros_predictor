from db.run_sql import run_sql
from models.player import Player
from models.league import League
from models.player_team import PlayerTeam
from models.prediction import Prediction
import repositories.team_repository as team_repository
import repositories.match_repository as match_repository

# Create
def save(player):
    player.hash_password()

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
        player = Player(result['email'], result['password'], result['first_name'], result['last_name'], result['team_name'], result['points'], result['id'])
    return player

def select_by_email(email):
    player = None

    sql = "SELECT * FROM players WHERE email = %s"
    values = [email]
    result = run_sql(sql, values)

    if len(result) > 0:
        result = result[0]
        player = Player(result['email'], result['password'], result['first_name'], result['last_name'], result['team_name'], result['points'], result['id'])
    return player

def select_all():
    players = []

    sql = "SELECT * FROM players"
    results = run_sql(sql)

    for row in results:
        player = Player(row['email'], row['password'], row['first_name'], row['last_name'], row['team_name'], row['points'])
        players.append(player)
    return players

def leagues(player):
    leagues = []

    sql = "SELECT leagues.* FROM leagues INNER JOIN player_leagues ON player_leagues.league_id = leagues.id WHERE player_leagues.player_id = %s"
    values = [player.id]
    results = run_sql(sql, values)

    for row in results:
        league = League(row['name'])
        leagues.append(league)
    return leagues

def player_teams(player):
    player_teams = []

    sql = "SELECT * FROM player_teams WHERE player_id = %s"
    values = [player.id]
    results = run_sql(sql, values)

    for row in results:
        team = team_repository.select(row['team_id'])
        player_team = PlayerTeam(player, team)
        player_teams.append(player_team)
    return player_teams

def predictions(player):
    predictions = []

    sql = "SELECT * FROM predictions WHERE player_id = %s"
    values = [player.id]
    results = run_sql(sql, values)

    for row in results:
        match = match_repository.select(row['match_id'])
        prediction = Prediction(player, match)
        predictions.append(prediction)
    return predictions

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

