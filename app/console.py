# API Connection

###

# import http.client
# import json

# conn = http.client.HTTPSConnection("v3.football.api-sports.io")

# headers = {
#     'x-rapidapi-host': "v3.football.api-sports.io",
#     'x-rapidapi-key': "ef86cf2f6eabdec8263cf20a190a764e"
#     }

# conn.request("GET", "/fixtures?league=4&season=2016&team=2", headers=headers) # Requests/queries go here in this format

# res = conn.getresponse()
# data = res.read()

# response = json.loads(data)
# # print(data.decode("utf-8"))
# print(response["response"][0])

###





from models.player import Player
from models.team import Team
from models.group import Group
from models.match import Match
from models.league import League
from models.player_league import PlayerLeague
from models.player_team import PlayerTeam

import repositories.player_repository as player_repository
import repositories.team_repository as team_repository
import repositories.group_repository as group_repository
import repositories.match_repository as match_repository
import repositories.league_repository as league_repository
import repositories.player_league_repository as player_league_repository
import repositories.player_team_repository as player_team_repository

# Players
player_1 = Player("euros@gmail.com", "password1", "John", "Smith", "Hopp Suisse")
player_repository.save(player_1)

# Teams
team_1 = Team("France")
team_1.group_info = {
            "played": 1,
            "won": 0,
            "drawn": 1,
            "lost": 0,
            "for": 2,
            "against": 2,
            "difference": 0,
            "points": 1,
            "rank": 1
        }
team_2 = Team("Germany")
team_2.group_info = {
            "played": 1,
            "won": 0,
            "drawn": 1,
            "lost": 0,
            "for": 2,
            "against": 2,
            "difference": 0,
            "points": 1,
            "rank": 2
        }
team_3 = Team("Hungary")
team_3.group_info = {
            "played": 1,
            "won": 0,
            "drawn": 0,
            "lost": 1,
            "for": 1,
            "against": 3,
            "difference": -2,
            "points": 0,
            "rank": 3
        }
team_4 = Team("Portugal")
team_4.group_info = {
            "played": 1,
            "won": 1,
            "drawn": 0,
            "lost": 0,
            "for": 3,
            "against": 1,
            "difference": 2,
            "points": 3,
            "rank": 4
        }
team_repository.save(team_1)
team_repository.save(team_2)
team_repository.save(team_3)
team_repository.save(team_4)

# Groups
group_1 = Group("A")
group_1.teams = [team_1, team_2, team_3, team_4]

group_repository.save(group_1)

# Matches
match_1 = Match(team_1, team_2)
match_repository.save(match_1)

# Leagues
league_1 = League("Wilton Wanderers")
league_repository.save(league_1)

# Player Leagues
player_league_1 = PlayerLeague(league_1, player_1)
player_league_repository.save(player_league_1)

# Player Teams
player_team_1 = PlayerTeam(player_1, team_4)
player_team_2 = PlayerTeam(player_1, team_3)
player_team_3 = PlayerTeam(player_1, team_2)
player_team_4 = PlayerTeam(player_1, team_1)
player_team_repository.save(player_team_1)
player_team_repository.save(player_team_2)
player_team_repository.save(player_team_3)
player_team_repository.save(player_team_4)


# Update
player_1.first_name = "Guillaume"
player_1.last_name = "Tell"
player_repository.update(player_1)

team_4.group_info["rank"] = 1
team_repository.update(team_4)

group_1.name = "F"
group_repository.update(group_1)

match_1.set_goals(4,3)
match_repository.update(match_1)

league_1.name = "Wonky Badgers"
league_repository.update(league_1)

player_team_1.group_info["for"] = 3
player_team_repository.update(player_team_1)

# # Select
# selected_player = player_repository.select(player_1.id)
# print(selected_player.full_name())
# print(player_repository.select_all())

# selected_team = team_repository.select(team_1.id)
# print(selected_team.group_info["rank"])
# print(team_repository.select_all())

# selected_group = group_repository.select(group_1.id)
# print(selected_group.name)
# print(group_repository.select_all())

# selected_match = match_repository.select(match_1.id)
# print(selected_match.team_1.name)
# print(match_repository.select_all())

# selected_league = league_repository.select(league_1.id)
# print(selected_league.name)
# print(league_repository.select_all())

# selected_player_league = player_league_repository.select(player_league_1.id)
# print(selected_player_league.player.full_name())
# print(player_league_repository.select_all())

# selected_player_team = player_team_repository.select(player_team_1.id)
# print(selected_player_team)
# print(player_team_repository.select_all())
