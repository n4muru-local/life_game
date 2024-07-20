import pygame
import numpy as np
from . import cells_module as cm

class Field:
    def __init__(self, _screen):
        self.screen = _screen
        self.Window_X = 1000
        self.Window_Y = 500
        self.cell_size = 10
        self.grid_row = int(self.Window_Y/self.cell_size)
        self.grid_col = int(self.Window_X/self.cell_size)
        self.cells = self.setupCells()

    def setupCells(self):
        cl = []
        for row in range(0, int(self.Window_Y/self.cell_size)):
            colum = []
            for col in range(0, int(self.Window_X/self.cell_size)):
                colum.append(cm.Cell([row,col],self.cell_size,0))
            cl.append(colum)
        return cl
    
    def getCell(self, row , col):
        return self.cells[row][col]
    
    def count_around_cells(self, row, col, _state):
        # 周囲のあるstateであるセルをカウントする
        offsets = [
                (-1, -1), (-1, 0), (-1, 1), 
                ( 0, -1),          ( 0, 1), 
                ( 1, -1), ( 1, 0), ( 1, 1)]
        cnt = 0
        # 端のセルは反対側を参照する
        for dr, dc in offsets:
            # ラップアラウンド処理
            r = (row + dr) % self.grid_row
            c = (col + dc) % self.grid_col

            if self.cells[r][c].state == _state:
                cnt += 1
        return cnt
    
    def update_cells_state(self):
        # 次の状態を決定
        for row in range(self.grid_row):
            for col in range(self.grid_col):
                state_cnt_1 = self.count_around_cells(row, col, 1)
                state_cnt_2 = self.count_around_cells(row, col, 2)
                state_num = state_cnt_1 + state_cnt_2

                cell = self.cells[row][col]
                if cell.state == 0:
                    # 誕生条件
                    if state_num == 3:
                        if state_cnt_1 > state_cnt_2:
                            cell.next_state = 1
                        elif  state_cnt_1 < state_cnt_2:
                            cell.next_state = 2
                elif cell.state == 1:
                    # 生存条件
                    if state_num == 2 or state_num == 3:
                        cell.next_state = cell.state
                    else:
                        cell.next_state = 0
        # 次の状態に更新
        for row in range(self.grid_row):
            for col in range(self.grid_col):
                self.cells[row][col].updateState()


    def getState(self):
        padd_array = np.pad(self.state, pad_width=1, mode='wrap')
        return padd_array


    def drawCell(self):
        for row in range(0, int(self.Window_Y/self.cell_size)):
            for col in range(0, int(self.Window_X/self.cell_size)):
                cell = self.cells[row][col]
                if cell.state == 1:
                    pygame.draw.rect(self.screen, (255,0,0), (cell.pos()[0], cell.pos()[1], self.cell_size, self.cell_size))
                elif cell.state == 2:
                    pygame.draw.rect(self.screen, (0,255,0), (cell.pos()[0], cell.pos()[1], self.cell_size, self.cell_size))
                elif cell.state == 0:
                    pygame.draw.rect(self.screen, (255, 255, 255), (cell.pos()[0], cell.pos()[1], self.cell_size, self.cell_size))

    def drawLine(self):
        for row in range(0, self.Window_Y,self.cell_size):
            pygame.draw.line(self.screen, (0,0,0), (0,row), (self.Window_X,row), 1)
        for col in range(0,self.Window_X,self.cell_size):
            pygame.draw.line(self.screen, (0,0,0), (col,0), (col,self.Window_Y), 1)