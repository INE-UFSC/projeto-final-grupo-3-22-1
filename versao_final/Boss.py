import pygame
from Settings import Settings
from Globals import Globals


class Boss():
    def __init__(self, x: int, y: int, dano: int,
                    vida: int, sprite: str,
                    vel_mov: int , vel_atq: int):
        self._dano = dano
        self._vel_mov = vel_mov
        self._vel_atq = vel_atq
        self._vida = vida
        self._sprite = pygame.image.load(sprite)
        self._rect = self._sprite.get_rect(center=(x, y))

        self._settings = Settings()
        self._globals = Globals()

    def atacar(self):


    def ataque_distancia(self, jogador_x, jogador_y):

