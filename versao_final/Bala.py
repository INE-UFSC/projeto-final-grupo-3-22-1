import pygame
from pygame.locals import *


class Bala(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, speed_x, speed_y, sprite, dano):
        self.__pos_x = int(pos_x)
        self.__pos_y = int(pos_y)
        self.__speed_x = int(speed_x)
        self.__speed_y = int(speed_y)
        self.__sprite = pygame.image.load(sprite)
        self.__rect = self.__sprite.get_rect(center=(self.__pos_x, self.__pos_y))
        self.__dano = int(dano)

    @property
    def pos_x(self):
        return self.__pos_x

    @property
    def pos_y(self):
        return self.__pos_y

    @property
    def speed_x(self):
        return self.__speed_x

    @property
    def speed_y(self):
        return self.__speed_y

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

    def desenhar(self, window):
        window.blit(self.__sprite, (self.x, self.y))
