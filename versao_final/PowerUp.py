import pygame
from pygame.locals import *

from abc import ABC, abstractmethod

from Globals import Globals


class PowerUp(ABC, pygame.sprite.Sprite):
    def __init__(
        self,
        sprite: str,
        nome: str,
        mudancas: dict,
    ):
        super().__init__()

        self.__sprite = pygame.image.load(f"assets/{sprite}.png")
        self.__rect = self.__sprite.get_rect()
        self.__rect.center = (
            int(self.sprite.get_width() / 2),
            int(self.sprite.get_height() / 2),
        )

        self.__nome = nome
        self.__mudancas = mudancas

        self.__tempo_pego = 0
        self.__pos_x = 0
        self.__pos_y = 0

        self.__globals = Globals()

    @property
    def rect(self):
        return self.__rect

    @property
    def spawn_position_x(self):
        return self.__spawn_position_x

    @property
    def spawn_position_y(self):
        return self.__spawn_position_y

    @property
    def sprite(self):
        return self.__sprite

    @property
    def nome(self):
        return self.__nome

    @property
    def mudancas(self):
        return self.__mudancas

    @property
    def globals(self):
        return self.__globals

    @property
    def tempo_pego(self):
        return self.__tempo_pego

    @tempo_pego.setter
    def tempo_pego(self, tempo):
        self.__tempo_pego = tempo

    @property
    def pos_x(self):
        return self.__pos_x

    @property
    def pos_y(self):
        return self.__pos_y

    @pos_x.setter
    def pos_x(self, pos_x):
        self.__pos_x = pos_x

    @pos_y.setter
    def pos_y(self, pos_y):
        self.__pos_y = pos_y

    def definir_coordenadas(self, pos_x, pos_y):
        self.__pos_x = pos_x
        self.__pos_y = pos_y

    # chamado dentro do main loop pelo controle dos power ups para cada power up
    def desenhar(self):
        self.globals.DISPLAY_SURF.blit(self.sprite, (self.pos_x, self.pos_y))
