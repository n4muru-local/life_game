
class Cell:
    """cell単体の情報を持つ構造体

    Attributes
    ----------
    grid_row: int
        縦(行)の番号(０～)
    grid_col: int
        横(列)の番号(０～)
    cell_size:int
        cellの大きさ(正方形)
    state: int
        cellの状態(0~2)
    next_state: int
        cellの次の状態(遷移後の状態)
    """
    def __init__(self,_grid_num, _size, _state):
        """
        Parameters
        ----------
        _grid_num: list
            cellの配列番号
        _size: int
            cell一つごとのサイズ
        _state: int
            cellの状態
        """
        self.grid_row = _grid_num[1] # [0]:縦 [1]:横 field Size
        self.grid_col = _grid_num[0]
        self.cell_size = _size
        self.state =  _state
        self.next_state = self.state

    def pos(self):
        """cellの位置座標を返す

        Returns
        -------
        [x座標,y座標]: [int, int]
            cell左上部の座標をlist型で返す
        """
        return [self.grid_row*self.cell_size, self.grid_col*self.cell_size]
  
    def set(self, _state):
        """cellのstateを書き換える

        Parameters
        ----------
        _state : int
            書き換えるための値
        
        returns
        ----------
        null

        """
        self.state = _state
    
    def updateState(self):
        """cellのstateを更新する
        """
        self.state = self.next_state

