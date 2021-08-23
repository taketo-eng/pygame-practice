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
    theta = 0

    while True:
        for event in pygame.event.get(QUIT):
            pygame.quit()
            sys.exit()

        # theta += 1 数が膨大になるのはいやだから 0-360の範囲に収めた
        theta = (theta + 1) % 360

        SURFACE.fill((255, 255, 255))

        new_logo = pygame.transform.rotate(logo, theta)

        rect = new_logo.get_rect()
        # 中心を設定
        rect.center = (200, 150)
        SURFACE.blit(new_logo, rect)

        pygame.display.update()

        # 一定のフレームレートにする
        FPSCLOCK.tick(30)

if __name__ == '__main__':
    main()