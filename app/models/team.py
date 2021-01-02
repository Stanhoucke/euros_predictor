class Team():
    def __init__(self, name, group_rank, matches_played=0, points=0, goals_for=0, goals_against=0, goal_difference=0, id=None):
        self.name = name
        self.group_rank = group_rank
        self.matches_played = matches_played
        self.points = points
        self.goals_for = goals_for
        self.goals_against = goals_against
        self.goal_difference = goal_difference
        self.id = id
        