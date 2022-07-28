from cmath import cos, sin
from math import atan2
import pygame
import random as rd
from math import sin, cos, atan2

from Settings import Settings
from Globals import Globals
from Bala import Bala
from BombaVeneno import BombaVeneno
from BombaLava import BombaLava


class Boss(pygame.sprite.Sprite):
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
        super().__init__()
        self._dano = dano
        self._vel_mov = vel_mov
        self._vel_atq = vel_atq
        self._vida = vida
        self._sprite = pygame.image.load(sprite)
        self._rect = self._sprite.get_rect(center=(x, y))

        self._settings = Settings()
        self._globals = Globals()

        self._tempo_ultimo_especial = 0
        self._tempo_ultimo_mov = 0
        self._tempo_ultimo_tiro = 0

    def atacar(self, jogador_x, jogador_y):
        choice = rd.choice([0, 1])

        if abs(jogador_x - self._rect.x) < 20:
            return self._ataque_proximo(self._rect.x, self._rect.y)

        if choice == 0:
            return self._ataque_distancia(jogador_x, jogador_y)
        return self._ataque_especial(jogador_x, jogador_y)

    def _ataque_distancia(self, jogador_x, jogador_y):
        """O InimigoAtirador vai atirar projéteis na direção do Jogador"""

        # obtém o tempo quando o método é chamado, para comparar com o tempo salvo
        # isso é a base do sistema de cadência de tiros
        tempo_agora = pygame.time.get_ticks()

        # compara o tempo obtido com o tempo salvo para checar se está dentro do tempo de cadência
        if tempo_agora - self._tempo_ultimo_tiro > 5000:
            # atualiza o tempo
            self._tempo_ultimo_tiro = tempo_agora

            # calcula as distâncias da posição do jogador à posição do inimigo
            distancia_x = jogador_x - self._rect.x
            distancia_y = jogador_y - self._rect.y

            # calcula o ângulo entre essas distâncias e com isso calcula a velocidade do projétil
            angulo = atan2(distancia_y, distancia_x)

            speed_x = self._vel_atq * cos(angulo)
            speed_y = self._vel_atq * sin(angulo)

            # instancia uma nova Bala de acordo com as informações obtidas e retorna a mesma
            incr = -0.05
            balas_boss = []
            for _ in range(5):
                nova_bala = Bala(
                    self._rect.x,
                    self._rect.y,
                    speed_x + incr,
                    speed_y + incr,
                    pygame.image.load("assets/isca.png"),
                    3,
                    20,
                )

                incr += 0.25
                balas_boss.append(nova_bala)

            return balas_boss

    def _ataque_proximo(self, x, y):

        tempo_agora = pygame.time.get_ticks()

        signal = 1
        while tempo_agora - self._tempo_comeco_ataque <= 500:
            self._rect.x += signal
            self._rect.y += signal
            signal *= -1

        return BombaVeneno(x, y, pygame.image.load("assets/mancha_veneno.png"), 5)

    def _ataque_especial(self, x, y):

        tempo_agora = pygame.time.get_ticks()

        if tempo_agora - self._tempo_ultimo_especial  > 1000:
            self._tempo_ultimo_especial = tempo_agora

            return BombaLava(
                x + rd.choice([-50, -70, 50, 70]),
                y + rd.choice([-50, -70, 50, 70]),
                pygame.image.load("assets/mancha_lava.png"),
                5,
             )

    def mover(self):
        
        tempo_agora = pygame.time.get_ticks()

        if tempo_agora - self._tempo_ultimo_mov >= 500:
            self._tempo_ultimo_mov = tempo_agora

            self._rect.x += rd.choice([-2, -1.5, -1, 1, 1.5, 2]) * self._vel_mov
            self._rect.y += rd.choice([-2, -1.5, -1, 1, 1.5, 2]) * self._vel_mov
    
    def receber_dano(self, dano):
        self._vida -= dano
    
    @property
    def sprite(self) -> str:
        return self._sprite
    
    @property
    def vida(self) -> int:
        return self._vida
    
    @property
    def rect(self) -> tuple:
        return self._rect
    
    @property
    def x(self) -> int:
        return self._rect.x
    
    @property
    def y(self) -> int:
        return self._rect.y
    
    @property
    def dano(self) -> int:
        return self._dano
