import pygame
import sys
from Interface import Interface
from ContinueButton import ContinueButton
from OptionsButton import OptionsButton
from ControlsButton import ControlsButton
from RankingButton import RankingButton
from ToMenuButton import ToMenuButton


class PauseMenuInterface(Interface):
    def __init__(self):
        super().__init__()
        self.__background = pygame.image.load(
            f"backgrounds/pause_menu_background.png"
        )
        self.__buttons_list = [ContinueButton(653, 280, "Continuar"),
                            ToMenuButton(653, 420, "Menu Principal")]

    @property
    def background(self):
        return self.__background

    @property
    def buttons_list(self) -> list:
        return self.__buttons_list

    def interfaceLoop(self):
        self.settings.screen.blit(self.background, (0, 0))
        self.settings.paused = True

        while self.settings.paused == True:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                for button in self.buttons_list:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        button.nextStep(pygame.mouse.get_pos())
                    button.changeColor(pygame.mouse.get_pos())

                    button.update()

            pygame.display.update()
