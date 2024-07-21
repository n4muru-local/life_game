import pygame
from . import cells_module as cm

class Field:
    """フィールドの描画・処理
    
    Attributes
    ----------
    screen : pygame.display.set_mode
        pygameのdisplayオブジェクト
    Window_X : int
        screenの横幅
    Window_Y : int
        screenの縦幅
    cell_size: int
        cellの大きさ(縦横)
    grid_row: int
        cellの行数
    grid_col: int
        cellの列数
    cells: list(class object)
        cellクラスの[grid_row][grid_col]列の配列
    """
    def __init__(self, _screen):
        """
        Parameters
        ----------
        _screen : pygame.display.set_mode
            pygameのdisplayオブジェクト
        """
        self.screen = _screen
        self.Window_X = 1000
        self.Window_Y = 500
        self.cell_size = 10
        self.grid_row = int(self.Window_Y/self.cell_size)
        self.grid_col = int(self.Window_X/self.cell_size)
        self.cells = self.setupCells()

    def setupCells(self):
        """__init__で使用するcellクラス配列の定義

        Returns
        -------
        list[grid_row][grid_col]: cellクラスオブジェクト
            cellの行列数分のクラス配列のリストを返す
        """
        cl = []
        #ウィンドウサイズとセルサイズから、セルの総数をリストとして定義
        for row in range(0, int(self.Window_Y/self.cell_size)):
            colum = []
            for col in range(0, int(self.Window_X/self.cell_size)):
                colum.append(cm.Cell([row,col],self.cell_size,0))
            cl.append(colum)
        return cl
    
    def getCell(self, row , col):
        """特定のcellクラスを取得する

        Parameters
        ----------
        row : int
            cell配列の行数
        col : int
            cell配列の列数

        Returns
        -------
        cellクラス
            [row][col] のcellクラスオブジェクト
        """
        return self.cells[row][col]
    
    def setArray(self, _array ,pos_x, pos_y):
        """配列でfieldをセットする

        Parameters
        ----------
        _array : list
            指定する配列
        pos_x : int
            配列を設定するX座標
        pos_y : int
            配列を設定するY座標

        Raises
        ------
        Exception
            指定した座標に配列を入れるとFieldを超える場合に出力
        """
        if len(_array)+pos_y > self.grid_col:
            raise Exception("out of range col \n配列がField範囲を超えています")
        for y in range(len(_array)):
            if len(_array[y]) + pos_x > self.grid_row:
                raise Exception("out of range row \n配列がField範囲を超えています")
            for x in range(len(_array[y])):
                self.getCell(pos_x + x,pos_y + y).state = _array[y][x]
        print("successfully entered")
        
    
    def count_around_cells(self, row, col, _state):
        """特定のcellに隣接する8マスの情報をカウントする。

        Parameters
        ----------
        row : int
            cell配列の行数
        col : int
            cell配列の列数
        _state : int
            どのstateを対象にカウントするか

        Returns
        -------
        cnt: int 
            _stateで指定された要素はいくつあったかを返す。(０～８)
        """
        # cellのオフセットを定義（周囲8マス文）
        offsets = [
                (-1, -1), (-1, 0), (-1, 1), 
                ( 0, -1),          ( 0, 1), 
                ( 1, -1), ( 1, 0), ( 1, 1)]
        cnt = 0

        # ラップアラウンド処理
        for dr, dc in offsets:
            r = (row + dr) % self.grid_row
            c = (col + dc) % self.grid_col

            #指定state数をカウント
            if self.cells[r][c].state == _state:
                cnt += 1
        return cnt
    
    def update_cells_state(self):
        """すべてのセルの状態を更新する
        """
        # 次の状態を決定
        for row in range(self.grid_row):
            for col in range(self.grid_col):
                state_cnt_1 = self.count_around_cells(row, col, 1) #state==1をカウント
                state_cnt_2 = self.count_around_cells(row, col, 2) #state==2をカウント
                state_num = state_cnt_1 + state_cnt_2 #生存セルの総和

                cell = self.cells[row][col]
                if cell.state == 0:
                    # 誕生条件
                    if state_num == 3:
                        #有意stateを誕生
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


    def drawCell(self):
        """すべてのセルを描画する
        """
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
        """フィールドの格子を描画
        """
        for row in range(0, self.Window_Y,self.cell_size):
            pygame.draw.line(self.screen, (0,0,0), (0,row), (self.Window_X,row), 1)
        for col in range(0,self.Window_X,self.cell_size):
            pygame.draw.line(self.screen, (0,0,0), (col,0), (col,self.Window_Y), 1)
