from db.run_sql import run_sql
from models.team import Team

# Create
def save(team):
    sql = "INSERT INTO teams (name, matches_played, won, drawn, lost, goals_for, goals_against, goal_difference, points, group_rank) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id"
    values = [team.name, team.group_info["played"], team.group_info["won"], team.group_info["drawn"], team.group_info["lost"], team.group_info["for"], team.group_info["against"], team.group_info["difference"], team.group_info["points"], team.group_info["rank"]]
    result = run_sql(sql, values)
    team.id = result[0]['id']
    return team

# Read

# Update

# Delete