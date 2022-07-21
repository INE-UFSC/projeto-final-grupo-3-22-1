from Jogador import Jogador
import pygame
from pygame.locals import *


class ControleJogador:
    def __init__(self, jogador: Jogador):
        self.__jogador = jogador

    def jogador_morto(self):
        vida = self.__jogador.vida
        if vida <= 0:
            return True
