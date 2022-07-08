from decimal import DivisionByZero
from Inimigo import Inimigo
from Jogador import Jogador
import pygame
from pygame.locals import *
import math 


class ControladorInimigo:
    def achar_caminho(self, inimigo, jogador_x, jogador_y):
        # Achando os catetos e a hipotenusa
        distx, disty = jogador_x - inimigo.x, jogador_y - inimigo.y 
        hyp = math.hypot(distx, disty)

        # Normalizando as distâncias e multiplicando isso pela velocidade do inimigo        
        distx, disty = distx / hyp, disty / hyp
        print(distx, disty)
        inimigo.mover(distx, disty)


