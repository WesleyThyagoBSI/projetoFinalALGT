#sistema de pontuações#

ganhou = True
score = {"jogador_1":0,"jogador_2":0}

if(ganhou):
  quem_ganhou = input("Quem foi o jogador que ganhou?")
  if(quem_ganhou=="jogador_1"):
    score["jogador_1"] += 1
  elif(quem_ganhou=="jogador_2"):
    score["jogador_2"] += 1
    

print(f"Jogador 1: {score['jogador_1']}")
print(f"Jogador 2: {score['jogador_2']}")