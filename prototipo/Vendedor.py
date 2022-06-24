import pygame
from pygame.locals import *

from Arma import Arma
from Melhoria import Melhoria


class Vendedor(pygame.sprite.Sprite):
    def __init__(self):
        self.__itens_disponivies = []
    
    @property
    def itens_disponivies(self) -> list:
        return self.__itens_disponivies
    
    @itens_disponivies.setter
    def itens_disponivies(self, itens):
        self.__itens_disponivies = itens
    
    def gerar_itens(self):
        ...
    
    # precisa de funcao para modificar a lista de itens ao comprar?
    # def comprar_item(self):
    #     ...