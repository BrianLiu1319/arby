from dataclasses import dataclass

@dataclass
class TeamS:
    name: str
    odd : str
    time: str
    event: str
        
    def __init__(self, name, odd, time, event):
        self.name = name
        self.odd = odd
        self.time = time
        self.event = event