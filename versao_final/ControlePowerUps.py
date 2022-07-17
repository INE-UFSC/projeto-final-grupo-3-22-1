import pygame
from pygame.locals import *

from PowerUpPermanente import PowerUpPermanente
from PowerUpTemporario import PowerUpTemporario
from GrupoPowerUps import GrupoPowerUps

from Jogador import Jogador


class ControlePowerUps:
    def __init__(self, jogador: Jogador):
        self.__jogador = jogador
        self.__grupo_powerUps = GrupoPowerUps()

        self.__powerUps_temporarios = {}
        self.__powerUps_temporarios["adilson"] = PowerUpTemporario(
            "adilson", "adilson", {"dano": 2, "cadencia": -250}, 15
        )
        self.__powerUps_temporarios["pureza"] = PowerUpTemporario(
            "pureza", "pureza", {"velocidade_movimento": 3}, 15
        )

    @property
    def jogador(self):
        return self.__jogador

    @property
    def grupo_powerUps(self):
        return self.__grupo_powerUps

    @property
    def powerUps_temporarios(self):
        return self.__powerUps_temporarios

    # cria um powerUp em uma posicao na tela
    def spawn_powerUp_temporario(self, nome, pos_x, pos_y):
        # seleciona do dicionario pelo nome
        powerUp = self.powerUps_temporarios[nome]
        self.grupo_powerUps.novo_powerUp_caido(powerUp)
        # desenha na tela usando a função desenhar() que todo powerUp possui
        powerUp.definir_coordenadas(pos_x, pos_y)
        powerUp.desenhar()

    def desenhar(self):
        for powerUp in self.grupo_powerUps.grupo_todos_caidos:
            powerUp.desenhar()
