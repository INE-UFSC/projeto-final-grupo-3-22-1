import pygame
from pygame.locals import *

import random as rd
from Settings import Settings
from Inimigo import Inimigo


class InimigoBasico(Inimigo):
    def __init__(self, x: int, y: int,
                    velocidade: int, dano: int,
                    sprite: str, vida=10):                
        super().__init__(x, y, velocidade,
                        dano, sprite, vida)
                
        self.__settings = Settings()

    def atacar(self, jogador_x, jogador_y):
        pass 

    def mover(self):
        direcao = rd.choice(["x", "y"])
        sentido = rd.choice([1, -1])

        if self.rect.left <= 0:
            self.__rect.x += self.__velocidade
        elif self.rect.right >= self.settings.largura_tela:
            self.__rect.x -= self.__velocidade
        elif self.rect.bottom >= self.settings.largura_tela:
            self.__rect.y -= self.__velocidade
        elif self.rect.top <= 0:
            self.__rect.y += self.__velocidade
        else:
            if direcao == "x":
                self.__rect.x += sentido * self.__velocidade
            elif direcao == "y":
                self.__rect.y += sentido * self.__velocidade

