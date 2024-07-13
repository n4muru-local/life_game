import pygame
class Field:
    def __init__(self, _screen):
        self.screen = _screen
        self.Window_X = 1000
        self.Window_Y = 500
        self.Cell_Size = 10
        self.Cell_state = [[0] * self.Window_X for i in range(self.Window_Y)]
    
    def set(self,_windowX,_windowY,_cellsize):
        self.Window_X = _windowX
        self.Window_Y = _windowY
        self.Cell_Size = _cellsize

    def printField(self):
        print("window_size:",
              self.Window_X,
              " ,  ",
              self.Window_Y)
        print("Cell Size = ", self.Cell_Size)