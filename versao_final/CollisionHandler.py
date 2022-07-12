from Jogador import Jogador

import pygame
from pygame.locals import *


class CollisionHandler(pygame.sprite.Sprite):
    # funcao que chama todas verificaoes de colisao necessarias
    def verificar_colisoes(self, grupo_inimigos, jogador, grupo_balas_jogador, grupo_balas_inimigos):
        self.colisao_jogador_inimigo(grupo_inimigos, jogador)
        self.colisao_bala_inimigo(grupo_inimigos, grupo_balas_jogador)
        self.colisao_bala_jogador(jogador, grupo_balas_inimigos)

    # colisao entre jogador e inimigos
    def colisao_jogador_inimigo(self, grupo_inimigos, jogador):
        for inimigo in grupo_inimigos:
            if jogador.rect.colliderect(inimigo.rect):
                jogador.vida -= inimigo.dano

    # colisao entre balas disparadas pelo jogador e inimigos
    def colisao_bala_inimigo(self, grupo_inimigos, grupo_balas):
        for inimigo in grupo_inimigos:
            hits = pygame.sprite.spritecollide(inimigo, grupo_balas, False)
            if hits:
                hits[0].reduzir_durabilidade()
                inimigo.receber_dano(hits[0].dano)
    
    def colisao_bala_jogador(self, jogador, grupo_balas_inimigos):
        for bala in grupo_balas_inimigos:
            hit = jogador.rect.colliderect(bala.rect)
            if hit:
                jogador.receber_dano(bala.dano)
