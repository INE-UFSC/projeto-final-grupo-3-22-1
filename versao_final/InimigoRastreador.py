import pygame
from pygame.locals import *

import random as rd
from Settings import Settings


class InimigoRastreador(pygame.sprite.Sprite):
    def __init__(self, x, y, velocidade, dano, sprite, vida=10):
        # self.__tipo_ataque = tipo_ataque
        # self.__pontos_concedidos = pontos_concedidos
        # self.__comprimento = comprimento
        super().__init__()
        self.__x = x
        self.__y = y
        self.__velocidade = velocidade
        self.__dano = dano
        self.__sprite = pygame.image.load(sprite)
        self.__rect = self.__sprite.get_rect(center=(self.__x, self.__y))
        self.__vida = vida
        
        self.__settings = Settings()

    def atacar(self):
        pass

    def mover(self, x, y):
        self.__rect.x += x*self.__velocidade
        self.__rect.y += y*self.__velocidade
    
    def desenhar(self):
        self.settings.DISPLAY_SURF.blit(self.__sprite, (self.x, self.y))

    @property
    def x(self) -> int:
        return self.__rect.x

    @property
    def y(self) -> int:
        return self.__rect.y
    
    @property
    def velocidade(self) -> int:
        return self.__velocidade

    @property
    def sprite(self):
        return self.__sprite

    @property
    def dano(self) -> int:
        return self.__dano

    @property
    def rect(self):
        return self.__rect

    @property
    def vida(self):
        return self.__vida

    @vida.setter
    def vida(self, vida):
        self.__vida = vida
        
    @property
    def settings(self) -> Settings:
        return self.__settings

    def receber_dano(self, dano):
        self.vida -= dano

        if self.vida <= 0:
            self.kill()