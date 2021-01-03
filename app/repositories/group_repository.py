from db.run_sql import run_sql
from models.group import Group
from models.team import Team

import repositories.team_repository as team_repository


# Create
def save(group):
    sql = "INSERT INTO groups (name, team_1_id, team_2_id, team_3_id, team_4_id) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [group.name, group.teams[0].id, group.teams[1].id, group.teams[2].id, group.teams[3].id]
    result = run_sql(sql, values)
    group.id = result[0]['id']
    return group

# Read
def select(id):
    group = None

    sql = "SELECT * FROM groups WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        team_1 = team_repository.select(result['team_1_id'])
        team_2 = team_repository.select(result['team_2_id'])
        team_3 = team_repository.select(result['team_3_id'])
        team_4 = team_repository.select(result['team_4_id'])
        teams = [team_1, team_2, team_3, team_4]
        group = Group(result['name'], teams, result['id'])
    return group

def select_all():
    groups = []

    sql = "SELECT * FROM groups"
    results = run_sql(sql)

    for row in results:
        team_1 = team_repository.select(row['team_1_id'])
        team_2 = team_repository.select(row['team_2_id'])
        team_3 = team_repository.select(row['team_3_id'])
        team_4 = team_repository.select(row['team_4_id'])
        teams = [team_1, team_2, team_3, team_4]
        group = Group(row['name'], teams, row['id'])
        groups.append(group)
    return groups

# Update


# Delete