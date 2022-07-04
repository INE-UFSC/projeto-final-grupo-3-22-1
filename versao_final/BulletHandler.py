import pygame
from pygame.locals import *

from Bala import Bala


class BulletHandler(pygame.sprite.Sprite):
    def __init__(self):
        self.__lista_balas = []

    @property
    def lista_balas(self):
        return self.__lista_balas

    def nova_bala(self, bala: Bala):
        self.__lista_balas.append(bala)

    def desenhar(self, window):
        # atualiza posicoes
        for bala in self.__lista_balas:
            bala.pos_x += bala.speed_x
            bala.pos_y += bala.speed_y

            window.blit(bala.sprite, (bala.pos_x, bala.pos_y))
