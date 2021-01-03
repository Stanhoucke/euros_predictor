from db.run_sql import run_sql
from models.group import Group


# Create
def save(group):
    sql = "INSERT INTO groups (name, team_1_id, team_2_id, team_3_id, team_4_id) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [group.name, group.teams[0].id, group.teams[1].id, group.teams[2].id, group.teams[3].id]
    result = run_sql(sql, values)
    group.id = result[0]['id']
    return group

# Read


# Update


# Delete