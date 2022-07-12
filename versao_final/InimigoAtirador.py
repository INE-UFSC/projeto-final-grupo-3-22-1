import pygame
from pygame.locals import *

from math import sin, cos, atan2, hypot


import random as rd
from Settings import Settings
from Bala import Bala


class InimigoAtirador(pygame.sprite.Sprite):
    """
    Classe que define inimigos atiradores, que evitam o jogador e atiram
    projéteis de uma distância segura
    """
    
    def __init__(self, x: int, y: int, velocidade: int,
                    dano: int, sprite: str,
                    velocidade_ataque: int, vida=10):
        # self.__tipo_ataque = tipo_ataque
        # self.__pontos_concedidos = pontos_concedidos
        # self.__comprimento = comprimento
        super().__init__()
        self.__x = x
        self.__y = y
        self.__velocidade = velocidade
        self.__dano = dano
        self.__velocidade_ataque = velocidade_ataque
        self.__sprite = pygame.image.load(sprite)
        self.image = pygame.image.load(sprite)
        self.__rect = self.__sprite.get_rect(center=(self.__x, self.__y))
        self.__vida = vida
        self.__tempo_ultimo_tiro = 0
        self.__tempo_ultimo_movimento = 0

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
        self.__rect.x += x * self.__velocidade
        self.__rect.y += y * self.__velocidade
    
    def achar_caminho(self, inimigo, jogador_x, jogador_y, raio=20) -> int:
        # Achando os catetos e a hipotenusa
        distx, disty = jogador_x - inimigo.x, jogador_y - inimigo.y
        hyp = hypot(distx, disty)

        # Normalizando as distâncias
        distx, disty = distx / hyp, disty / hyp
        tempo_agora = pygame.time.get_ticks()

        # Checando se o jogador está perto,
        # se sim, fugir dele
        # se não, caminho aleatório
        if abs(jogador_x - inimigo.x) <= raio:
            return -2.5*distx, -2.5*disty
        elif tempo_agora - self.__tempo_ultimo_movimento >= 200:
            x = rd.choice([1, -1])
            y = rd.choice([1, -1])
            
            # Atualiza o tempo
            self.__tempo_ultimo_movimento = tempo_agora
            
            return x, y
                
        # Caso não haja nenhum movimento acima, retorna 0, 0
        return 0, 0 

    def desenhar(self):
        # Desenha o sprite do inimigo na tela 
        self.settings.DISPLAY_SURF.blit(self.__sprite, (self.x, self.y))

    @property
    def x(self) -> int:
        return self.__rect.x

    @property
    def y(self) -> int:
        return self.__rect.y

    @property
    def velocidade(self) -> int:
        return self.__velocidade

    @property
    def sprite(self) -> str:
        return self.__sprite

    @property
    def dano(self) -> int:
        return self.__dano

    @property
    def rect(self) -> tuple:
        return self.__rect

    @property
    def vida(self) -> int:
        return self.__vida

    @vida.setter
    def vida(self, vida: int):
        self.__vida = vida

    @property
    def settings(self) -> Settings:
        return self.__settings

    def receber_dano(self, dano: int):
        self.vida -= dano

        if self.vida <= 0:
            self.kill()
