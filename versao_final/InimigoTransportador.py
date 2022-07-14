import pygame
from pygame.locals import *

from math import hypot, degrees, atan2

from Settings import Settings
from Inimigo import Inimigo


class InimigoTeletransportador(Inimigo):
    """
    Classe que define inimigos atiradores, que evitam o jogador e atiram
    projéteis de uma distância segura
    """
    
    def __init__(self, x: int, y: int, velocidade: int,
                    dano: int, sprite: str, vida=10):
        super().__init__(x, y, velocidade,
                        dano, sprite, vida)
        
        self._pulo_completo = False
        self._sprite_original = self._sprite
        self._cooldown_ataque = 300
        self._tempo_inicio_ataque = pygame.time.get_ticks()

        self._settings = Settings()

    def atacar(self, jogador_x, jogador_y):
        tempo_agora = pygame.time.get_ticks()
        
        if tempo_agora - self._tempo_inicio_ataque >= 300:

    def mover(self, x, y):
        pass

    def desaparecer(self):
        if self._pulo_completo:
            self._sprite = ""
