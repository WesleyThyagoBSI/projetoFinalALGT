players = []  # Lista que armazena os nomes dos jogadores cadastrados

# Loop para cadastrar jogadores
while True:
    name = input("Digite o nome do jogador (ou 'fim' para encerrar o cadastro): ")
    
    # Encerra o cadastro se o usuário digitar 'fim'
    if name.lower() == 'fim':
        break
    
    players.append(name)  # Adiciona o nome do jogador à lista de jogadores

# Exibe a lista de jogadores cadastrados
print("Jogadores cadastrados:")
for player in players:
    print("- " + player)
