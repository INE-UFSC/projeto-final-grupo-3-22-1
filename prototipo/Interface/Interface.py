from abc import ABC
from Pontuacao import Pontuacao


class Interface(ABC):
    def __init__(self, pontuacao: Pontuacao, vidas_atuais: int):
        self.__pontuacao = pontuacao
        self.__vidas_atuais = vidas_atuais

    @property
    def pontuacao(self) -> Pontuacao:
        return self.__pontuacao

    @property
    def vidas_atuais(self) -> int:
        return self.__vidas_atuais
