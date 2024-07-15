import pygame

class Field:
    def __init__(self, _screen):
        self.screen = _screen
        self.Window_X = 1000
        self.Window_Y = 500
        self.Cell_Size = 10
        self.Cell_state = [[0] * self.Window_X for i in range(self.Window_Y)]
    
    #基本設定
    def set(self,_windowX,_windowY,_cellsize):
        self.Window_X = _windowX
        self.Window_Y = _windowY
        self.Cell_Size = _cellsize
    
    #配列設定
    def setState(self, _list):
        try:
            self.Cell_state = _list.copy()
        except Exception as e:
            print(e.__class__.__name__)
            print(e.args)
            print(e)
            print(f"{e.__class__.__name__}: {e}")
            
    
    
    #配列の取得
    def getState(self):
        return self.Cell_state
    
    #配列のターミナル出力
    def printState(self):
        for list in self.Cell_state:
            print(*list,sep='')

    def printField(self):
        print("window_size:",
            self.Window_X,
            " ,  ",
            self.Window_Y)
        print("Cell Size = ", self.Cell_Size)
        
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
                    
    def updateField(self):
        newField = self.getState().copy()
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
                else:
                    newField[i][j] = 0
        self.setState(newField)
