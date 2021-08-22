import sys
import pygame
from pygame.locals import QUIT

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

        SURFACE.fill((0, 0, 0))

        #白 vertical
        for xpos in range(0, 400, 25):
            pygame.draw.line(SURFACE, 0xFFFFFF, (xpos, 0), (xpos, 300))

        #白 horizontal
        for ypos in range(0, 300, 25):
            pygame.draw.line(SURFACE, 0xFFFFFF, (0, ypos), (400, ypos))

        pygame.display.update()

        # 一定のフレームレートにする
        FPSCLOCK.tick(60)

if __name__ == '__main__':
    main()