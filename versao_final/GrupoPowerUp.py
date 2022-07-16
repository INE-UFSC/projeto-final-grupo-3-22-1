from numpy import power
import pygame
from pygame.locals import *

from Globals import Globals
from PowerUp import PowerUp
from PowerUpTemporario import PowerUpTemporario


class GrupoPowerUp:
    def __init__(self):
        # self.__jogador = jogador

        # self.__powerUps = {}
        # self.__powerUps["adilson"] = PowerUpTemporario(
        #     100, 100, "adilson", "adilson", 30, dano=10, cadencia=15
        # )

        self.__grupo_todos_caidos = pygame.sprite.Group()
        self.__grupo_temporarios_caidos = pygame.sprite.Group()

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
    def globals(self):
        return self.__globals

    def novo_powerUp(self, powerUp: PowerUp):
        if isinstance(powerUp, PowerUpTemporario):
            self.grupo_temporarios_caidos.add(powerUp)
            
        self.grupo_todos_caidos.add(powerUp)

    def desenhar(self):
        for powerUp in self.grupo_todos_caidos:
            powerUp.desenhar()
