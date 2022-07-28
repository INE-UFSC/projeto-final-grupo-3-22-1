from Jogador import Jogador
from ControlePowerUps import ControlePowerUps

import pygame
from pygame.locals import *


class CollisionHandler(pygame.sprite.Sprite):
    def __init__(self, jogador: Jogador, controlePowerUps: ControlePowerUps):
        self.__jogador = jogador
        self.__controlePowerUps = controlePowerUps

    @property
    def jogador(self) -> Jogador:
        return self.__jogador

    @property
    def controlePowerUps(self) -> ControlePowerUps:
        return self.__controlePowerUps

    # funcao que chama todas verificaoes de colisao necessarias
    def verificar_colisoes(
        self,
        grupo_inimigos,
        grupo_balas_jogador,
        grupo_balas_inimigos,
        grupo_powerUps,
    ):
        self.colisao_jogador_inimigo(grupo_inimigos)
        self.colisao_bala_inimigo(grupo_inimigos, grupo_balas_jogador)
        self.colisao_bala_jogador(grupo_balas_inimigos)
        self.colisao_powerUp(grupo_powerUps)

    # colisao entre jogador e inimigos
    def colisao_jogador_inimigo(self, grupo_inimigos):
        for inimigo in grupo_inimigos:
            if self.jogador.rect.colliderect(inimigo.rect):
                self.jogador.receber_dano(inimigo.dano)

    # colisao entre balas disparadas pelo jogador e inimigos
    def colisao_bala_inimigo(self, grupo_inimigos, grupo_balas_jogador):
        for inimigo in grupo_inimigos:
            hits = pygame.sprite.spritecollide(inimigo, grupo_balas_jogador, False)
            if hits:
                hits[0].reduzir_durabilidade()
                inimigo.receber_dano(hits[0].dano)

                if inimigo.vida <= 0:
                    self.controlePowerUps.calcular_drop(inimigo.x, inimigo.y)

    # colisao entre balas disparadas por inimigos e jogador
    def colisao_bala_jogador(self, grupo_balas_inimigos):
        for bala in grupo_balas_inimigos:
            hit = self.jogador.rect.colliderect(bala.rect)
            if hit:
                self.jogador.receber_dano(bala.dano)

    # verifica sem jogador pegou um powerUp
    def colisao_powerUp(self, grupo_powerUps):
        for powerUp in grupo_powerUps:
            colision = self.jogador.rect.colliderect(powerUp.rect)
            if colision:
                self.jogador.usar_powerUp(powerUp)
                powerUp.kill()
