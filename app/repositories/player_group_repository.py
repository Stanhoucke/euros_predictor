from db.run_sql import run_sql
from models.player_group import PlayerGroup
from models.player_team import PlayerTeam

import repositories.player_team_repository as player_team_repository
import repositories.player_repository as player_repository

# Create
def save(group):
    sql = "INSERT INTO player_groups (player_id, name, team_1_id, team_2_id, team_3_id, team_4_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"
    values = [group.player.id, group.name, group.player_teams[0].id, group.player_teams[1].id, group.player_teams[2].id, group.player_teams[3].id]
    result = run_sql(sql, values)
    group.id = result[0]['id']
    return group

# Read
def select(id):
    group = None

    sql = "SELECT * FROM player_groups WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        player = player_repository.select(result['player_id'])
        team_1 = player_team_repository.select(result['team_1_id'])
        team_2 = player_team_repository.select(result['team_2_id'])
        team_3 = player_team_repository.select(result['team_3_id'])
        team_4 = player_team_repository.select(result['team_4_id'])
        player_teams = [team_1, team_2, team_3, team_4]
        group = PlayerGroup(player, result['name'], player_teams, result['id'])
    return group

def select_all():
    player_groups = []

    sql = "SELECT * FROM player_groups"
    results = run_sql(sql)

    for row in results:
        player = player_repository.select(row['player_id'])
        team_1 = player_team_repository.select(row['team_1_id'])
        team_2 = player_team_repository.select(row['team_2_id'])
        team_3 = player_team_repository.select(row['team_3_id'])
        team_4 = player_team_repository.select(row['team_4_id'])
        player_teams = [team_1, team_2, team_3, team_4]
        group = PlayerGroup(player, row['name'], player_teams, row['id'])
        player_groups.append(group)
    return player_groups

# Update
def update(group):
    sql = "UPDATE player_groups SET (name, team_1_id, team_2_id, team_3_id, team_4_id) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [group.name, group.player_teams[0].id, group.player_teams[1].id, group.player_teams[2].id, group.player_teams[3].id, group.id]
    run_sql(sql, values)
    
# Delete
def delete(id):
    sql = "DELETE FROM player_groups WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM player_groups"
    run_sql(sql)

