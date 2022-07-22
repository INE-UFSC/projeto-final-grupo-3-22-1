import pygame
import sys
from Interface import Interface
from ToMenuButton import ToMenuButton
from Settings import Settings

settings = Settings()

class RankingInterface(Interface):

    def __init__(self):
        super().__init__()
        self.__ranking_background = pygame.image.load(f'./ranking_background.png')

    @property
    def ranking_background(self):
        return self.__ranking_background

    @ranking_background.setter
    def ranking_background(self, ranking_background):
        self.__ranking_background = ranking_background

    def interfaceLoop(self):
        while True:
            return_button = ToMenuButton(650, 590, "Voltar")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return_button.nextStep(pygame.mouse.get_pos())

            settings.screen.blit(self.ranking_background, (0,0))

            return_button.changeColor(pygame.mouse.get_pos())
            return_button.update()
            
            pygame.display.update()
