import pygame
from pygame.locals import *

import random as rd
from Settings import Settings
from Inimigo import Inimigo


class InimigoRastreador(Inimigo):
    def __init__(self, x: int, y:int,
                    velocidade: int, dano:int,
                    sprite: str, vida=10):
        super().__init__(x, y, velocidade, dano,
                            sprite, vida)
        
        self.__settings = Settings()

    def atacar(self):
        pass

    def mover(self, x, y):
        self.__rect.x += x * self.__velocidade
        self.__rect.y += y * self.__velocidade
    