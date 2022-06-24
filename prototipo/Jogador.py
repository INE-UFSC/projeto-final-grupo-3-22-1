import pygame
from pygame.locals import *

from Arma import Arma
from Melhoria import Melhoria


class Player(pygame.sprite.Sprite):
    def __init__(self, vida: int, velocidade_movimento: int, arma: Arma):
        self.__vida = vida
        self.__velocidade_movimento = velocidade_movimento
        self.__arma = arma

    @property
    def vida(self) -> int:
        return self.__vida

    @property
    def velocidade_movimento(self) -> int:
        return self.__velocidade_movimento

    @property
    def arma(self) -> Arma:
        return self.__arma

    def mover(self):
        ...
    
    def atirar(self):
        ...
    
    def usar_melhoria(self, melhoria: Melhoria):
        ...