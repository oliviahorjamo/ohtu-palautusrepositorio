class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.goals = dict['goals']
        self.assists = dict['assists']
        self.team = dict['team']
        self.nationality = dict['nationality']
    
    def __str__(self):
        return f"{self.name:20}{self.team:3}{self.goals:3} + {self.assists:3} = {self.goals + self.assists:3}"
