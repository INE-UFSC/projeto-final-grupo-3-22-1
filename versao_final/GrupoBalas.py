from abc import ABC

import pygame
from pygame.locals import *

from Settings import Settings
from Bala import Bala


class GrupoBalas(ABC, pygame.sprite.Sprite):
    def __init__(self):
        self.__grupo_balas = pygame.sprite.Group()
        self.__settings = Settings()

    @property
    def grupo_balas(self):
        return self.__grupo_balas

    @property
    def settings(self):
        return self.__settings

    def nova_bala(self, bala: Bala):
        self.__grupo_balas.add(bala)

    def desenhar(self):
        for bala in self.__grupo_balas:
            bala.pos_x += bala.speed_x
            bala.pos_y += bala.speed_y

            bala.rect.x = bala.pos_x
            bala.rect.y = bala.pos_y

            # caso esteja fazendo debug e vendo aonde esta o rect da bala
            # bala.hitbox = (bala.rect.x, bala.rect.y, 20, 20)

            # verifica se bala esta nas bordas do mapa
            if (
                bala.pos_x < 0
                or bala.pos_y < 0
                or bala.pos_x > self.settings.largura_tela
                or bala.pos_y > self.settings.largura_tela
            ):
                bala.kill()
            else:
                # para debug da hitbox da bala
                # pygame.draw.rect(self.settings.DISPLAY_SURF, (0, 255, 0), bala.hitbox, 1)
                self.settings.DISPLAY_SURF.blit(bala.sprite, (bala.pos_x, bala.pos_y))
