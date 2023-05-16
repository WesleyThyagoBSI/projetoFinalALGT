import pygame
import tkinter as tk

pygame.init()

# Configurações da tela
WIDTH = 800
HEIGHT = 600
BG_COLOR = (255, 255, 255)

# Variáveis de controle de cadastro
jogador1_registrado = False
jogador2_registrado = False

# Função que salva o nome do jogador
def registrar_jogador(name1, name2, janela):
    global jogador1_registrado, jogador2_registrado

    if name1 and name2:
        # Salva o nome do jogador em um arquivo ou banco de dados, por exemplo
        print("Jogador 1 cadastrado:", name1)
        print("Jogador 2 cadastrado:", name2)

        jogador1_registrado = True
        jogador2_registrado = True

        # Fecha a janela de cadastro
        janela.destroy()
    else:
        # Exibe uma mensagem de erro se algum jogador não for cadastrado
        error_label = tk.Label(janela, text="Ambos os jogadores devem ser cadastrados!")
        error_label.pack()

# Função que exibe a janela de cadastro
def show_register_window():
    # Cria uma janela do tkinter
    register_window = tk.Tk()
    register_window.title("Cadastro de Jogadores")

    # Cria um campo de texto para o nome do jogador 1
    jogador_nome_etiqueta_1 = tk.Label(register_window, text="Nome do Jogador 1:")
    jogador_nome_etiqueta_1.pack()
    jogador_nome_entrada_1 = tk.Entry(register_window)
    jogador_nome_entrada_1.pack()

    # Cria um campo de texto para o nome do jogador 2
    jogador_nome_etiqueta_2 = tk.Label(register_window, text="Nome do Jogador 2:")
    jogador_nome_etiqueta_2.pack()
    jogador_nome_entrada_2 = tk.Entry(register_window)
    jogador_nome_entrada_2.pack()

    # Cria um botão para enviar o cadastro
    register_button = tk.Button(register_window, text="Cadastrar",
                                command=lambda: registrar_jogador(name1=jogador_nome_entrada_1.get(), name2=jogador_nome_entrada_2.get(), janela=register_window))
    register_button.pack()

    register_window.mainloop()

# Loop principal do jogo
while not (jogador1_registrado and jogador2_registrado):
    show_register_window()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Preenche o fundo com a cor branca
    screen.fill(BG_COLOR)

    pygame.display.update()

pygame.quit()

