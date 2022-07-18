import pygame
import sys
from Interface import Interface
from PlayButton import PlayButton
from OptionsButton import OptionsButton
from QuitButton import QuitButton
from Settings import Settings

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
        pygame.init()
        pygame.display.set_caption("O Mar não está pra Gente")

        play_button = PlayButton(665, 220, "Jogar")
        options_button = OptionsButton(665, 320, "Opções")
        button3 = PlayButton(665, 420, "Controles")
        button4 = PlayButton(665, 520, "Ranking")
        quit_button = QuitButton(665, 620, "Sair")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                play_button.nextStep(pygame.mouse.get_pos())
                options_button.nextStep(pygame.mouse.get_pos())
                button3.nextStep(pygame.mouse.get_pos())
                button4.nextStep(pygame.mouse.get_pos())
                quit_button.nextStep(pygame.mouse.get_pos())
            
        settings.screen.blit(self.main_menu_background, (0,0))

        play_button.changeColor(pygame.mouse.get_pos())
        options_button.changeColor(pygame.mouse.get_pos())
        button3.changeColor(pygame.mouse.get_pos())
        button4.changeColor(pygame.mouse.get_pos())
        quit_button.changeColor(pygame.mouse.get_pos())

        play_button.update()
        options_button.update()
        button3.update()
        button4.update()
        quit_button.update()
            
        pygame.display.update()
