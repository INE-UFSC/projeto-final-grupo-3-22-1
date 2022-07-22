import pygame
from pygame.locals import *

from Singleton import Singleton
from Settings import Settings


class Globals(Singleton):
    settings = Settings()
    DISPLAY_SURF = pygame.display.set_mode(
        (settings.largura_tela, settings.altura_tela)
    )
