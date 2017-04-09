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

class Portfolio():

    def __init__(self):
        self.fund_count = 0

        self.profit = 0

        self.win_item = LotteryItem()
        self.draw_item = LotteryItem()
        self.lose_item = LotteryItem()

        self.win_percentage = 0
        self.draw_percentage = 0
        self.lose_percentage = 0

    def display(self):
        print "profit:\t%s\nwin:\t%s %s\t%s\t%s\ndraw:\t%s %s\t%s\t%s\nlose:\t%s %s\t%s\t%s" % \
              (self.profit,
               self.win_item.id, self.win_item.company, self.win_item.cw_odds, self.win_percentage,
               self.draw_item.id, self.draw_item.company, self.draw_item.cd_odds, self.draw_percentage,
               self.lose_item.id, self.lose_item.company, self.lose_item.cl_odds, self.lose_percentage)
