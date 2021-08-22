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
        pygame.draw.circle(SURFACE, (255, 0, 0), (50, 50), 20)

        #赤
        pygame.draw.circle(SURFACE, (255, 0, 0), (150, 50), 20, 10)

        #緑 radius = 10
        pygame.draw.circle(SURFACE, (0, 255, 0), (50, 150), 10)

        #緑 radius = 20
        pygame.draw.circle(SURFACE, (0, 255, 0), (150, 150), 20)

        # 緑 radius = 30
        pygame.draw.circle(SURFACE, (0, 255, 0), (250, 150), 30)

        pygame.display.update()

        # 一定のフレームレートにする
        FPSCLOCK.tick(60)

if __name__ == '__main__':
    main()