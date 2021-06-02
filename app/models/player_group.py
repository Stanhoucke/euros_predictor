class PlayerGroup():
    def __init__(self, player, name, player_teams=[], id=None):
        self.player = player
        self.name = name
        self.player_teams = player_teams
        self.id = id

    def assign_rank(self):
        self.player_teams.sort(reverse=True, key=lambda team: team.group_info["points"])
        
        rank = 1
        for team in self.player_teams:
            team.group_info["rank"] = rank
            rank += 1

