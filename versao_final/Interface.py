import pygame
import sys
from abc import ABC, abstractmethod
from Pontuacao import Pontuacao
from Settings import Settings

settings = Settings()
pygame.init()

class Interface(ABC):

    def __init__(self):
        #falta implementar
        #self.__pontuacao = pontuacao
        #self.__vidas_atuais = vidas_atuais
        #falta implementar
        settings.FPS_VALUE = 20
        FPS = pygame.time.Clock()
        self.__settings = Settings()
        
        import os, sys

    @property
    def pontuacao(self) -> Pontuacao:
        return self.__pontuacao

    @property
    def vidas_atuais(self) -> int:
        return self.__vidas_atuais

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
