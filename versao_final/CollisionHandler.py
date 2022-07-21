from numpy import power
from Jogador import Jogador

import pygame
from pygame.locals import *


class CollisionHandler(pygame.sprite.Sprite):
    # funcao que chama todas verificaoes de colisao necessarias
    def verificar_colisoes(
        self,
        grupo_inimigos,
        jogador,
        grupo_balas_jogador,
        grupo_balas_inimigos,
        grupo_powerUps,
    ):
        self.colisao_jogador_inimigo(grupo_inimigos, jogador)
        self.colisao_bala_inimigo(grupo_inimigos, grupo_balas_jogador)
        self.colisao_bala_jogador(jogador, grupo_balas_inimigos)
        self.colisao_powerUp(jogador, grupo_powerUps)

    # colisao entre jogador e inimigos
    def colisao_jogador_inimigo(self, grupo_inimigos, jogador):
        for inimigo in grupo_inimigos:
            if jogador.rect.colliderect(inimigo.rect):
                jogador.receber_dano(inimigo.dano)

    # colisao entre balas disparadas pelo jogador e inimigos
    def colisao_bala_inimigo(self, grupo_inimigos, grupo_balas_jogador):
        for inimigo in grupo_inimigos:
            hits = pygame.sprite.spritecollide(inimigo, grupo_balas_jogador, False)
            if hits:
                hits[0].reduzir_durabilidade()
                inimigo.receber_dano(hits[0].dano)

    # colisao entre balas disparadas por inimigos e jogador
    def colisao_bala_jogador(self, jogador, grupo_balas_inimigos):
        for bala in grupo_balas_inimigos:
            hit = jogador.rect.colliderect(bala.rect)
            if hit:
                jogador.receber_dano(bala.dano)

    # verifica sem jogador pegou um powerUp
    def colisao_powerUp(self, jogador, grupo_powerUps):
        for powerUp in grupo_powerUps:
            colision = jogador.rect.colliderect(powerUp.rect)
            if colision:
                jogador.usar_melhoria(powerUp)
