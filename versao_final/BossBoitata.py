from cmath import cos, sin
from math import atan2
import pygame
from math import sin, cos, atan2

from Boss import Boss
from Bala import Bala

class BossBoitata(Boss):
    def __init__(
        self,
        x: int,
        y: int,
        dano: int,
        vida: int,
        sprite: str,
        vel_mov: int,
        vel_atq: int,
    ):
        super().__init__(x, y, dano, vida,
                            sprite, vel_mov, vel_atq)

    def _ataque_distancia(self, jogador_x, jogador_y):
        # calcula as distâncias da posição do jogador à posição do inimigo
        distancia_x = jogador_x - self._rect.x
        distancia_y = jogador_y - self._rect.y

        # calcula o ângulo entre essas distâncias e com isso calcula a velocidade do projétil
        angulo = atan2(distancia_y, distancia_x)

        balas_boss = []
        ang_diff = -1.2
        for _ in range(7):
            speed_x, speed_y = self._vel_atq * cos(angulo+ang_diff), self._vel_atq * sin(angulo+ang_diff)
            bala = Bala(self._rect.x, self._rect.y, speed_x, speed_y, pygame.image.load("assets/isca.png"), 3, 20)
            balas_boss.append(bala)
            ang_diff += 0.4
        
        return balas_boss