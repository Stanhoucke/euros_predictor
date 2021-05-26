from db.run_sql import run_sql
from models.player_team import PlayerTeam

import repositories.player_repository as player_repository
import repositories.team_repository as team_repository

# Create
def save(player_team):
    sql = "INSERT INTO player_teams (player_id, team_id, matches_played, won, drawn, lost, goals_for, goals_against, goal_difference, points, group_rank) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id"
    values = [player_team.player.id, player_team.team.id, player_team.group_info["played"], player_team.group_info["won"], player_team.group_info["drawn"], player_team.group_info["lost"], player_team.group_info["for"], player_team.group_info["against"], player_team.group_info["difference"], player_team.group_info["points"], player_team.group_info["rank"]]
    result = run_sql(sql, values)
    player_team.id = result[0]['id']
    return player_team

# Read
def select(id):
    player_team = None

    sql = "SELECT * FROM player_teams WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        player = player_repository.select(result['player_id'])
        team = team_repository.select(result['team_id'])
        group_info = {
            "played": result['matches_played'],
            "won": result['won'],
            "drawn": result['drawn'],
            "lost": result['lost'],
            "for": result['goals_for'],
            "against": result['goals_against'],
            "difference": result['goal_difference'],
            "points": result['points'],
            "rank": result['group_rank']
        }
        player_team = PlayerTeam(player, team, result['id'])
        player_team.group_info = group_info
    return player_team

def select_all():
    player_teams = []

    sql = "SELECT * FROM player_teams"
    results = run_sql(sql)

    for row in results:
        player = player_repository.select(row['player_id'])
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

def select_by_player(player_id):
    pass

# Update
def update(player_team):
    sql = "UPDATE player_teams SET (matches_played, won, drawn, lost, goals_for, goals_against, goal_difference, points, group_rank) = (%s, %s, %s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [player_team.group_info["played"], player_team.group_info["won"], player_team.group_info["drawn"], player_team.group_info["lost"], player_team.group_info["for"], player_team.group_info["against"], player_team.group_info["difference"], player_team.group_info["points"], player_team.group_info["rank"], player_team.id]
    run_sql(sql, values)

# Delete
def delete(id):
    sql = "DELETE FROM player_teams WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM player_teams"
    run_sql(sql)
