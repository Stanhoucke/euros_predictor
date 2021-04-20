from db.run_sql import run_sql
from models.player_league import PlayerLeague
import repositories.player_repository as player_repository
import repositories.league_repository as league_repository

# Create
def save(player_league):
    sql = "INSERT INTO player_leagues (player_id, league_id) VALUES (%s, %s) RETURNING id"
    values = [player_league.player.id, player_league.league.id]
    result = run_sql(sql, values)
    player_league.id = result[0]['id']
    return player_league

# Read
def select(id):
    player_league = None

    sql = "SELECT * FROM player_leagues WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        player = player_repository.select(result['player_id'])
        league = league_repository.select(result['league_id'])
        player_league = PlayerLeague(league, player)
    return player_league

def select_all():
    player_leagues = []

    sql = "SELECT * FROM player_leagues"
    results = run_sql(sql)

    for row in results:
        player = player_repository.select(row['player_id'])
        league = league_repository.select(row['league_id'])
        player_league = PlayerLeague(league, player, row['id'])
        player_leagues.append(player_league)
    return player_leagues

# Delete
def delete(id):
    sql = "DELETE FROM player_leagues WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM player_leagues"
    run_sql(sql)
