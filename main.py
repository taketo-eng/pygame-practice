import sys
import pygame
from pygame.locals import QUIT

pygame.init()
#ウィンドウの大きさ
SURFACE = pygame.display.set_mode((400, 300))

#画面の色 RGB
s_colour = (0,0,0)

# 一定のフレームレートにする (オブジェクト生成)
FPSCLOCK = pygame.time.Clock()

def main():
    ''' main routine '''
    # font
    sysfont = pygame.font.SysFont(None, 36)
    counter = 0

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        counter += 1
        SURFACE.fill(s_colour)
        count_image = sysfont.render(
            "count is {}".format(counter), True, (255, 255, 255)
        )
        SURFACE.blit(count_image, (50, 50))
        pygame.display.update()

        # 一定のフレームレートにする
        FPSCLOCK.tick(60)

if __name__ == '__main__':
    main()