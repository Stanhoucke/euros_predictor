from models.team import Team
from models.group import Group

import repositories.team_repository as team_repository
import repositories.group_repository as group_repository


# Teams
team_1 = Team("France", {
            "played": 1,
            "won": 0,
            "drawn": 1,
            "lost": 0,
            "for": 2,
            "against": 2,
            "difference": 0,
            "points": 1,
            "rank": 1
        })
team_2 = Team("Germany", {
            "played": 1,
            "won": 0,
            "drawn": 1,
            "lost": 0,
            "for": 2,
            "against": 2,
            "difference": 0,
            "points": 1,
            "rank": 2
        })
team_3 = Team("Hungary", {
            "played": 1,
            "won": 0,
            "drawn": 0,
            "lost": 1,
            "for": 1,
            "against": 3,
            "difference": -2,
            "points": 0,
            "rank": 3
        })
team_4 = Team("Portugal", {
            "played": 1,
            "won": 1,
            "drawn": 0,
            "lost": 0,
            "for": 3,
            "against": 1,
            "difference": 2,
            "points": 3,
            "rank": 4
        })

team_repository.save(team_1)
team_repository.save(team_2)
team_repository.save(team_3)
team_repository.save(team_4)

# Groups
group_1 = Group("F")
group_1.teams = [team_1, team_2, team_3, team_4]

group_repository.save(group_1)

# Update
team_4.group_info["rank"] = 1
team_repository.update(team_4)

# Select
# selected_team = team_repository.select(team_1.id)
# print(selected_team.group_info["rank"])
# print(team_repository.select_all())

selected_group = group_repository.select(group_1.id)
print(selected_group.name)
print(group_repository.select_all)
