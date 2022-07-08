from decimal import DivisionByZero
from Inimigo import Inimigo
from Jogador import Jogador
import pygame
from pygame.locals import *
import numpy as np


class ControladorInimigo:
    def achar_caminho(self, inimigo, jogador_x, jogador_y):
        distx = jogador_x - inimigo.x
        disty = jogador_y - inimigo.y

        try:
            angulo = np.arctan(disty / distx)
        except DivisionByZero:
            angulo = np.arctan(disty / 1)

        xmov = inimigo.velocidade * np.sin(angulo)
        ymov = inimigo.velocidade * np.cos(angulo)

        if jogador_x >= inimigo.x and jogador_y >= inimigo.y:
            inimigo.mover(xmov, ymov, sentidox=1, sentidoy=1)
        elif jogador_x <= inimigo.x and jogador_y >= inimigo.y:
            inimigo.mover(xmov, ymov, sentidox=-1, sentidoy=1)
        elif jogador_x >= inimigo.x and jogador_y <= inimigo.y:
            inimigo.mover(xmov, ymov, sentidox=1, sentidoy=-1)
        else:
            inimigo.mover(xmov, ymov, sentidox=-1, sentidoy=-1)
