import pygame
from .field_module import Field
class ShowField(Field):

    def drawLine(self):
        for i in range(0, self.Window_X, self.Cell_Size):
            pygame.draw.line(self.screen, (0,0,0), (i,0), (i,500), 1)
        for i in range(0,self.Window_Y,self.Cell_Size):
            pygame.draw.line(self.screen, (0,0,0), (0,i), (1000,i), 1)

    def drawCell(self):
        for y in range(0,int(self.Window_Y / self.Cell_Size)):
            for x in range(0, int(self.Window_X / self.Cell_Size)):
                pos_x = x * self.Cell_Size
                pos_y = y * self.Cell_Size
                size = self.Cell_Size
                if self.Cell_state[y][x] == 1:
                    #self.screen.fill((255,0,0), (pos_x, pos_y, size, size))
                    pygame.draw.rect(self.screen,(255,0,0), (pos_x, pos_y, size, size))
                elif self.Cell_state[y][x] == 2:
                    pygame.draw.rect(self.screen,(0,255,0), (pos_x, pos_y, size, size))
                
    
