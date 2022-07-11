from Jogo import Jogo

j = Jogo()
j.iniciar_nova_rodada()

while j.rodando:
    j.rodar_jogo()