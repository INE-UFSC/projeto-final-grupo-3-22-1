from abc import ABC

import pygame
from pygame.locals import *


class Inimigo(ABC, pygame.sprite.Sprite):
    def __init__(
        self,
        vida: int,
        velocidade_projetil: int,
        tipo_de_ataque: list,
        pontuacao_concedida: int,
    ):
        self.__vida = vida
        self.__velocidade_projetil = velocidade_projetil
        self.__tipo_de_ataque = tipo_de_ataque
        self.__pontuacao_concedida = pontuacao_concedida

    @property
    def vida(self) -> int:
        return self.__vida

    @property
    def velocidade_projetil(self) -> int:
        return self.__velocidade_projetil

    @property
    def tipo_de_ataque(self) -> list:
        return self.__tipo_de_ataque

    @property
    def pontuacao_concedida(self) -> int:
        return self.__pontuacao_concedida
