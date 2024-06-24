from dataclasses import dataclass

@dataclass
class Team:
    name: str
    odd_rv : float
    odd_tp : float
            
    def __init__(self, name, odd_rv, odd_tp ):
        self.name = name
        self.odd_rv = odd_rv
        self.odd_tp = odd_tp
        
@dataclass
class match:
    date: str
    team_a : Team
    team_b : Team
    
    def __init__(self, date, team_a, team_b):
        self.date = date
        self.team_a = team_a
        self.team_b = team_b
        