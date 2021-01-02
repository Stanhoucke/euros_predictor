from models.team import Team

class Group():
    def __init__(self, name, teams=[], id=None):
        self.name = name
        self.teams = teams
        self.id = id

    def assign_rank(self):
        self.teams.sort(reverse=True, key=lambda team: team.group_info["points"])
        
        rank = 1
        for team in self.teams:
            team.group_info["rank"] = rank
            rank += 1

