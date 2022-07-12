from decimal import DivisionByZero
from InimigoBasico import InimigoBasico
from Jogador import Jogador
import pygame
from pygame.locals import *
import math 
import random as rd


class ControladorInimigo:
    def __init__(self):
        self.__ultimo_tempo = 0
    
    def caminho_rastreador(self, inimigo, jogador_x, jogador_y) -> int:
        # Achando os catetos e a hipotenusa
        distx, disty = jogador_x - inimigo.x, jogador_y - inimigo.y 
        hyp = math.hypot(distx, disty)

        # Normalizando as distâncias e retornando        
        distx, disty = distx / hyp, disty / hyp
        return distx, disty
    
    def caminho_atirador(self, inimigo, jogador_x, jogador_y, raio=20) -> int:
        # Achando os catetos e a hipotenusa
        distx, disty = jogador_x - inimigo.x, jogador_y - inimigo.y
        hyp = math.hypot(distx, disty)

        # Normalizando as distâncias
        distx, disty = distx / hyp, disty / hyp
        tempo_agora = pygame.time.get_ticks()

        # Checando se o jogador está perto,
        # se sim, fugir dele
        # se não, caminho aleatório
        if abs(jogador_x - inimigo.x) <= raio:
            return -2.5*distx, -2.5*disty
        elif tempo_agora - self.__ultimo_tempo >= 200:
            x = rd.choice([1, -1])
            y = rd.choice([1, -1])
            
            # Atualiza o tempo
            self.__ultimo_tempo = tempo_agora
            
            return x, y
                
        # Caso não haja nenhum movimento acima, retorna 0, 0
        return 0, 0 