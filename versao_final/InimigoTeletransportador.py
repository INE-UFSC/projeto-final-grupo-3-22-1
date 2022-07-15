import pygame
from pygame.locals import *

from math import hypot, degrees, atan2

from Settings import Settings
from Inimigo import Inimigo


class InimigoTeletransportador(Inimigo):
    """
    Classe que define inimigos teletransportadores, surpreendem o Jogador ao
    aparecer do nada para atacar e depois desaparecer
    """
    
    def __init__(self, x: int, y: int, velocidade: int,
                    dano: int, sprite: str,
                    cooldown_ataque: int, vida=10):
        super().__init__(x, y, velocidade,
                        dano, sprite, vida)
        
        self._pulo_completo = False
        self._sprite_original = self._sprite
        self._cooldown_ataque = cooldown_ataque
        self._tempo_inicio_ataque = pygame.time.get_ticks()
        self._atacando = False

        self._settings = Settings()

    def atacar(self, jogador_x, jogador_y):
        tempo_agora = pygame.time.get_ticks()


        if tempo_agora - self._tempo_inicio_ataque >= self._cooldown_ataque or self._atacando:
            self._rect.x, self._rect.y = jogador_x, jogador_y



    def mover(self, x: int, y: int):
        pass

    def desaparecer(self):
        if self._pulo_completo:
            self._sprite = ""
