class PlayerTeam():
    def __init__(self, player, team, id=None):
        self.player = player
        self.team = team
        self.group_info = {
            "played": 0,
            "won": 0,
            "drawn": 0,
            "lost": 0,
            "for": 0,
            "against": 0,
            "difference": 0,
            "points": 0,
            "rank": None
        }
        self.id = id
