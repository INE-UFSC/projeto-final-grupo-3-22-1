import pygame
from pygame.locals import *
from math import hypot

import random as rd
from Globals import Globals
from Settings import Settings
from Inimigo import Inimigo


class InimigoRastreador(Inimigo):
    def __init__(self, x: int, y:int,
                    velocidade: int, dano:int,
                    sprite: str, vida=10):
        super().__init__(x, y, velocidade, dano,
                            sprite, vida)
        
        self._settings = Settings()
        self._globals = Globals()

    def atacar(self):
        pass

    def mover(self, x, y):
        self._rect.x += x * self._velocidade
        self._rect.y += y * self._velocidade
    
    def desenhar(self):
        self.globals.DISPLAY_SURF.blit(self.__sprite, (self.x, self.y))

    def achar_caminho(self, jogador_x, jogador_y) -> int:
        # Achando os catetos e a hipotenusa
        distx, disty = jogador_x - self._rect.x, jogador_y - self._rect.y 
        hyp = hypot(distx, disty)

        # Normalizando as distâncias e retornando        
        distx, disty = distx / hyp, disty / hyp
        return distx, disty

    