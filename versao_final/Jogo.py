import pygame
from pygame.locals import *

from Mapa import Mapa


class Jogo(pygame.sprite.Sprite):
    def __init__(self):
        ...
    
    def iniciar_jogo(self):
        ...
    
    def pausar(self):
        ...
    
    def mudar_mapa(self, mapa: Mapa):
        ...
    
    def encerrar_jogo(self):
        ...