# -*- coding: utf-8 -*-

class TennisGame3:
    def __init__(self, p1Name, p2Name):
        self.p1Name = p1Name
        self.p2Name = p2Name
        self.p1Points = 0
        self.p2Points = 0

    def won_point(self, playerName):
        if playerName == self.p1Name:
            self.P1Score()
        elif playerName == self.p2Name:
            self.P2Score()

    def score(self):
        if (self.p1Points < 4 and self.p2Points < 4) and (self.p1Points + self.p2Points < 6):
            p = ["Love", "Fifteen", "Thirty", "Forty"]
            s = p[self.p1Points]
            return s + "-All" if (self.p1Points == self.p2Points) else s + "-" + p[self.p2Points]
        else:
            if (self.p1Points == self.p2Points):
                return "Deuce"
            s = self.p1Name if self.p1Points > self.p2Points else self.p2Name
            return "Advantage " + s if ((self.p1Points-self.p2Points)*(self.p1Points-self.p2Points) == 1) else "Win for " + s

    def SetP1Score(self, number):
        for i in range(number):
            self.P1Score()

    def SetP2Score(self, number):
        for i in range(number):
            self.P2Score()

    def P1Score(self):
        self.p1Points += 1


    def P2Score(self):
        self.p2Points += 1