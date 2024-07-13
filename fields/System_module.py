
import pygame
from .field_module import Field
class SystemField(Field):

    def updateField(self):
        newField = [[0] * self.Window_X for i in range(self.Window_Y)]
        chex = [-1, 0, 1,-1, 1,-1, 0, 1]
        chey= [-1,-1,-1, 0, 0, 1, 1, 1]
        for i in range(self.Window_Y):
            for j in range(self.Window_X):
                aroundCell = []
                for n in range(8):
                    X = j + int(chex[n])
                    Y = i + int(chey[n])
                    if X == -1:
                        X = self.Window_X - 1
                    elif X == self.Window_X:
                        X = 0
                    if Y == -1:
                        Y = self.Window_Y - 1
                    elif Y == self.Window_Y:
                        Y = 0
                    aroundCell.append(self.Cell_state[Y][X])
                player_a = aroundCell.count(1)
                player_b = aroundCell.count(2)
                if player_a+player_b <= 1:
                    newField[i][j] = 0
                elif player_a+player_b <= 3:
                    if player_a-player_b > 0:
                        newField[i][j] = 1
                    elif player_a-player_b < 0:
                        newField[i][j] = 2
                    else:
                        newField[i][j] = 0
                elif player_a+player_b >= 4:
                    newField[i][j] = 0
        self.setState(newField)
                
    
    def setState(self, _list):
        try:
            self.Cell_state = _list.copy()
        except Exception as e:
            print(e.__class__.__name__)
            print(e.args)
            print(e)
            print(f"{e.__class__.__name__}: {e}")


    def getState(self):
        return self.Cell_state
    
    def printState(self):
        for list in self.Cell_state:
            print(list)
        