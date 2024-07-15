import pygame
import sys, os
sys.path.append(os.pardir)
import fields.cells as cl

def test_cells():
    pygame.init() # Pygameの初期化
    window_width = 1000
    window_height = 500
    screen = pygame.display.set_mode((window_width, window_height))  # 1000*500の画面

    cells = cl.Cells(screen, (100, 50), 10)
    cells.get_cell(20, 20).state = 1
    cells.get_cell(20, 21).state = 1
    cells.get_cell(21, 19).state = 1
    cells.get_cell(22, 20).state = 1

    while True:
        screen.fill((255,255,255))# 背景を白
        cells.update_cells_state()
        cells.draw()

        # 画面更新
        pygame.display.update()

        # イベント処理
        for event in pygame.event.get():  # イベントを取得
            if event.type == pygame.KEYDOWN:  
                # ESCキーならスクリプトを終了
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()               # 終了（ないとエラーで終了することになる）


if __name__ == "__main__":
   test_cells()