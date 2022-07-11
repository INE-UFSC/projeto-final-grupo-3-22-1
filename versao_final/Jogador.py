import pygame
from pygame.locals import *
from math import sin, cos, atan2
import os

from Arma import Arma
from Bala import Bala
from Melhoria import Melhoria

from Settings import Settings


class Jogador(pygame.sprite.Sprite):
    def __init__(
        self,
        vida: int,
        velocidade_movimento: int,
        arma: Arma = Arma(0, 20, 4, 250, "isca", 1)  
    ):
        super().__init__()
        self.__vida = vida
        self.__velocidade_movimento = velocidade_movimento
        self.__arma = arma

        self.__sprite = pygame.image.load("assets/ChicoCunha.png")
        self.__rect = self.__sprite.get_rect()
        self.__rect.center = (
            int(self.sprite.get_width() / 2),
            int(self.sprite.get_height() / 2),
        )

        self.__tempo_ultimo_tiro = 0

        self.__settings = Settings()

    @property
    def vida(self) -> int:
        return self.__vida
        self.__rect = self.__sprite.get_rect(center=(self.__x, self.__y))

    @vida.setter
    def vida(self, valor):
        self.__vida = valor

    @property
    def x(self) -> int:
        return self.__rect.x

    @property
    def y(self) -> int:
        return self.__rect.y

    @property
    def velocidade_movimento(self) -> int:
        return self.__velocidade_movimento

    @property
    def arma(self) -> Arma:
        return self.__arma

    @arma.setter
    def arma(self, arma):
        self.__arma = arma

    @property
    def sprite(self):
        return self.__sprite

    def set_sprite(self, sprite):
        self.__sprite = pygame.image.load(sprite)

    @property
    def rect(self):
        return self.__rect

    @property
    def tempo_ultimo_tiro(self) -> int:
        return self.__tempo_ultimo_tiro

    @tempo_ultimo_tiro.setter
    def tempo_ultimo_tiro(self, tempo):
        self.__tempo_ultimo_tiro = tempo

    @property
    def settings(self) -> Settings:
        return self.__settings

    def mover(self):
        # TODO: animacao de acordo com andando
        self.__andando = False
        pressed_keys = pygame.key.get_pressed()

        if self.rect.left > 0:
            if pressed_keys[K_LEFT] or pressed_keys[K_a]:
                self.rect.move_ip(-(self.velocidade_movimento), 0)
                self.__andando = True

        if self.rect.right < self.settings.largura_tela:
            if pressed_keys[K_RIGHT] or pressed_keys[K_d]:
                self.rect.move_ip(self.velocidade_movimento, 0)
                self.__andando = True

        if self.rect.bottom < self.settings.largura_tela:
            if pressed_keys[K_DOWN] or pressed_keys[K_s]:
                self.rect.move_ip(0, self.velocidade_movimento)
                self.__andando = True

        if self.rect.top > 0:
            if pressed_keys[K_UP] or pressed_keys[K_w]:
                self.rect.move_ip(0, -(self.velocidade_movimento))
                self.__andando = True

    def atirar(self, mouse_x, mouse_y):
        tempo_agora = pygame.time.get_ticks()

        if tempo_agora - self.__tempo_ultimo_tiro > self.arma.cadencia:
            self.__tempo_ultimo_tiro = tempo_agora

            distancia_x = mouse_x - self.rect.x
            distancia_y = mouse_y - self.rect.y

            angulo = atan2(distancia_y, distancia_x)

            speed_x = self.arma.velocidade_projetil * cos(angulo)
            speed_y = self.arma.velocidade_projetil * sin(angulo)

            nova_bala = Bala(
                self.rect.x,
                self.rect.y,
                speed_x,
                speed_y,
                self.arma.nome_sprite,
                self.arma.dano,
                self.arma.durabilidade_bala,
            )

            return nova_bala

    def usar_melhoria(self, melhoria: Melhoria):
        ...
