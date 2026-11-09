class Player:
    def __init__(self, player_player_dict):
        self.name = player_player_dict['name']
        self.nationality = player_player_dict['nationality']
        self.team = player_player_dict['team']
        self.goals = player_player_dict['goals']
        self.assists = player_player_dict['assists']

    @property
    def points(self):
        return self.goals + self.assists

    def __str__(self):
        return f"{self.name:20} {self.team:15} {self.goals:2} + {self.assists:2} = {self.points}"
