import pygame

class player:
    def __init__(self, _id, _color, _pos, _range):
        self.Player_Id = _id
        self.Player_color = _color
        self.Player_X = _pos[0]
        self.Player_Y = _pos[1]
        self.Player_range = _range
        
    def printPlayer(self):
        print("ID: ",self.Player_Id)
        print("Position: [",
              self.Player_X, " - ",self.Player_X + self.Player_range,
              "]","  [",
              self.Player_Y, " - ",self.Player_Y + self.Player_range,
              "]")
        
    def showPlayerVal(self):
        return self.Player_color,(self.player_X,self.Player_Y,self.Player_range,self.Player_range)