from Inimigo import Inimigo
from Jogador import Jogador

import pygame
from pygame.locals import *


class CollisionHandler(pygame.sprite.Sprite):
    # funcao que chama todas verificaoes de colisao necessarias
    def verificar_colisoes(self, grupo_inimigos, jogador, grupo_balas):
        self.colisao_jogador_inimigo(grupo_inimigos, jogador)

        self.colisao_bala_inimigo(grupo_inimigos, grupo_balas)

    # colisao entre jogador e inimigos
    def colisao_jogador_inimigo(self, grupo_inimigos, jogador):
        for inimigo in grupo_inimigos:
            if jogador.rect.colliderect(inimigo.rect):
                jogador.vida -= inimigo.dano

    # colisao entre balas disparadas pelo jogador e inimigos
    def colisao_bala_inimigo(self, grupo_inimigos, grupo_balas):
        for inimigo in grupo_inimigos:
            hits = pygame.sprite.spritecollide(inimigo, grupo_balas, True)
            if hits:
                inimigo.receber_dano(hits[0].dano)
