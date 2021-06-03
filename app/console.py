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
from models.player_group import PlayerGroup
from models.team import Team
from models.group import Group
from models.match import Match
from models.league import League
from models.player_league import PlayerLeague
from models.player_team import PlayerTeam
from models.prediction import Prediction
from models.blacklist import Blacklist

import repositories.player_repository as player_repository
import repositories.team_repository as team_repository
import repositories.group_repository as group_repository
import repositories.player_group_repository as player_group_repository
import repositories.match_repository as match_repository
import repositories.league_repository as league_repository
import repositories.player_league_repository as player_league_repository
import repositories.player_team_repository as player_team_repository
import repositories.prediction_repository as prediction_repository
import repositories.blacklist_token_repository as blacklist_token_repository

new_group_info = {
    "played": 0,
    "won": 0,
    "drawn": 0,
    "lost": 0,
    "for": 0,
    "against": 0,
    "difference": 0,
    "points": 0,
    "rank": 0
}

# Players
player_1 = Player("euros@gmail.com", "password1", "John", "Smith", "Hopp Suisse")
player_repository.save(player_1)
player_2 = Player("stan@gmail.com", "password", "Stan", "H", "Footy")
player_repository.save(player_2)

# Teams
team_1 = Team("France")
team_2 = Team("Switzerland")
team_3 = Team("Albania")
team_4 = Team("Romania")
team_repository.save(team_1)
team_repository.save(team_2)
team_repository.save(team_3)
team_repository.save(team_4)

team_5 = Team("Wales")
team_6 = Team("England")
team_7 = Team("Slovakia")
team_8 = Team("Russia")
team_repository.save(team_5)
team_repository.save(team_6)
team_repository.save(team_7)
team_repository.save(team_8)

team_9 = Team("Germany")
team_10 = Team("Poland")
team_11 = Team("Northern Ireland")
team_12 = Team("Ukraine")
team_repository.save(team_9)
team_repository.save(team_10)
team_repository.save(team_11)
team_repository.save(team_12)

team_13 = Team("Croatia")
team_14 = Team("Spain")
team_15 = Team("Turkey")
team_16 = Team("Czech Republic")
team_repository.save(team_13)
team_repository.save(team_14)
team_repository.save(team_15)
team_repository.save(team_16)

team_17 = Team("Italy")
team_18 = Team("Belgium")
team_19 = Team("Republic of Ireland")
team_20 = Team("Sweden")
team_repository.save(team_17)
team_repository.save(team_18)
team_repository.save(team_19)
team_repository.save(team_20)

team_21 = Team("Hungary")
team_22 = Team("Iceland")
team_23 = Team("Portugal")
team_24 = Team("Austria")
team_repository.save(team_21)
team_repository.save(team_22)
team_repository.save(team_23)
team_repository.save(team_24)

# Groups
group_1 = Group("A")
group_1.teams = [team_1, team_2, team_3, team_4]
group_repository.save(group_1)

group_2 = Group("B")
group_2.teams = [team_5, team_6, team_7, team_8]
group_repository.save(group_2)

group_3 = Group("C")
group_3.teams = [team_9, team_10, team_11, team_12]
group_repository.save(group_3)

group_4 = Group("D")
group_4.teams = [team_13, team_14, team_15, team_16]
group_repository.save(group_4)

group_5 = Group("E")
group_5.teams = [team_17, team_18, team_19, team_20]
group_repository.save(group_5)

group_6 = Group("F")
group_6.teams = [team_21, team_22, team_23, team_24]
group_repository.save(group_6)

# Matches
# Day 1
match_1 = Match(team_1, team_4)
match_repository.save(match_1)
match_2 = Match(team_2, team_3)
match_repository.save(match_2)
match_3 = Match(team_5, team_7)
match_repository.save(match_3)
match_4 = Match(team_6, team_8)
match_repository.save(match_4)
match_5 = Match(team_15, team_13)
match_repository.save(match_5)
match_6 = Match(team_10, team_11)
match_repository.save(match_6)
match_7 = Match(team_9, team_12)
match_repository.save(match_7)
match_8 = Match(team_14, team_16)
match_repository.save(match_8)
match_9 = Match(team_19, team_20)
match_repository.save(match_9)
match_10 = Match(team_17, team_18)
match_repository.save(match_10)
match_11 = Match(team_24, team_21)
match_repository.save(match_11)
match_12 = Match(team_23, team_22)
match_repository.save(match_12)


# Leagues
league_1 = League("Wilton Wanderers")
league_repository.save(league_1)

# Player Leagues
player_league_1 = PlayerLeague(league_1, player_1)
player_league_repository.save(player_league_1)

# Player Teams
# player_team_1 = PlayerTeam(player_1, team_1)
# player_team_2 = PlayerTeam(player_1, team_2)
# player_team_3 = PlayerTeam(player_1, team_3)
# player_team_4 = PlayerTeam(player_1, team_4)
# player_team_repository.save(player_team_1)
# player_team_repository.save(player_team_2)
# player_team_repository.save(player_team_3)
# player_team_repository.save(player_team_4)
# player_teams_1 = [player_team_1, player_team_2, player_team_3, player_team_4]

for team in team_repository.select_all():
    player_team_repository.save(PlayerTeam(player_1, team))

# Player Groups

for group in group_repository.select_all():
    player_teams = []
    for team in group.teams:
        player_teams.append(player_team_repository.select_by_player_and_team(player_1, team))
    player_group_repository.save(PlayerGroup(player_1, group.name, player_teams))

# player_group_1 = PlayerGroup(player_1, group_1.name, player_teams_1)
# player_group_repository.save(player_group_1)

# Predictions
matches = [match_1, match_2, match_3, match_4, match_5, match_6]
for match in match_repository.select_all():
    home_player_team = player_team_repository.select_by_player_and_team(player_1, match.team_1)
    away_player_team = player_team_repository.select_by_player_and_team(player_1, match.team_2)
    prediction_repository.save(Prediction(player_1, match, home_player_team, away_player_team))
# prediction_1 = Prediction(player_1, match_1, player_team_1, player_team_2)
# prediction_repository.save(prediction_1)

# Update
# player_1.first_name = "Guillaume"
# player_1.last_name = "Tell"
# player_repository.update(player_1)

# team_4.group_info["rank"] = 1
# team_repository.update(team_4)

# group_1.name = "F"
# group_repository.update(group_1)

# match_1.set_goals(4,3)
# match_repository.update(match_1)

# league_1.name = "Wonky Badgers"
# league_repository.update(league_1)

# player_team_1.group_info["for"] = 3
# player_team_repository.update(player_team_1)

# prediction_1.set_goals(3, 1)
# prediction_repository.update(prediction_1)

# blacklist_token_1 = Blacklist("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c")
# blacklist_token_repository.save(blacklist_token_1)

# # Select
# selected_player = player_repository.select(player_1.id)
# selected_player = player_repository.select_by_email("stan@gmail.com")
# print(selected_player.full_name())
# print(player_repository.select_all())
# print(player_repository.leagues(player_1))

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
# print(league_repository.players(league_1)[0].full_name())

# selected_player_league = player_league_repository.select(player_league_1.id)
# print(selected_player_league.player.full_name())
# print(player_league_repository.select_all())

# selected_player_team = player_team_repository.select(player_team_1.id)
# print(selected_player_team.id)
# print(player_team_repository.select_all())
# selected_player_team = player_team_repository.select_by_player_and_team(player_1, team_2)
# print(selected_player_team.id)

# selected_prediction = prediction_repository.select(prediction_1.id)
# print(selected_prediction.player.full_name())
# print(prediction_repository.select_all())


# print(blacklist_token_repository.check_blacklist("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"))