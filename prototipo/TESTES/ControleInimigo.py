from Inimigo import Inimigo
from Jogador import Jogador
import pygame
from pygame.locals import *

class ControladorInimigo():
    def checar_colisao(self, inimigo, jogador):
        if jogador.rect.colliderect(inimigo.rect):
            jogador.vida -= inimigo.dano
            
    def checar_sofreu_dano(self, inimigo, lista_balas):
        for bala in lista_balas:
            if bala.rect.colliderect(inimigo.rect):
                inimigo.vida -= bala.dano