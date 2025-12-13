import os

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

nome = input("Qual é o seu nome? ")

print(f"Olá, {nome}! Bem-vindo ao jogo de adivinhação.")
num_perguntas = int(input("Para começar, digite o número de perguntas que você gostaria de fazer: "))

perguntas = []  

for i in range(num_perguntas):
    pergunta = input("Digite sua pergunta: ")
    perguntas.append(pergunta)
    limpar_tela()

print("\nPerguntas armazenadas:")
for p in perguntas:
    print("-", p)

input("\nVamos responder suas perguntas!")
limpar_tela()

respostas = []

for pergunta in perguntas:
    resposta = input(pergunta + " ")
    respostas.append(resposta)

limpar_tela()
print("Suas repostas:")
for i in range(num_perguntas):
    print(f"{perguntas[i]} → {respostas[i]}")
    
    vidas = 3
input("\nSegundo jogador pronto? (aperte enter)")    
limpar_tela()

for pergunta in perguntas:
    resposta_correta = input(pergunta + " ")
    limpar_tela()
    if resposta_correta.lower() == respostas[perguntas.index(pergunta)].lower():
        print("Resposta correta!")
    else:
        print(f"Resposta errada! A resposta correta era: {respostas[perguntas.index(pergunta)]}") 
        vidas -= 1   
        print(f"Vidas restantes: {vidas}"   )
        if vidas == 0:
            print("Você perdeu todas as suas vidas! Fim de jogo.")
            break
    
