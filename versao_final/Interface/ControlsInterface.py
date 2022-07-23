import pygame
import sys
from .Interface import Interface
from .ToMenuButton import ToMenuButton
from .Settings import Settings

settings = Settings()

class ControlsInterface(Interface):

    def __init__(self):
        super().__init__()
        self.__controls_background = pygame.image.load(f'./controls_background.png')

    @property
    def controls_background(self):
        return self.__controls_background

    @controls_background.setter
    def controls_background(self, controls_background):
        self.__controls_background = controls_background

    def interfaceLoop(self):
        while True:
            return_button = ToMenuButton(650, 590, "Voltar")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return_button.nextStep(pygame.mouse.get_pos())

            settings.screen.blit(self.controls_background, (0,0))

            return_button.changeColor(pygame.mouse.get_pos())
            return_button.update()
            
            pygame.display.update()
