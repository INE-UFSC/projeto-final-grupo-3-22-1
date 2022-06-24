class Pontuacao:
    def __init__(self, pontos: int):
        self.__pontos = pontos

    @property
    def pontos(self) -> int:
        return self.__pontos

    @pontos.setter
    def pontos(self, pontos: int):
        self.__pontos = pontos

    def aumentar_pontuacao(self, pontos: int):
        ...

    def diminuir_pontuacao(self, pontos: int):
        ...

    def resetar_pontuacao(self):
        ...
