import pygame
from pygame.locals import *
import os

from Settings import Settings


class BombaTinta(pygame.sprite.Sprite):
    def __init__(self, pos_x: float, pos_y: float,
                    sprite: str, dano: int):
        super().__init__()
        self.__pos_x = int(pos_x)
        self.__pos_y = int(pos_y)
        self.__dano = int(dano)

        self.__sprite = sprite
        self.__rect = self.__sprite.get_rect()
        self.__rect.center = (self.sprite.get_width(), self.sprite.get_height())

        self.__hitbox = (self.__pos_x, self.__pos_y, 20, 20)

        self.__settings = Settings()

    @property
    def rect(self):
        return self.__rect

    @property
    def pos_x(self):
        return self.__pos_x

    @property
    def pos_y(self):
        return self.__pos_y

    @property
    def sprite(self):
        return self.__sprite

    @pos_x.setter
    def pos_x(self, posicao):
        self.__pos_x = posicao

    @pos_y.setter
    def pos_y(self, posicao):
        self.__pos_y = posicao

    @property
    def rect(self):
        return self.__rect

    @property
    def sprite(self):
        return self.__sprite

    @property
    def dano(self):
        return self.__dano
    
    @sprite.setter
    def sprite(self, sprite):
        self.__sprite = sprite
    
    @property
    def settings(self) -> Settings:
        return self.__settings

    @property
    def hitbox(self):
        return self.__hitbox
    
    @hitbox.setter
    def hitbox(self, hitbox):
        self.__hitbox = hitbox

    def desenhar(self):
        # pygame.draw.rect(self.settings.DISPLAY_SURF, (0, 255, 0), self.__hitbox, 1)
        self.settings.DISPLAY_SURF.blit(self.__sprite, (self.rect.x, self.rect.y))
