import pygame
from pygame.locals import *
import os

from Settings import Settings


class BombaTinta(pygame.sprite.Sprite):
    def __init__(self, pos_x: float, pos_y: float,
                    sprite: str, dano: int):
        super().__init__()
        #self._pos_x = int(pos_x)
        #self._pos_y = int(pos_y)
        self._dano = int(dano)

        self._sprite = sprite
        self._rect = self._sprite.get_rect()

        self._pos_x = pos_x - (self._sprite.get_width() / 2)
        self._pos_y = pos_y - (self._sprite.get_height() / 2)
        
        self._hitbox = (self._pos_x, self._pos_y, self._sprite.get_width(), self._sprite.get_height())

        self._settings = Settings()

    @property
    def rect(self):
        return self._rect

    @property
    def pos_x(self):
        return self._pos_x

    @property
    def pos_y(self):
        return self._pos_y

    @property
    def sprite(self):
        return self._sprite

    @pos_x.setter
    def pos_x(self, posicao):
        self._pos_x = posicao

    @pos_y.setter
    def pos_y(self, posicao):
        self._pos_y = posicao

    @property
    def rect(self):
        return self._rect

    @property
    def sprite(self):
        return self._sprite

    @property
    def dano(self):
        return self._dano
    
    @sprite.setter
    def sprite(self, sprite):
        self._sprite = sprite
    
    @property
    def settings(self) -> Settings:
        return self._settings

    @property
    def hitbox(self):
        return self._hitbox
    
    @hitbox.setter
    def hitbox(self, hitbox):
        self._hitbox = hitbox

    def desenhar(self):
        # pygame.draw.rect(self.settings.DISPLAY_SURF, (0, 255, 0), self.__hitbox, 1)
        self.settings.DISPLAY_SURF.blit(self._sprite, (self._rect.x, self._rect.y))
