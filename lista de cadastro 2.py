import pygame 
import tkinter as tk

pygame.init()

# Configurações da tela
WIDTH = 800
HEIGHT = 600
BG_COLOR = (255, 255, 255)

# Inicializa a tela
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Função que exibe a janela de cadastro
def show_register_window():
    # Cria uma janela do tkinter
    register_window = tk.Tk()
    register_window.title("Cadastro de Jogadores")

    # Cria um campo de texto para o nome do jogador
    player_name_label = tk.Label(register_window, text="Nome do Jogador:")
    player_name_label.pack()
    player_name_entry = tk.Entry(register_window)
    player_name_entry.pack()

    # Cria um botão para enviar o cadastro
    register_button = tk.Button(register_window, text="Cadastrar",
                                command=lambda: register_player(player_name_entry.get(), register_window))
    register_button.pack()

    register_window.mainloop()

# Função que salva o nome do jogador
def register_player(name, window):
    # Salva o nome do jogador em um arquivo ou banco de dados, por exemplo
    print("Jogador cadastrado:", name)

    # Fecha a janela de cadastro
    window.destroy()

# Exibe a janela de cadastro quando o jogo é iniciado
show_register_window()

# Loop principal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Preenche o fundo com a cor branca
    screen.fill(BG_COLOR)

    pygame.display.update()

pygame.quit()
