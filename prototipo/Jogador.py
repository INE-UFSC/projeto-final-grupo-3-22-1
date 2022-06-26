import pygame
from pygame.locals import *

from Arma import Arma
from Melhoria import Melhoria


class Jogador(pygame.sprite.Sprite):
    def __init__(
        self, vida: int, velocidade_movimento: int, arma: Arma, surface, largura_tela
    ):
        self.__vida = vida
        self.__velocidade_movimento = velocidade_movimento
        self.__arma = arma

        # (left, top), (width, height)
        self.__sprite = pygame.image.load("ChicoCunha.png")
        self.__rect = self.__sprite.get_rect()
        self.__rect.center = (32, 32)

        self.__surface = surface
        self.__largura_tela = largura_tela

    @property
    def vida(self) -> int:
        return self.__vida

    @vida.setter
    def vida(self, vida):
        self.__vida = vida
    
    @property
    def velocidade_movimento(self) -> int:
        return self.__velocidade_movimento

    @property
    def arma(self) -> Arma:
        return self.__arma

    @property
    def sprite(self):
        return self.__sprite

    @property
    def rect(self):
        return self.__rect

    def mover(self):
        pressed_keys = pygame.key.get_pressed()

        # para nao passar do limite da tela
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-(self.velocidade_movimento), 0)
        if self.rect.right < self.__largura_tela:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(self.velocidade_movimento, 0)
        # mudar para ser altura da tela
        if self.rect.bottom < self.__largura_tela:
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0, self.velocidade_movimento)
        if self.rect.top > 0:
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -(self.velocidade_movimento))

    def atirar(self):
        ...

    def usar_melhoria(self, melhoria: Melhoria):
        ...
