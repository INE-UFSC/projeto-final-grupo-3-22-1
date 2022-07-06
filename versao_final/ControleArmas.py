from Arma import Arma

class ControleArmas:
    def __init__(self):
        self.__armas = {}
        self.__armas["anzol"] = Arma(0, 20, 4, "isca")
        self.__armas["tarrafa"] = Arma(15, 13, 8, "rede")
    
    def trocar_arma(self, nome_arma: str):
        return self.__armas[nome_arma]
    
        