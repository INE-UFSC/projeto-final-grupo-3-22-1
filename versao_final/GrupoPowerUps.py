from numpy import power
import pygame
from pygame.locals import *

from Globals import Globals
from PowerUp import PowerUp
from PowerUpPermanente import PowerUpPermanente
from PowerUpTemporario import PowerUpTemporario


class GrupoPowerUps:
    def __init__(self):
        self.__grupo_todos_caidos = pygame.sprite.Group()
        self.__grupo_temporarios_caidos = pygame.sprite.Group()
        self.__grupo_permanentes_caidos = pygame.sprite.Group()

        self.__globals = Globals()

    @property
    def powerUps(self):
        return self.__powerUps

    @property
    def grupo_todos_caidos(self):
        return self.__grupo_todos_caidos

    @property
    def grupo_temporarios_caidos(self):
        return self.__grupo_temporarios_caidos

    @property
    def grupo_permanentes_caidos(self):
        return self.__grupo_permanentes_caidos

    @property
    def globals(self):
        return self.__globals

    def novo_powerUp_caido(self, powerUp: PowerUp):
        if isinstance(powerUp, PowerUpTemporario):
            self.grupo_temporarios_caidos.add(powerUp)
        elif isinstance(powerUp, PowerUpPermanente):
            self.grupo_permanentes_caidos.add(powerUp)

        self.grupo_todos_caidos.add(powerUp)

    def desenhar(self):
        for powerUp in self.grupo_todos_caidos:
            powerUp.desenhar()
