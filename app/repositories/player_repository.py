from db.run_sql import run_sql
from models.player import Player
from models.league import League
from models.player_group import PlayerGroup
from models.player_team import PlayerTeam
from models.prediction import Prediction
import repositories.team_repository as team_repository
import repositories.match_repository as match_repository
import repositories.player_team_repository as player_team_repository

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
        player = Player(row['email'], row['password'], row['first_name'], row['last_name'], row['team_name'], row['points'], row['id'])
        players.append(player)
    return players

def leagues(player):
    leagues = []

    sql = "SELECT leagues.* FROM leagues INNER JOIN player_leagues ON player_leagues.league_id = leagues.id WHERE player_leagues.player_id = %s"
    values = [player.id]
    results = run_sql(sql, values)

    for row in results:
        league = League(row['name'], row['id'])
        league.join_code = row['join_code']
        leagues.append(league)
    return leagues

def player_teams(player):
    player_teams = []

    sql = "SELECT * FROM player_teams WHERE player_id = %s"
    values = [player.id]
    results = run_sql(sql, values)

    for row in results:
        team = team_repository.select(row['team_id'])
        group_info = {
            "played": row['matches_played'],
            "won": row['won'],
            "drawn": row['drawn'],
            "lost": row['lost'],
            "for": row['goals_for'],
            "against": row['goals_against'],
            "difference": row['goal_difference'],
            "points": row['points'],
            "rank": row['group_rank']
        }
        player_team = PlayerTeam(player, team, row['id'])
        player_team.group_info = group_info
        player_teams.append(player_team)
    return player_teams

def player_groups(player):
    player_groups = []

    sql = "SELECT * FROM player_groups WHERE player_id = %s"
    values = [player.id]
    results = run_sql(sql, values)

    for row in results:
        player_teams = []
        player_teams.append(player_team_repository.select(row['team_1_id']))
        player_teams.append(player_team_repository.select(row['team_2_id']))
        player_teams.append(player_team_repository.select(row['team_3_id']))
        player_teams.append(player_team_repository.select(row['team_4_id']))
        player_group = PlayerGroup(player, row['name'], player_teams, row['id'])
        player_groups.append(player_group)
    return player_groups

def predictions(player):
    predictions = []

    sql = "SELECT * FROM predictions WHERE player_id = %s"
    values = [player.id]
    results = run_sql(sql, values)

    for row in results:
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
        prediction.set_goals(row['home_goals'], row['away_goals'])
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

