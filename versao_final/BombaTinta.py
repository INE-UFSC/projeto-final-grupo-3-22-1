import pygame
from pygame.locals import *
from Globals import Globals


class BombaTinta(pygame.sprite.Sprite):
    def __init__(self, pos_x: float, pos_y: float, sprite: str, dano: int):
        super().__init__()
        # self._pos_x = int(pos_x)
        # self._pos_y = int(pos_y)
        self._dano = int(dano)

        self._sprite = sprite
        self._rect = self._sprite.get_rect(center=(pos_x, pos_y))

        self._pos_x = pos_x - (self._sprite.get_width() / 2)
        self._pos_y = pos_y - (self._sprite.get_height() / 2)
        self._speed_x, self._speed_y = 0, 0

        self._hitbox = (
            self._pos_x,
            self._pos_y,
            self._sprite.get_width(),
            self._sprite.get_height(),
        )

        self._globals = Globals()

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
    def speed_x(self) -> int:
        return self._speed_x

    @property
    def speed_y(self) -> int:
        return self._speed_y

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
    def globals(self) -> Globals:
        return self._globals

    @property
    def hitbox(self):
        return self._hitbox

    @hitbox.setter
    def hitbox(self, hitbox):
        self._hitbox = hitbox

    def desenhar(self):
        pygame.draw.rect(self.globals.DISPLAY_SURF, (0, 255, 0), self._hitbox, 1)
        self.globals.DISPLAY_SURF.blit(self._sprite, (self._pos_x, self._pos_y))
