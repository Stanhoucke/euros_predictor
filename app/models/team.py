class Team():
    def __init__(self, name, id=None):
        self.name = name
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
        