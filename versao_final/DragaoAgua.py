import pygame
from pygame.locals import *
import os
from Globals import Globals

from Settings import Settings
from Bomba import Bomba


class DragaoAgua(Bomba):
    def __init__(self, pos_x: float, pos_y: float,
                    sprite: str, dano: int, vida: int):
        super().__init__(pos_x, pos_y, sprite, dano)
        
        self._vida = vida

    def receber_dano(self, dano):
        self._vida -= dano
    
        if self._vida <= 0:
            self.kill()
            
    @property
    def vida(self):
        return self._vida
    