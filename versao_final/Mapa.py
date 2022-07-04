class Mapa:
    def __init__(self, nome: str, numero_de_ondas: int):
        self.__nome = nome
        self.__numero_de_ondas = numero_de_ondas
        self.__lista_de_inimigos = []
        
    @property
    def nome(self) -> str:
        return self.__nome
    
    @property
    def numero_de_ondas(self) -> int:
        return self.__numero_de_ondas

    @property
    def lista_de_inimigos(self) -> list:
        return self.__lista_de_inimigos