class Bookie():
    def __init__(self, name, id, fee):
        self.name = name
        self.id = id
        self.fee = fee

class Event():
    def __init__(self, name, id):
        self.name = name
        self.id = id
        
class EventOdds():
    def __init__(self, id, win, draw, lose):
        self.id = id
        self.win = win
        self.draw = draw
        self.lose = lose
