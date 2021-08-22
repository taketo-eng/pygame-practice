import sys
import pygame
from pygame.locals import QUIT, Rect

pygame.init()
#ウィンドウの大きさ
SURFACE = pygame.display.set_mode((400, 300))
# 一定のフレームレートにする (オブジェクト生成)
FPSCLOCK = pygame.time.Clock()

def main():
    ''' main routine '''
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        SURFACE.fill((255, 255, 255))

        #赤(塗りつぶし)
        pygame.draw.rect(SURFACE, (255, 0, 0), (10, 20, 100, 50))

        #赤
        pygame.draw.rect(SURFACE, (0, 255, 0), ((100, 80), (80, 50)))

        #緑
        pygame.draw.rect(SURFACE, (0, 255, 0), ((100, 80), (80, 50)))

        #青
        rect0 = Rect(200, 60, 140, 80)
        pygame.draw.rect(SURFACE, (0, 0, 255), rect0)

        #黄
        rect1 = Rect((30, 160), (100, 50))
        pygame.draw.rect(SURFACE, (255, 255, 0), rect1)
        
        pygame.display.update()

        # 一定のフレームレートにする
        FPSCLOCK.tick(60)

if __name__ == '__main__':
    main()