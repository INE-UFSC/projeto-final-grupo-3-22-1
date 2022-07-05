import pygame
from pygame.locals import *

from Bala import Bala


class BulletHandler(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.__grupo_balas = pygame.sprite.Group()

    @property
    def grupo_balas(self):
        return self.__grupo_balas

    def nova_bala(self, bala: Bala):
        self.__grupo_balas.add(bala)

    def desenhar(self, window, largura_tela):
        # atualiza posicoes
        for bala in self.__grupo_balas:
            bala.pos_x += bala.speed_x
            bala.pos_y += bala.speed_y
            
            bala.rect.x = bala.pos_x
            bala.rect.y = bala.pos_y
            
            bala.hitbox = (bala.rect.x, bala.rect.y, 20, 20)

            # verifica se bala esta nas bordas do mapa
            if (
                bala.pos_x < 0
                or bala.pos_y < 0
                or bala.pos_x > largura_tela
                or bala.pos_y > largura_tela
            ):
                bala.kill()
            else:
                pygame.draw.rect(window, (0, 255, 0), bala.hitbox, 1)
                window.blit(bala.sprite, (bala.pos_x, bala.pos_y))
