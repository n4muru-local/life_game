
import pygame
class Field:
    def __init__(self,_screen):
        self.screen = _screen
        self.Window_X = 1000
        self.Window_Y = 500
        self.Cell_Size = 10
        self.Cell_state = [[0] * self.Window_X for i in range(self.Window_Y)]
    
    def set(self,_windowX,_windowY,_cellsize):
        self.Window_X = _windowX
        self.Window_Y = _windowY
        self.Cell_Size = _cellsize

    def setState(self, _list):
        try:
            self.Cell_state = _list.copy()
        except Exception as e:
            print(e.__class__.__name__)
            print(e.args)
            print(e)
            print(f"{e.__class__.__name__}: {e}")

    def drawLine(self):
        for i in range(0, self.Window_X, self.Cell_Size):
            pygame.draw.line(self.screen, (0,0,0), (i,0), (i,500), 1)
        for i in range(0,self.Window_Y,self.Cell_Size):
            pygame.draw.line(self.screen, (0,0,0), (0,i), (1000,i), 1)

    def drawCell(self):
        for y in range(0,self.Window_Y):
            for x in range(0,self.Window_X):
                pos_x = x * self.Cell_Size
                pos_y = y * self.Cell_Size
                size = self.Cell_Size
                if self.Cell_state == 1:
                    self.screen.fill((255,0,0), (pos_x, pos_y, pos_x+size, y+size))
                elif self.Cell_state == 2:
                    self.screen.fill((0,255,0), (pos_x, pos_y, pos_x+size, y+size))
                
    
