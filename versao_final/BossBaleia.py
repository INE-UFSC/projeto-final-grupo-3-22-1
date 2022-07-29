from cmath import cos, sin
from math import atan2
import pygame
import random as rd
from math import sin, cos, atan2, hypot

from Boss import Boss
from DragaoAgua import DragaoAgua


class BossBaleia(Boss):
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

    def _ataque_especial(self, x, y):
        
        print("chegou aqui")
        return DragaoAgua(
            x + rd.choice([-80, -110, 80, 110]),
            y + rd.choice([-80, -110, 80, 110]),
            pygame.image.load("assets/dragao_agua.png"),
            10,
            20
            )