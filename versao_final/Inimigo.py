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

        self._x = x
        self._y = y
        self._velocidade = velocidade
        self._dano = dano
        self._sprite = pygame.image.load(sprite)
        self._rect = self._sprite.get_rect(center=(self._x, self._y))
        self._vida = vida
        
        self._settings = Settings()

    @abstractmethod
    def atacar(self, jogador_x, jogador_y):
        pass 

    @abstractmethod
    def mover(self):
        pass

    def desenhar(self):
        self._settings.DISPLAY_SURF.blit(self._sprite, (self._x, self._y))

    @property
    def x(self) -> int:
        return self._rect.x

    @property
    def y(self) -> int:
        return self._rect.y

    @property
    def velocidade(self) -> int:
        return self._velocidade

    @property
    def sprite(self) -> str:
        return self._sprite

    @property
    def dano(self) -> int:
        return self._dano

    @property
    def rect(self) -> tuple:
        return self._rect

    @property
    def vida(self) -> int:
        return self._vida

    @vida.setter
    def vida(self, vida):
        self._vida = vida
        
    @property
    def settings(self) -> Settings:
        return self._settings

    def receber_dano(self, dano):
        self._vida -= dano

        if self._vida <= 0:
            self.kill()
