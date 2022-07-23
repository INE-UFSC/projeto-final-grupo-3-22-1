import pygame
from abc import ABC, abstractmethod
from .Pontuacao import Pontuacao
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
        settings.largura_tela = 1280
        settings.altura_tela = 720
        settings.main_font = pygame.font.Font(f"./alterebro-pixel-font.ttf", 50)
        settings.screen = pygame.display.set_mode((settings.largura_tela, 
				settings.altura_tela))

    @property
    def pontuacao(self) -> Pontuacao:
        return self.__pontuacao

    @property
    def vidas_atuais(self) -> int:
        return self.__vidas_atuais

    @property
    def button_surface(self):
        return self.__button_surface
    
    @button_surface.setter
    def button_surface(self, button_surface):
        self.__button_surface = button_surface

    @abstractmethod
    def interfaceLoop(self):
        pass
