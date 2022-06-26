import pygame
from pygame.locals import *
import random as rd

pygame.init()

class Inimigo():
    def __init__(self, x, y, velocidade):
        #self.vida = vida
        #self.velocidade = velocidade
        #self.tipo_ataque = tipo_ataque
        #self.dano = dano
        #self.pontos_concedidos = pontos_concedidos
        #self.comprimento = comprimento
        #self.largura = largura
        self.__x = x
        self.__y = y
        self.__velocidade = velocidade
        self.__sprite = pygame.image.load("ChicoCunha.png")

    def atacar(self):
        pass

    def mover(self, direcao, sentido):
        if direcao == 'x':
            self.__x += sentido * self.__velocidade
        elif direcao == 'y':
            self.__y += sentido * self.__velocidade    

    def desenhar(self, win):
        self.mover(rd.choice(['x', 'y']), rd.choice([-1, 1]))
        win.blit(self.__sprite, (self.x, self.y))
    
    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
    
    @property
    def sprite(self):
        return self.__sprite