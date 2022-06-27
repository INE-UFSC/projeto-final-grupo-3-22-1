import pygame
from pygame.locals import *

from Bullet import Bullet


class BulletHandler:
    def __init__(self):
        self.__lista_bullets = []
    
    @property
    def lista_bullets(self):
        return self.__lista_bullets
    
    def nova_bala(self, bala: Bullet):
        self.__lista_bullets.append(bala)
        
    def desenhar(self, window):
        # atualiza posicoes
        for bullet in self.__lista_bullets:
            bullet.pos_x += bullet.speed_x
            bullet.pos_y += bullet.speed_y
            
            window.blit(bullet.sprite, (bullet.pos_x, bullet.pos_y))