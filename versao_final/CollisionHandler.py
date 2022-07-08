from Inimigo import Inimigo
from Jogador import Jogador

import pygame
from pygame.locals import *


class CollisionHandler(pygame.sprite.Sprite):
    # funcao que chama todas verificaoes de colisao necessarias
    def verificar_colisoes(self, grupo_inimigos, jogador, grupo_balas_jogador, grupo_balas_inimigos):
        self.colisao_jogador_inimigo(grupo_inimigos, jogador)
        self.colisao_bala_inimigo(grupo_inimigos, grupo_balas_jogador)
        self.colisao_bala_jogador(grupo_balas_inimigos, jogador)

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
    
    def colisao_bala_jogador(self, grupo_balas_inimigos, jogador):
        hits = pygame.sprite.spritecollide(grupo_balas_inimigos, jogador, False)
        if hits:
            jogador.receber_dano(hits[0].dano)