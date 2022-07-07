from Arma import Arma

class ControleArmas:
    def __init__(self):
        self.__armas = {}
        self.__armas["isca"] = Arma(0, 20, 4, 250, "isca")
        self.__armas["rede"] = Arma(15, 13, 8, 750, "rede")
    
    def trocar_arma(self, nome_arma: str):
        return self.__armas[nome_arma]
    
        