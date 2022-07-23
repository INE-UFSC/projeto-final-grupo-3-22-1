import pygame
from Interface import Interface
from ToMenuButton import ToMenuButton
from Settings import Settings

settings = Settings()


class OptionsInterface(Interface):
    def __init__(self):
        super().__init__()
        self.__background = pygame.image.load(f'./options_background.png')
        self.__buttons_list = [ToMenuButton(510, 590, "Voltar"),
                            ToMenuButton(790, 590, "Confirmar")]

    @property
    def background(self):
        return self.__background

    @property
    def buttons_list(self):
        return self.__buttons_list
