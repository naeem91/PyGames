import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, APP_CAPTION, GRAPHICS_PATH


class GameScreen(object):
    def __init__(self):
        # set up the window
        self.DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
        pygame.display.set_caption(APP_CAPTION)

        background_image = pygame.image.load(GRAPHICS_PATH + "candy-rescue.jpg").convert()
        start_button = pygame.image.load(GRAPHICS_PATH + "button.png").convert()
        credits_button = pygame.image.load(GRAPHICS_PATH + "button.png").convert()

        self.DISPLAYSURF.blit(background_image, [0, 0])
        self.DISPLAYSURF.blit(start_button, [150, 350])
        self.DISPLAYSURF.blit(credits_button, [450, 350])

    def change_screen(self):
        pass
