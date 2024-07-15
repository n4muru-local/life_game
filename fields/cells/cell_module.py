import pygame


class Cell:
    def __init__(self, _screen, _size, _pos, _state):
        self.screen = _screen
        self.size = _size
        self.pos = _pos
        self.state = _state

    def draw(self):
        if self.state == 1:
            pygame.draw.rect(self.screen, (255,0,0), (self.pos[0], self.pos[1], self.size, self.size))
        elif self.state == 2:
            pygame.draw.rect(self.screen, (0,255,0), (self.pos[0], self.pos[1], self.size, self.size))
        elif self.state == 0:
            pygame.draw.rect(self.screen, (0, 0, 0), (self.pos[0], self.pos[1], self.size, self.size))

class Cells:
    def __init__(self, _screen, _grid_size, _cell_size):
        self.screen = _screen
        self.grid_size = _grid_size # 縦横それぞれ何個cellが並ぶか
        self.cell_size = _cell_size
        self.ar = self.create_cells()
    
    def create_cells(self):
        cells = []
        for row in range(self.grid_size[0]):
            cells_row = []
            for col in range(self.grid_size[1]):
                pos = (row * self.cell_size, col * self.cell_size)
                cell = Cell(self.screen, self.cell_size, pos, 0)
                cells_row.append(cell)
            cells.append(cells_row)
        return cells

    def get_cell(self, row, col):
        return self.ar[row][col]
    
    def set_cell(self, row, col, new_cell):
        self.ar[row][col] = new_cell
    
    def count_living(self):
        cnt = 0
        for row in range(self.grid_size[0]):
            for col in range(self.grid_size[1]):
                if self.get_cell(row, col).state != 0: cnt += 1
        return cnt

    def count_around_cells(self, row, col, state):
        # 周囲のあるstateであるセルをカウントする

        # チェックテーブルの作成
        check_row = [-1, -1, -1,  0,  0,  1,  1,  1]
        check_col = [-1,  0,  1, -1,  1, -1,  0,  1]
        check_row = [n + row for n in check_row]
        check_col = [n + col for n in check_col]
        # 端のセルは反対側を参照する
        check_row =  [0 if n==self.grid_size[0] else n for n in check_row]
        check_col =  [0 if n==self.grid_size[1] else n for n in check_col]
        check_row =  [self.grid_size[0]-1 if n == -1 else n for n in check_row]
        check_col =  [self.grid_size[1]-1 if n == -1 else n for n in check_col]

        cnt = 0

        print()
        for c_row, c_col in zip(check_row, check_col):
            print(c_row, c_col)
            if self.get_cell(c_row, c_col).state != 0: cnt += 1
        return cnt

    def update_cells_state(self):
        for row in range(self.grid_size[0]):
            for col in range(self.grid_size[1]):
                # 同じstateのセルが4個以上だったら，state=0にする．
                state_cnt = self.count_around_cells(row, col, 1)

                # 誕生条件
                #print(state_cnt)
                if self.get_cell(row, col) == 0:
                    if state_cnt == 3:
                        print("birth")
                        self.get_cell(row, col).state = 1 
                # 生存条件
                if self.get_cell(row, col) == 1:
                    if state_cnt==2 or state_cnt==3:
                        self.get_cell(row, col).state = 1
                    else:
                        self.get_cell(row, col).state = 0

    def draw(self):
        #print(self.count_living())
        for row in range(self.grid_size[0]):
            for col in range(self.grid_size[1]):
                self.get_cell(row, col).draw()