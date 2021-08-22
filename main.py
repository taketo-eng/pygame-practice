import sys
import pygame
from pygame.locals import QUIT
import random

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

        pointlist = []

        for _ in range(10):
            xpos = random.randint(0, 400)
            ypos = random.randint(0, 300)
            pointlist.append((xpos, ypos))

        pygame.draw.lines(SURFACE, (255, 255, 255), True, pointlist, 5)

        pygame.display.update()

        # 一定のフレームレートにする
        FPSCLOCK.tick(3)

if __name__ == '__main__':
    main()