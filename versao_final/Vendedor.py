import pygame
from pygame.locals import *

from Arma import Arma
from Melhoria import Melhoria
from InterfaceVendedor


class Vendedor(pygame.sprite.Sprite):
    def __init__(self, lista_armas: list, lista_upgrades: list):
        self._itens_disponiveis = lista_armas.extend(lista_upgrades)

    def mostrar_itens(self):
        pass
        #return InterfaceVendedor()
    
    def vender_item(self, item):
        item_vendido = self._itens_disponiveis.pop(item)
        return item_vendido

    @property
    def itens_disponivies(self) -> list:
        return self._itens_disponiveis
    
    @itens_disponiveis.setter
    def itens_disponiveis(self, itens):
        self._itens_disponiveis = itens
    
    # precisa de funcao para modificar a lista de itens ao comprar?
    # def comprar_item(self):
    #     ...