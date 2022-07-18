import pygame
import sys
from Interface import Interface
from PlayButton import PlayButton
from Settings import Settings

settings = Settings()

class OptionsInterface(Interface):

    def __init__(self):
        super().__init__()
        self.__options_background = pygame.image.load(f'./options_background.png')

    @property
    def options_background(self):
        return self.__options_background

    @options_background.setter
    def options_background(self, options_background):
        self.__options_background = options_background

    def interfaceLoop(self):
        pygame.init()
        pygame.display.set_caption("O Mar não está pra Gente")

        return_button = PlayButton(665, 220, "Voltar")
        confirm_button = PlayButton(665, 620, "Confirmar")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                return_button.nextStep(pygame.mouse.get_pos())
                confirm_button.nextStep(pygame.mouse.get_pos())
            
        settings.screen.blit(self.options_background, (0,0))

        return_button.changeColor(pygame.mouse.get_pos())
        confirm_button.changeColor(pygame.mouse.get_pos())

        return_button.update()
        confirm_button.update()
            
        pygame.display.update()
