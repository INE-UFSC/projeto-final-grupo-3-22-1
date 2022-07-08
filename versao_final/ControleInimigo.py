from decimal import DivisionByZero
from Inimigo import Inimigo
from Jogador import Jogador
import pygame
from pygame.locals import *
import numpy as np

class ControladorInimigo():
    def checar_colisao(self, inimigo, jogador):
        if jogador.rect.colliderect(inimigo.rect):
            jogador.vida -= inimigo.dano
            
    def checar_sofreu_dano(self, inimigo, lista_balas):
        for bala in lista_balas:
            if bala.rect.colliderect(inimigo.rect):
                
                inimigo.vida -= bala.dano
                print("dano")
    
    def achar_caminho(self, inimigo, jogador_x, jogador_y):
        distx = jogador_x - inimigo.x
        disty = jogador_y - inimigo.y

        try:
            angulo = np.arctan(disty/distx)
        except DivisionByZero:
            angulo = np.arctan(disty/1)
        
        xmov = inimigo.velocidade * np.sin(angulo)
        ymov = inimigo.velocidade * np.cos(angulo)

        if jogador_x >= inimigo.x and jogador_y >= inimigo.y:
            inimigo.mover(xmov, ymov, sentidox = 1, sentidoy = 1)
        elif jogador_x <= inimigo.x and jogador_y >= inimigo.y:
            inimigo.mover(xmov, ymov, sentidox = -1, sentidoy = 1)
        elif jogador_x >= inimigo.x and jogador_y <= inimigo.y:
            inimigo.mover(xmov, ymov, sentidox = 1, sentidoy = -1)
        else:
            inimigo.mover(xmov, ymov, sentidox = -1, sentidoy = -1)

