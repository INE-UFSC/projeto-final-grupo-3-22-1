from InimigoBasico import Inimigo


class Boss(Inimigo):
    def __init__(
        self,
        vida,
        velocidade_movimento: int,
        tipo_de_ataque: list,
        pontuacao_concedida: int,
        estagios: int,
    ):
        super().__init__(
            vida, velocidade_movimento, tipo_de_ataque, pontuacao_concedida
        )
        self.__estagios = estagios

    @property
    def estagios(self) -> int:
        return self.__estagios
