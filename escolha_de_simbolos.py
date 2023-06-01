import pygame

pygame.init()
tamanho_janela = (300, 300)
janela = pygame.display.set_mode(tamanho_janela)
pygame.display.set_caption("Jogo da Velha")

# Essa parte do código importa a biblioteca pygame e cria uma janela para o jogo.

def exibir_tabuleiro(tabuleiro):
    # Essa função mostra o tabuleiro na tela.
    for linha in tabuleiro:
        # Coloca um "|" entre os elementos de cada linha.
        print("|".join(linha))
        print("-----")  # Mostra uma linha horizontal entre as linhas do tabuleiro.

# Essa função verifica se alguém ganhou o jogo.
def verificar_vitoria(tabuleiro, simbolo):
    for i in range(3):
        # Verifica se alguém ganhou nas linhas.
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] == simbolo:
            return True
        # Verifica se alguém ganhou nas colunas.
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] == simbolo:
            return True
    # Verifica se alguém ganhou na diagonal principal.
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == simbolo:
        return True
    # Verifica se alguém ganhou na diagonal secundária.
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == simbolo:
        return True
    return False

# Essa função é o jogo em si.
def jogar_jogo_da_velha():
    # Cria um tabuleiro vazio.
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]

    # Pergunta aos jogadores qual símbolo eles querem usar.
    jogador1 = input("Jogador 1, escolha X ou O: ").upper()
    while jogador1 != "X" and jogador1 != "O":
        jogador1 = input(
            "Escolha inválida. Jogador 1, escolha X ou O: ").upper()
    if jogador1 == "X":
        jogador2 = "O"
    else:
        jogador2 = "X"

    jogador_atual = 1
    simbolo_atual = jogador1

    # O jogo continua até alguém ganhar ou empatar.
    while True:
        print("Jogador", jogador_atual)
        exibir_tabuleiro(tabuleiro)
        linha = int(input("Digite o número da linha (0, 1 ou 2): "))
        coluna = int(input("Digite o número da coluna (0, 1 ou 2): "))

        # Verifica se a posição escolhida está vazia.
        if tabuleiro[linha][coluna] == " ":
            tabuleiro[linha][coluna] = simbolo_atual

            # Verifica se o jogador atual ganhou.
            if verificar_vitoria(tabuleiro, simbolo_atual):
                print("Jogador", jogador_atual, "venceu!")
                exibir_tabuleiro(tabuleiro)
                break
            # Verifica se houve empate.
            elif all(all(linha != " " for linha in linha_tabuleiro) for linha_tabuleiro in tabuleiro):
                print("Empate!")
                exibir_tabuleiro(tabuleiro)
                break

            # Troca o jogador e o símbolo para o próximo jogador.
            if jogador_atual == 1:
                jogador_atual = 2
                simbolo_atual = jogador2
            else:
                jogador_atual = 1
                simbolo_atual = jogador1
        else:
            print("Essa posição já está ocupada. Tente novamente.")
