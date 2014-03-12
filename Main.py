import pygame, sys
from pygame.locals import *

from settings import *


class GameApp():
    @staticmethod
    def main():
        pygame.init()
    
        # set up the window
        DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
        pygame.display.set_caption(APP_CAPTION)
    
        # run the game loop
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                    pygame.display.update()


if __name__ == '__main__':
    GameApp.main()
