import pygame
from pygame.locals import *

from Globals import Globals


class Bala(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, speed_x, speed_y, sprite, dano, durabilidade):
        super().__init__()

        self.__pos_x = pos_x
        self.__pos_y = pos_y
        self.__speed_x = speed_x
        self.__speed_y = speed_y
        self.__dano = dano
        self.__durabilidade = durabilidade

        self.__sprite = sprite
        self.__rect = self.__sprite.get_rect()
        self.__rect.center = (self.sprite.get_width() / 2, self.sprite.get_height() / 2)

        # self.__hitbox = (self.__pos_x, self.__pos_y, 20, 20)

        self.__globals = Globals()

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
    def sprite(self):
        return self.__sprite

    @property
    def dano(self):
        return self.__dano

    @property
    def speed_x(self):
        return self.__speed_x

    @property
    def speed_y(self):
        return self.__speed_y

    @property
    def durabilidade(self):
        return self.__durabilidade

    @durabilidade.setter
    def durabilidade(self, valor):
        self.__durabilidade = valor

    # @property
    # def hitbox(self):
    #     return self.__hitbox

    @sprite.setter
    def sprite(self, sprite):
        self.__sprite = sprite

    @property
    def globals(self) -> Globals:
        return self.__globals

    # @hitbox.setter
    # def hitbox(self, hitbox):
    #     self.__hitbox = hitbox

    def desenhar(self):
        # pygame.draw.rect(self.globals.DISPLAY_SURF, (0, 255, 0), self.__hitbox, 1)
        self.globals.DISPLAY_SURF.blit(self.__sprite, (self.rect.x, self.rect.y))

    def reduzir_durabilidade(self):
        self.durabilidade -= 1

        if self.durabilidade < 1:
            self.kill()
