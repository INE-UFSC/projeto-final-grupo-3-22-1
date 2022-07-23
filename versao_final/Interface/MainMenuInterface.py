import pygame
import sys
from Interface import Interface
from .PlayButton import PlayButton
from .OptionsButton import OptionsButton
from .ControlsButton import ControlsButton
from .RankingButton import RankingButton
from .QuitButton import QuitButton
from .Settings import Settings

settings = Settings()

class MainMenuInterface(Interface):

    def __init__(self):
        super().__init__()
        self.__main_menu_background = pygame.image.load(f'./main_menu_background.png')

    @property
    def main_menu_background(self):
        return self.__main_menu_background

    @main_menu_background.setter
    def main_menu_background(self, main_menu_background):
        self.__main_menu_background = main_menu_background

    def interfaceLoop(self):
        while True:            
            play_button = PlayButton(665, 220, "Jogar")
            options_button = OptionsButton(665, 320, "Opções")
            controls_button = ControlsButton(665, 420, "Controles")
            ranking_button = RankingButton(665, 520, "Ranking")
            quit_button = QuitButton(665, 620, "Sair")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    play_button.nextStep(pygame.mouse.get_pos())
                    options_button.nextStep(pygame.mouse.get_pos())
                    controls_button.nextStep(pygame.mouse.get_pos())
                    ranking_button.nextStep(pygame.mouse.get_pos())
                    quit_button.nextStep(pygame.mouse.get_pos())
            
            settings.screen.blit(self.main_menu_background, (0,0))

            play_button.changeColor(pygame.mouse.get_pos())
            options_button.changeColor(pygame.mouse.get_pos())
            controls_button.changeColor(pygame.mouse.get_pos())
            ranking_button.changeColor(pygame.mouse.get_pos())
            quit_button.changeColor(pygame.mouse.get_pos())

            play_button.update()
            options_button.update()
            controls_button.update()
            ranking_button.update()
            quit_button.update()
            
            pygame.display.update()
