import sys
import pygame
from pygame.locals import QUIT

pygame.init()
#ウィンドウの大きさ
SURFACE = pygame.display.set_mode((400, 300))
#ウィンドウのキャプション
pygame.display.set_caption('Just Window')
#画面の色 RGB
s_colour = (255,255,255)

def main():
    ''' main routine '''
    while True:
        SURFACE.fill(s_colour)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

if __name__ == '__main__':
    main()