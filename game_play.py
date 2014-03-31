import sys

import pygame
from pygame.locals import *

from settings import *


class GamePlay(object):
    def __init__(self, game):
        self.game = game

    def start(self):
        if self.game.game_status == GAME_STATUS.STOP:
            # run the game loop
            while True:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()

            pygame.display.update()
