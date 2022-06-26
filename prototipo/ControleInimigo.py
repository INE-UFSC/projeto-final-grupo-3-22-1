from Inimigo import Inimigo
from Jogador import Jogador
import pygame
from pygame.locals import *

class ControladorInimigo():
    def __init__(self, lista_inimigos: list, jogador: Jogador):
        self.__lista_inimigos = lista_inimigos
        self.__jogador = jogador
    
    def checar_colisao(self):
        for inimigo in self.__lista_inimigos:
            if self.__jogador.rect.colliderect(inimigo.rect):
                self.__jogador.vida -= inimigo.dano