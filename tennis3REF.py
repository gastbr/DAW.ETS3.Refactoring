# -*- coding: utf-8 -*-

class TennisGame3:
    def __init__(self, p1Name, p2Name):
        self.p1Name = p1Name
        self.p2Name = p2Name
        self.p1Points = 0
        self.p2Points = 0
        self.scores = ["Love", "Fifteen", "Thirty", "Forty"]        

    def Score(self, playerName):
        if playerName == self.p1Name:
            self.p1Points += 1
        elif playerName == self.p2Name:
            self.p2Points += 1
    
    def Winner(self):
        # Determina si la partida ha acabado y quién ha sido el ganador.
        # Si no ha acabado, devuelve "TDB" ("To be determined").
        winner = "TBD"
        if (self.p1Points >= 4 and self.p1Points > (self.p2Points + 1)):
            winner = "player1"        
        elif (self.p2Points >= 4 and self.p2Points > (self.p1Points + 1)):
            winner = "player2"
        return winner
        
    def ShowScore(self):
        if (self.Winner() != "TBD"): # Si nadie ha ganado aún
            result1 = "Win for "
            result2 = self.Winner()
            
        elif ((self.p1Points < 4 and self.p2Points < 4) and (self.p1Points + self.p2Points) < 6): # Si aún no llegaron al DEUCE
            result1 = self.scores[self.p1Points] 
            if (self.p1Points == self.p2Points):
                result2 = "-All"
            else:
                result2 = "-" + self.scores[self.p2Points]
                
        else:
            if (self.p1Points == self.p2Points):
                result1 = "Deuce"
                result2 = ""
            else:
                result1 = "Advantage "
                if (self.p1Points > self.p2Points):
                    result2 = "player1"
                else:
                    result2 = "player2"         
        
        return result1 + result2