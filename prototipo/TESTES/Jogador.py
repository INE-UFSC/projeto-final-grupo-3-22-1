import pygame
from pygame.locals import *
from math import sin, cos, atan2

from Arma import Arma
from Bullet import Bullet
from Melhoria import Melhoria


class Jogador(pygame.sprite.Sprite):
    def __init__(
        self, vida: int, velocidade_movimento: int, arma: Arma, surface, largura_tela
    ):
        self.__vida = vida
        self.__velocidade_movimento = velocidade_movimento
        self.__arma = arma

        # (left, top), (width, height)
        self.__sprite = pygame.image.load("ChicoCunha.png")
        self.__rect = self.__sprite.get_rect()
        self.__rect.center = (32, 32)

        self.__surface = surface
        self.__largura_tela = largura_tela

    @property
    def vida(self) -> int:
        return self.__vida
    
    @vida.setter
    def vida(self, valor):
        self.__vida = valor

    @property
    def velocidade_movimento(self) -> int:
        return self.__velocidade_movimento

    @property
    def arma(self) -> Arma:
        return self.__arma

    @property
    def sprite(self):
        return self.__sprite
    
    def set_sprite(self, sprite):
        self.__sprite = pygame.image.load(sprite)

    @property
    def rect(self):
        return self.__rect

    def mover(self):
        self.__andando = False
        pressed_keys = pygame.key.get_pressed()

        if self.rect.left > 0:
            if pressed_keys[K_LEFT] or pressed_keys[K_a]:
                self.rect.move_ip(-(self.velocidade_movimento), 0)
                self.__andando = True

        if self.rect.right < self.__largura_tela:
            if pressed_keys[K_RIGHT] or pressed_keys[K_d]:
                self.rect.move_ip(self.velocidade_movimento, 0)
                self.__andando = True

        if self.rect.bottom < self.__largura_tela:
            if pressed_keys[K_DOWN] or pressed_keys[K_s]:
                self.rect.move_ip(0, self.velocidade_movimento)
                self.__andando = True

        if self.rect.top > 0:
            if pressed_keys[K_UP] or pressed_keys[K_w]:
                self.rect.move_ip(0, -(self.velocidade_movimento))
                self.__andando = True

    def atirar(self, mouse_x, mouse_y):
        distancia_x = mouse_x - self.rect.x
        distancia_y = mouse_y - self.rect.y

        angulo = atan2(distancia_y, distancia_x)

        speed_x = self.arma.velocidade_projetil * cos(angulo)
        speed_y = self.arma.velocidade_projetil * sin(angulo)

        nova_bala = Bullet(self.rect.x, self.rect.y, speed_x, speed_y, "anzol.png")
        
        return nova_bala

    def usar_melhoria(self, melhoria: Melhoria):
        ...
