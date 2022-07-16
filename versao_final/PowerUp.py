import pygame
from pygame.locals import *

from abc import ABC, abstractmethod

from Globals import Globals


class PowerUp(ABC, pygame.sprite.Sprite):
    def __init__(
        self, spawn_position_x: int, spawn_position_y: int, sprite: str, nome: str, **mudancas
    ):
        super().__init__()

        self.__sprite = pygame.image.load(f"assets/{sprite}.png")
        self.__rect = self.__sprite.get_rect()
        self.__rect.center = (
            int(self.sprite.get_width() / 2),
            int(self.sprite.get_height() / 2),
        )

        self.__spawn_position_x = spawn_position_x
        self.__spawn_position_y = spawn_position_y
        self.__nome = nome

        self.__mudancas = mudancas
        
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

    def desenhar(self):
        self.globals.DISPLAY_SURF.blit(
            self.sprite, (self.spawn_position_x, self.spawn_position_y)
        )
