import pygame

def exibir_tabuleiro(tabuleiro):
    # Função de Exibição do tabuleiro na tela
    for linha in tabuleiro:
        # Junta os elementos de cada linha com um "|" entre eles
        print("|".join(linha))
        print("-----")  # Exibe uma linha horizontal entre as linhas do tabuleiro


def verificar_vitoria(tabuleiro, simbolo):
    # Verifica se há uma vitória nas linhas, colunas ou diagonais
    for i in range(3):
        # Verifica vitória em linhas
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] == simbolo:
            return True
        # Verifica vitória em colunas
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] == simbolo:
            return True
    # Verifica vitória na diagonal principal
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == simbolo:
        return True
    # Verifica vitória na diagonal secundária
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == simbolo:
        return True
    return False


def jogar_jogo_da_velha():
    # Inicializa o tabuleiro com espaços em branco
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]

    # Pede aos jogadores para escolherem seus símbolos
    jogador1 = input("Jogador 1, escolha X ou O: ").upper()
    # Se jogador 1 não escolher "X" e nem "O"
    while jogador1 != "X" and jogador1 != "O":
        # Mensagem de atenção
        jogador1 = input(
            "Escolha inválida. Jogador 1, escolha X ou O: ").upper()
#  Se jogador 1 escolher "X", automaticamente o jogador 2 ficará com "O"
    if jogador1 == "X":
        jogador2 = "O"
    else:
        jogador2 = "X"

    jogador_atual = 1
    simbolo_atual = jogador1

    while True:
        print("Jogador", jogador_atual)
        exibir_tabuleiro(tabuleiro)
        linha = int(input("Digite o número da linha (0, 1 ou 2): "))
        coluna = int(input("Digite o número da coluna (0, 1 ou 2): "))

        if tabuleiro[linha][coluna] == " ":
            # Atualiza o tabuleiro com o símbolo do jogador atual na posição escolhida
            tabuleiro[linha][coluna] = simbolo_atual

            if verificar_vitoria(tabuleiro, simbolo_atual):
                # Verifica se o jogador atual venceu
                print("Jogador", jogador_atual, "venceu!")
                exibir_tabuleiro(tabuleiro)
                break
            elif all(all(linha != " " for linha in linha_tabuleiro) for linha_tabuleiro in tabuleiro):
                # Verifica se houve empate, ou seja, todas as posições estão preenchidas
                print("Empate!")
                exibir_tabuleiro(tabuleiro)
                break

            # Troca o jogador atual e o símbolo atual para o próximo jogador

        if jogador_atual == 1:
            jogador_atual = 2
            simbolo_atual = jogador2
        else:
            jogador_atual = 1
            simbolo_atual = jogador1
    else:
        print("Essa posição já está ocupada. Tente novamente.")
