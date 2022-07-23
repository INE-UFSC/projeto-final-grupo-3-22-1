import pygame
from Interface import Interface
from PlayButton import PlayButton
from OptionsButton import OptionsButton
from ControlsButton import ControlsButton
from RankingButton import RankingButton
from QuitButton import QuitButton
from Settings import Settings

settings = Settings()

class MainMenuInterface(Interface):

    def __init__(self):
        super().__init__()
        self.__background = pygame.image.load(f'./main_menu_background.png')
        self.__buttons_list = [PlayButton(665, 220, "Jogar"), 
                            OptionsButton(665, 320, "Opções"),
                            ControlsButton(665, 420, "Controles"),
                            RankingButton(665, 520, "Ranking"),
                            QuitButton(665, 620, "Sair")]

    @property
    def background(self):
        return self.__background

    @property
    def buttons_list(self) -> list:
        return self.__buttons_list
