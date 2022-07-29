import pygame
from pygame.locals import *


class Arma:
    def __init__(
        self,
        velocidade_projetil: int,
        dano: int,
        cadencia: int,
        nome_sprite: str,
        durabilidade_bala,
    ):
        self.__stats = {
            "velocidade_projetil": velocidade_projetil,
            "dano": dano,
            "cadencia": cadencia,  # milisegundos
            "durabilidade_bala": durabilidade_bala,
        }

        self.__sprite_bala = pygame.image.load(f"assets/{nome_sprite}.png")
        self.__nome_sprite = "assets/" + nome_sprite + ".png"

    @property
    def stats(self) -> dict:
        return self.__stats

    @property
    def nome_sprite(self) -> str:
        return self.__nome_sprite

    @property
    def sprite_bala(self):
        return self.__sprite_bala
