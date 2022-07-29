import pygame
import sys
from Interface import Interface
from ContinueButton import ContinueButton
from OptionsButton import OptionsButton
from ControlsButton import ControlsButton
from RankingButton import RankingButton
from ToMenuButton import ToMenuButton
from Settings import Settings


class PauseMenuInterface(Interface):
    def __init__(self):
        super().__init__()
        self.__background = pygame.image.load(
            f"backgrounds/main_menu_background.png"
        )
        self.__settings = Settings()
        self.__buttons_list = [ContinueButton(665, 220, "Continuar"), 
                            OptionsButton(665, 320, "Opções"),
                            ControlsButton(665, 420, "Controles"),
                            RankingButton(665, 520, "Ranking"),
                            ToMenuButton(665, 620, "Menu Principal")]

    @property
    def background(self):
        return self.__background

    @property
    def settings(self) -> Settings:
        return self.__settings

    @property
    def buttons_list(self) -> list:
        return self.__buttons_list

    def interfaceLoop(self):
        self.settings.screen.blit(self.background, (0, 0))

        while True:
            
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
