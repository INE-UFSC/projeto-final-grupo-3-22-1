from re import X
import pygame
from pygame.locals import *
import random as rd

pygame.init()

class Inimigo():
    def __init__(self, x, y, velocidade, dano, sprite):
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
        self.__sprite = pygame.image.load(sprite)
        self.__rect = self.__sprite.get_rect(center=(self.__x, self.__y))
        self.__dano = dano

    def atacar(self):
        pass

    def mover(self):
        direcao = rd.choice(['x', 'y'])
        sentido = rd.choice([1, -1])
        if direcao == 'x':
            self.__rect.x += sentido * self.__velocidade
        elif direcao == 'y':
            self.__rect.y += sentido * self.__velocidade    

    def desenhar(self, win):
        win.blit(self.__sprite, (self.x, self.y))
    
    @property
    def x(self) -> int:
        return self.__rect.x
    
    @property
    def y(self) -> int:
        return self.__rect.y
    
    @property
    def sprite(self):
        return self.__sprite
    
    @property
    def dano(self) -> int:
        return self.__dano
    
    @property
    def rect(self):
        return self.__rect