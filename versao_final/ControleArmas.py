from Arma import Arma
from Jogador import Jogador


class ControleArmas:
    def __init__(self):
        # pode ter "jogador" como property?
        self.__armas = {}
        self.__armas["isca"] = Arma(0, 20, 4, 250, "isca", 1)
        self.__armas["rede"] = Arma(15, 13, 8, 750, "rede", 15)

    def trocar_arma(self, jogador: Jogador, nome_arma: str):
        jogador.arma = self.__armas[nome_arma]
