from Inimigo import Inimigo
from Jogador import Jogador

import pygame
from pygame.locals import *


class CollisionHandler:
    def verificar_colisoes(self, lista_inimigos, jogador, lista_balas):
        self.colisao_jogador_inimigo(lista_inimigos, jogador)
        self.colisao_bala_inimigo(lista_inimigos, lista_balas)

    def colisao_jogador_inimigo(self, lista_inimigos, jogador):
        for inimigo in lista_inimigos:
            if jogador.rect.colliderect(inimigo.rect):
                jogador.vida -= inimigo.dano

    def colisao_bala_inimigo(self, lista_inimigos, lista_balas):
        for bala in lista_balas:
            for inimigo in lista_inimigos:
                if bala.rect.colliderect(inimigo.rect):
                    print("colidiu")
                    inimigo.vida -= bala.dano
                    if inimigo.vida <= 0:
                        print("morto")
