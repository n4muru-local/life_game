import pygame
import sys

import fields # type: ignore
import globals # type: ignore
from globals import global_value as g # type: ignore


def main():
    pygame.init()# Pygameの初期化
    globals.set_global.set_value()
    screen = pygame.display.set_mode((g.window_X, g.window_Y))  # 1000*500の画面

    field = fields.field_module.Field(screen)
    

    instant_state = [[0] * g.window_X for i in range(g.window_Y)]
    instant_state[100][100] = 1
    instant_state[100][101] = 1
    instant_state[101][99] = 1
    instant_state[101][100] = 1
    instant_state[102][100] = 1
    field.setState(instant_state)
    field.printState()
    #field.updateField()


    while True:
        screen.fill((255,255,255))# 背景を白
        field.drawCell()
        field.drawLine()

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