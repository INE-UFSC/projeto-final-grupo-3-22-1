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
    
    # provavelmente teremos que usar isso para alguma coisa, então não deletei o arquivo ainda