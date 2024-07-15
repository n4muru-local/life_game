import pygame


class Cell:
    def __init__(self, _screen, _size, _pos, _state):
        self.screen = _screen
        self.size = _size
        self.pos = _pos
        self.state = _state

    def draw(self):
        if self.state == 1:
            pygame.draw.rect(self.screen, (255,0,0), (pos[0], pos[1], size, size))
        elif self.state == 2:
            pygame.draw.rect(self.screen, (0,255,0), (pos[0], pos[1], size, size))
        elif self.state == 0:
            pygame.draw.rect(self.screen, (255,255,255), (pos[0], pos[1], size, size))

class Cells:
    def __init__(self, _screen, _grid_size, _cell_size):
        self.list = self.create_cells
        self.screen = _screen
        self.grid_size = _grid_size # 縦横それぞれ何個cellが並ぶか
        self.cell_size = _cell_size
    
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

    def get_cell(row, col):
        return self.list[row, col]
    
    def set_cell(row, col, new_cell):
        self.list[row, col] = new_cell
    
    def count_around_cells(row, col, state):
        # 周囲のあるstateであるセルをカウントする
        # チェックテーブルの作成
        check_row = [-1, -1, -1,  0,  0,  1,  1,  1]
        check_col = [-1,  0,  1, -1,  1, -1,  0,  1]
        check_row = [n + row for n in check_row]
        check_col = [n + col for n in check_col]
        # 端のセルは反対側を参照する
        check_row =  [0 if n==grid_size[0] +1 else n for n in check_row]
        check_col =  [0 if n==grid_size[1] +1 else n for n in check_col]
        check_row =  [grid_size[0] if n == -1 else n for n in check_row]
        check_col =  [grid_size[1] if n == -1 else n for n in check_col]

        state_cnt = 0
        for c_row, c_col in zip(check_row, check_col):
            if self.get_cell(c_row, c_col).state == state: state_cnt += 1 
        return state_cnt

    def update_cells_state(self):
        for row, col in zip(range(self.grid_size[0]), range(self.grid_size[1])):
            # 同じstateのセルが4個以上だったら，state=0にする．
            state_cnt = count_around_cells(row, col, self.get_cell(row, col).state)
            if state_cnt >= 4:
                self.get_cell(row, col).state = 0

    def draw(self):
        for row, col in zip(range(self.grid_size[0]), range(self.grid_size[1])):
            self.get_cell(row, col).draw()