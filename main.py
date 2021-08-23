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
    logo = pygame.image.load('images/pythonlogo.jpg')

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        SURFACE.fill((255, 255, 255))

        SURFACE.blit(logo, (20, 50))


        pygame.display.update()

        # 一定のフレームレートにする
        FPSCLOCK.tick(3)

if __name__ == '__main__':
    main()