from Melhoria import Melhoria


class Arma:
    def __init__(
        self, dano: int, preco: int, velocidade_projetil: float, cadencia_tiro: float
    ):
        self.__dano = dano
        self.__preco = preco
        self.__velocidade_projetil = velocidade_projetil
        self.__cadencia_tiro = cadencia_tiro

    @property
    def dano(self) -> int:
        return self.__dano

    @property
    def preco(self) -> int:
        return self.__preco

    @property
    def velocidade_projetil(self) -> float:
        return self.__velocidade_projetil

    @property
    def cadencia_tiro(self) -> float:
        return self.__cadencia_tiro

    def aplicar_melhoria(self, melhoria: Melhoria):
        ...
    
    def remover_melhoria(self):
        ...