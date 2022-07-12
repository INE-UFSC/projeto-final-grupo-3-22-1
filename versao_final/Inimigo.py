import pygame
from pygame.locals import *
from abc import (
  ABC,
  abstractmethod
)

import random as rd
from Settings import Settings


class Inimigo(pygame.sprite.Sprite, ABC):
    def __init__(self, x, y, velocidade, dano, sprite, vida=10):             
        pygame.sprite.Sprite.__init__(self)
        ABC.__init__(self)

        self.x = x
        self.y = y
        self.velocidade = velocidade
        self.dano = dano
        self.sprite = pygame.image.load(sprite)
        self.rect = self.sprite.get_rect(center=(self.x, self.y))
        self.vida = vida
        
        self.settings = Settings()

    @abstractmethod
    def atacar(self, jogador_x, jogador_y):
        pass 

    @abstractmethod
    def mover(self):
        pass

    def desenhar(self):
        self.settings.DISPLAY_SURF.blit(self.__sprite, (self.x, self.y))

    @property
    def x(self) -> int:
        return self.rect.x

    @property
    def y(self) -> int:
        return self.rect.y

    @property
    def velocidade(self) -> int:
        return self.velocidade

    @property
    def sprite(self):
        return self.sprite

    @property
    def dano(self) -> int:
        return self.dano

    @property
    def rect(self):
        return self.rect

    @property
    def vida(self):
        return self.vida

    @vida.setter
    def vida(self, vida):
        self.vida = vida
        
    @property
    def settings(self) -> Settings:
        return self.settings

    def receber_dano(self, dano):
        self.vida -= dano

        if self.vida <= 0:
            self.kill()
