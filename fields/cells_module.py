import pygame
from . import field_module as fm

class Cell:
    def __init__(self,_grid_num, _size, _state):
        self.grid_row = _grid_num[1] # [0]:縦 [1]:横 field Size
        self.grid_col = _grid_num[0]
        self.cell_size = _size
        self.state =  _state
        self.next_state = self.state

    def pos(self):
        return [self.grid_row*self.cell_size, self.grid_col*self.cell_size]
  
    def set(self, _state):
        self.state = _state
    

    def updateState(self):
        self.state = self.next_state


    
'''
    def setCell(self, row, col, new_cell):
        if isinstance(new_cell, int):
            self.state = new_cell
        else:
            raise Exception('setする値が異なります。\n new_cell: type<int64>')

    def getCell(self):
        return self.state
    

    def countLiving(self, player = [1,2]):
        cnt = 0
        ret = []
        for id in player:
            for row in range(self.grid_row):
                for col in range(self.grid_col):
                    if self.getCell(row, col).state == id: cnt += 1
            ret.append(cnt)
        
        return ret, sum(ret)

    def count_around_cells(self, row, col, _state):
        # 周囲のあるstateであるセルをカウントする

        # チェックテーブルの作成
        check_row = [-1, -1, -1,  0,  0,  1,  1,  1]
        check_col = [-1,  0,  1, -1,  1, -1,  0,  1]
        check_row = [n + row for n in check_row]
        check_col = [n + col for n in check_col]
        # 端のセルは反対側を参照する
        check_row =  [0 if n==self.grid_row else n for n in check_row]
        check_col =  [0 if n==self.grid_col else n for n in check_col]
        check_row =  [self.grid_row-1 if n == -1 else n for n in check_row]
        check_col =  [self.grid_col-1 if n == -1 else n for n in check_col]

        cnt = 0
        for c_row, c_col in zip(check_row, check_col):
            #print(c_row, c_col)
            if self.get_cell(c_row, c_col).state == _state: cnt += 1
        return cnt
        
    def update_cells_state(self):
        # 次の状態を決定
        for row in range(self.grid_row):
            for col in range(self.grid_col):
                state_cnt_1 = self.count_around_cells(row, col, 1)
                state_cnt_2 = self.count_around_cells(row, col, 2)
                state_num = state_cnt_1 + state_cnt_2

                if self.get_cell(row, col) == 0:
                    # 誕生条件
                    if state_num == 3:
                        if state_cnt_1 > state_cnt_2:
                            self.get_cell(row, col).next_state = 1
                        elif  state_cnt_1 < state_cnt_2:
                            self.get_cell(row, col).next_state = 2
                elif self.get_cell(row, col) == 1:
                    # 生存条件
                    if state_num == 2 or state_num == 3:
                        self.get_cell(row, col).next_state = self.getCell(row, col)
                    else:
                        self.get_cell(row, col).next_state = 0
        # 次の状態に更新
        for row in range(self.grid_row):
            for col in range(self.grid_col):
                self.get_cell(row, col).update_state()
                
    def draw(self):
        for row in range(self.grid_size[0]):
            for col in range(self.grid_size[1]):
                self.get_cell(row, col).draw()
                '''