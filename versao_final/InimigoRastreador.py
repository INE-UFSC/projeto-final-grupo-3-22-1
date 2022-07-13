import pygame
from pygame.locals import *
from math import hypot

import random as rd
from Settings import Settings
from Inimigo import Inimigo


class InimigoRastreador(Inimigo):
    def __init__(self, x: int, y:int,
                    velocidade: int, dano:int,
                    sprite: str, vida=10):
        super().__init__(x, y, velocidade, dano,
                            sprite, vida)
        
        self._settings = Settings()

    def atacar(self):
        pass

    def mover(self, x, y):
        self._rect.x += x * self._velocidade
        self._rect.y += y * self._velocidade
    
    def achar_caminho(self, inimigo, jogador_x, jogador_y) -> int:
        # Achando os catetos e a hipotenusa
        distx, disty = jogador_x - inimigo.x, jogador_y - inimigo.y 
        hyp = hypot(distx, disty)

        # Normalizando as distâncias e retornando        
        distx, disty = distx / hyp, disty / hyp
        return distx, disty

    