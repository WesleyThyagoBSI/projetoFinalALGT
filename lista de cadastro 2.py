import pygame 
import tkinter as tk

pygame.init()

# Configurações da tela
WIDTH = 800
HEIGHT = 600
BG_COLOR = (255, 255, 255)

# Função que salva o nome do jogador
def register_player(name1, name2, window):
    # Salva o nome do jogador em um arquivo ou banco de dados, por exemplo
    print("Jogador 1 cadastrado:", name1)
    print ("Jogador 2 cadastrado: ", name2) 

    # Fecha a janela de cadastro
    window.destroy()

# Função que exibe a janela de cadastro
def show_register_window():
    # Cria uma janela do tkinter
    register_window = tk.Tk()
    register_window.title("Cadastro de Jogadores")

    # Cria um campo de texto para o nome do jogador 1
    player_name_label_1 = tk.Label(register_window, text="Nome do Jogador 1:")
    player_name_label_1.pack()
    player_name_entry_1 = tk.Entry(register_window)
    player_name_entry_1.pack()

    # Cria um campo de texto para o nome do jogador 2
    player_name_label_2 = tk.Label(register_window, text="Nome do Jogador 2:")
    player_name_label_2.pack()
    player_name_entry_2 = tk.Entry(register_window)
    player_name_entry_2.pack()

    # Cria um botão para enviar o cadastro
    register_button = tk.Button(register_window, text="Cadastrar",
                                command=lambda: register_player(name1=player_name_entry_1.get(), name2=player_name_entry_2.get(), window=register_window))
    register_button.pack()

    register_window.mainloop()

# Exibe a janela de cadastro quando o jogo é iniciado
show_register_window()

# Loop principal do jogo
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

