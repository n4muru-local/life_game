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

class Cells:
    def __init__(self, _screen, _grid_size):
        self.list = self.create_cells
        self.screen = _screen
        self.grid_size = _grid_size
    
    def create_cells(self):
        cells = []
        for x in range(self.grid_size[0]):
            row = []
            for y in range(self.grid_size[1]):
                pos = (x * self.cell_size, y * self.cell_size)
                cell = Cell(self.screen, self.cell_size, pos, 0)
                row.append(cell)
            cells.append(row)
        return cells

    def get_cell(x, y):
        return self.list[x, y]
    
    def set_cell(x, y, new_cell):
        self.list[x, y] = new_cell
    
    def draw(self):
        for cell in self.list:
            cell.draw()