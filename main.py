import pygame
import sys

import Field

def main():
    pygame.init()                                 # Pygameの初期化
    screen = pygame.display.set_mode((1000, 500))  # 1000*500の画面

    field = Field.Field(screen)
    field.setState([[1] * 1000 for i in range(500)])

    while True:
        screen.fill((255,255,255))# 背景を白
        field.drawLine()
        field.drawCell()

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