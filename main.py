import pygame
import sys

import fields # type: ignore
import players # type: ignore

window_X = 1000
window_Y = 500

def main():
    pygame.init()# Pygameの初期化
    screen = pygame.display.set_mode((window_X, window_Y))  # 1000*500の画面

    field = fields.field_module.Field(screen)
    n4muru = players.player_module.player(1,(255,200,200),(150,150),200)

    
    
    glider = [
        [1, 1, 0],
        [1, 0, 1],
        [1, 0, 0]
    ]
    field.setArray(glider,20,20)



    while True:
        screen.fill((255,255,255))# 背景を白
        field.drawCell()
        field.drawPlayers()
        field.drawLine()



        field.update_cells_state()
        
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
    main()