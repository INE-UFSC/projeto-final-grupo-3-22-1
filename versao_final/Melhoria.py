class Melhoria:
    def __init__(self, nome: str, modificacoes: dict):
        self.__nome = nome
        self.__modificacoes = modificacoes

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def modificacoes(self) -> dict:
        return self.__modificacoes
