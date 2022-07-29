import pygame
import sys
from abc import ABC, abstractmethod
from Settings import Settings

pygame.init()

class Interface(ABC):

    def __init__(self):
        self.__settings = Settings()

    @property
    def settings(self) -> Settings:
        return self.__settings

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
