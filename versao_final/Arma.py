from Melhoria import Melhoria
import os


class Arma:
    def __init__(self, preco: int, velocidade_projetil: int, dano: int, cadencia: int, nome_sprite: str, durabilidade_bala):
        self.__preco = preco
        self.__velocidade_projetil = velocidade_projetil
        self.__dano = dano
        # cadencia em ms
        self.__cadencia = cadencia
        self.__nome_sprite = "assets/" +  nome_sprite + ".png"
        self.__durabilidade_bala = durabilidade_bala

    @property
    def preco(self) -> int:
        return self.__preco

    @property
    def velocidade_projetil(self) -> int:
        return self.__velocidade_projetil
    
    @property
    def nome_sprite(self) -> str:
        return self.__nome_sprite

    @property
    def dano(self) -> int:
        return self.__dano
    
    @property
    def cadencia(self) -> int:
        return self.__cadencia
    
    @property
    def durabilidade_bala(self):
        return self.__durabilidade_bala

    def aplicar_melhoria(self, melhoria: Melhoria):
        ...

    def remover_melhoria(self):
        ...
