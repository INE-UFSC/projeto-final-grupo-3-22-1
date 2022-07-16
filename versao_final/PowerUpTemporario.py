import pygame
from pygame.locals import *

from PowerUp import PowerUp


"""
:param str sprite: nome arquivo .png do powerup
:param dict mudanca: dicionario contendo o nome da propriedade e valor do buff
"""


class PowerUpTemporario(PowerUp):
    def __init__(
        self,
        spawn_position_x: int,
        spawn_position_y: int,
        sprite: str,
        nome: str,
        duracao: int,
        **mudanca: int
    ):
        super().__init__(spawn_position_x, spawn_position_y, sprite, nome)

        self.__duracao = duracao
        self.__mudanca = mudanca

        self.__tempo_spawn = pygame.time.get_ticks()

    @property
    def duracao(self):
        return self.__duracao

    @property
    def tempo_spawn(self):
        return self.__tempo_spawn

    @property
    def mudanca(self):
        return self.__mudanca

    @property
    def valor(self):
        return self.__valor
