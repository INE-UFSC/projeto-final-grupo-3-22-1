from Melhoria import Melhoria


class MelhoriaTemporaria(Melhoria):
    def __init__(self, nome: str, modificacoes: dict, duracao: int):
        super().__init__(nome, modificacoes)
        self.__duracao = duracao

    @property
    def duracao(self) -> int:
        return self.__duracao

    def encerrar_efeito(self):
        ...
