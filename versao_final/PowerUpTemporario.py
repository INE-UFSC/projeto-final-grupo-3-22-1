import pygame
from pygame.locals import *

from PowerUp import PowerUp


"""
:param str sprite: nome arquivo .png do powerup
:param dict mudanca: dicionario contendo o nome da propriedade e valor do buff
"""


class PowerUpTemporario(PowerUp):
    def __init__(self, sprite: str, nome: str, mudancas: dict, duracao: int):
        super().__init__(sprite, nome, mudancas)

        self.__duracao = duracao
        self.__mudancas = mudancas

        self.__tempo_spawn = pygame.time.get_ticks()

    @property
    def duracao(self):
        return self.__duracao

    @property
    def tempo_spawn(self):
        return self.__tempo_spawn

    def encerrar(self):  # percorrer mudancas e passar elas de volta com valor negativo?
        ...
