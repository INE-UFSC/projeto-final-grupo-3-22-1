import pygame
from pygame.locals import *

from random import randint, choice

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
            "adilson", "adilson", {"dano": 2, "cadencia": -250}, 15000  # tempo em ms
        )
        self.__powerUps_temporarios["pureza"] = PowerUpTemporario(
            "pureza", "pureza", {"velocidade_movimento": 3}, 25000
        )

        self.__powerUps_permanentes = {}
        self.__powerUps_permanentes["chinelo"] = PowerUpPermanente(
            "chinelo", "chinelo", {"velocidade_movimento": 3}
        )
        # mais uma vida é tratada como um powerUp
        self.__powerUps_permanentes["umaVida"] = PowerUpPermanente(
            "umaVida", "umaVida", {"vida": 1}
        )
        self.__powerUps_permanentes["tresVidas"] = PowerUpPermanente(
            "tresVidas", "tresVidas", {"vida": 3}
        )
        
        self.__lista_nomes_powerUps_temporarios = []
        self.__lista_nomes_powerUps_permanentes = []
        self.__lista_nomes_powerUps = []
        
        for powerUpTemporario in self.powerUps_temporarios:
            self.lista_nomes_powerUps_temporarios.append(powerUpTemporario)
            self.lista_nomes_powerUps.append(powerUpTemporario)
        for powerUpPermanente in self.powerUps_permanentes:
            self.lista_nomes_powerUps_permanentes.append(powerUpPermanente)
            self.lista_nomes_powerUps.append(powerUpPermanente)

    @property
    def jogador(self):
        return self.__jogador

    @property
    def grupo_powerUps(self):
        return self.__grupo_powerUps

    @property
    def powerUps_temporarios(self) -> dict:
        return self.__powerUps_temporarios

    @property
    def powerUps_permanentes(self) -> dict:
        return self.__powerUps_permanentes

    @property
    def lista_nomes_powerUps_temporarios(self) -> list:
        return self.__lista_nomes_powerUps_temporarios

    @property
    def lista_nomes_powerUps_permanentes(self) -> list:
        return self.__lista_nomes_powerUps_permanentes
    
    @property
    def lista_nomes_powerUps(self) -> list:
        return self.__lista_nomes_powerUps

    def calcular_drop(self, pos_x: int, pos_y: int):
        porcentagem = randint(1, 100)

        if (porcentagem >= 1) and (porcentagem <= 10):
            powerUp_escolhido = choice(self.lista_nomes_powerUps)
            
            self.spawn_powerUp(powerUp_escolhido, pos_x, pos_y)
    
    # cria um powerUp em uma posicao na tela
    def spawn_powerUp(self, nome, pos_x, pos_y):
        if nome in self.lista_nomes_powerUps_temporarios:
            powerUp = self.powerUps_temporarios[nome]
        else:
            powerUp = self.powerUps_permanentes[nome]

        self.grupo_powerUps.novo_powerUp_caido(powerUp)
        
        powerUp.definir_coordenadas(pos_x, pos_y)
        powerUp.desenhar()

    def verificar_fim_temporarios(self):
        tempo_atual = pygame.time.get_ticks()
        for powerUp in self.jogador.powerUps_temporarios:
            # verifica se ja passou o tempo que o powerUp dura
            if tempo_atual - powerUp.tempo_pego > powerUp.duracao:
                self.jogador.encerrar_powerUp(powerUp)
