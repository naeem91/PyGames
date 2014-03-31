import pygame

from graphics.screen import GameScreen
from game_play import GamePlay
from settings import *


class Game(object):
    def __init__(self):
        pygame.init()

        self.status = GAME_STATUS.STOP
        self.screen = GameScreen()
        self.play = GamePlay(self)

    def start(self):
        self.play.start()
