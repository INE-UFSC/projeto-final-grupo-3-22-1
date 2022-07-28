from Arma import Arma
from Jogador import Jogador


class ControleArmas:
    def __init__(self, jogador: Jogador):
        self.__jogador = jogador
        self.__armas = {}
        self.__armas["isca"] = Arma(20, 4, 250, "isca", 1)
        self.__armas["rede"] = Arma(8, 10, 750, "rede", 50)
        self.__armas["arpao"] = Arma(12, 8, 500, "arpao", 4)

    @property
    def jogador(self) -> Jogador:
        return self.__jogador

    def trocar_arma(self, nome_arma: str):
        self.jogador.arma = self.__armas[nome_arma]
