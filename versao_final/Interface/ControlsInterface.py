import pygame
from .Interface import Interface
from .ToMenuButton import ToMenuButton
from .Settings import Settings

settings = Settings()

class ControlsInterface(Interface):

    def __init__(self):
        super().__init__()
        self.__background = pygame.image.load('Interface/controls_background.png')
        self.__buttons_list = [ToMenuButton(650, 590, "Voltar")]

    @property
    def background(self):
        return self.__background

    @property
    def buttons_list(self):
        return self.__buttons_list
