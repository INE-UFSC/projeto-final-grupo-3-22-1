import pygame
from pygame.locals import *

from math import sin, cos, atan2

import random as rd
from Settings import Settings
from Bala import Bala
from Inimigo import Inimigo


class InimigoAtirador(Inimigo):
    """
    Classe que define inimigos atiradores, que evitam o jogador e atiram
    projéteis de uma distância segura
    """
    
    def __init__(self, x: int, y: int, velocidade: int,
                    dano: int, sprite: str,
                    velocidade_ataque: int, vida=10):
        super().__init__(x, y, velocidade,
                        dano, sprite, vida)
        
        self.__velocidade_ataque = velocidade_ataque
        self.__tempo_ultimo_tiro = 0

        self.__settings = Settings()

    def atacar(self, jogador_x, jogador_y):
        """O InimigoAtirador vai atirar projéteis na direção do Jogador"""

        # obtém o tempo quando o método é chamado, para comparar com o tempo salvo
        # isso é a base do sistema de cadência de tiros  
        tempo_agora = pygame.time.get_ticks()

        # compara o tempo obtido com o tempo salvo para checar se está dentro do tempo de cadência
        if tempo_agora - self.__tempo_ultimo_tiro > 5000:
            # atualiza o tempo
            self.__tempo_ultimo_tiro = tempo_agora


            # calcula as distâncias da posição do jogador à posição do inimigo
            distancia_x = jogador_x - self.__rect.x
            distancia_y = jogador_y - self.__rect.y

            # calcula o ângulo entre essas distâncias e com isso calcula a velocidade do projétil
            angulo = atan2(distancia_y, distancia_x)

            speed_x = self.__velocidade_ataque * cos(angulo)
            speed_y = self.__velocidade_ataque * sin(angulo)

            # instancia uma nova Bala de acordo com as informações obtidas e retorna a mesma
            nova_bala = Bala(
                self.rect.x,
                self.rect.y,
                speed_x,
                speed_y,
                pygame.image.load("assets/isca.png"),
                3,
                20)

            return nova_bala

    def mover(self, x, y):
        # Move-se ao multiplicar os xs e ys obtidos pelo processo de normalização 
        # pela velocidade do inimigo
        self.rect.x += x * self.velocidade
        self.rect.y += y * self.velocidade
