from Inimigo import Inimigo
from Jogador import Jogador
import pygame
from pygame.locals import *

class ControladorInimigo():
    def checar_colisao(self, inimigo, jogador):
        if jogador.rect.colliderect(inimigo.rect):
            jogador.vida -= inimigo.dano