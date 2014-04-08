from enum import Enum

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

GRAPHICS_PATH = 'graphics/images/'
APP_CAPTION = 'Candy Rescue'
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

GAME_STATUS = Enum('START', 'STOP', 'PAUSE')
