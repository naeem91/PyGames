import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, APP_CAPTION


class GameScreen(object):
    def __init__(self):
        # set up the window
        self.DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
        pygame.display.set_caption(APP_CAPTION)
