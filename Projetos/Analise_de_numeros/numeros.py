numeros = []

quant = int(input("Quantos números você quer adicionar? "))

if quant == 0:
    print("Nenhum número foi digitado.")
else:
    for i in range(quant):
        num = int(input(f"Digite o {i+1}º número: "))
        numeros.append(num)

def avaliacao_numerica():
    print(f"Números digitados: {numeros}")
    print(f"Soma: {sum(numeros)}")
    print(f"Maior número: {max(numeros)}")
    print(f"Menor número: {min(numeros)}")

    numeros_pares = [valor for valor in numeros if valor % 2 == 0]
    print(f"Pares: {numeros_pares}")

    numeros_media = sum(numeros) / len(numeros)
    print(f"Média: {numeros_media:.2f}")
    
avaliacao_numerica()

alterar = input("Deseja alterar um número? (s/n) ")
if alterar == "s":
    index_numero = int(input("Qual o indice do numero que você deseja alterar? "))
    print(f"O número no índice {index_numero} é: {numeros[index_numero]} ")  
    novo_valor = int(input("Digite o novo valor valor: ")) 
    numeros[index_numero] = novo_valor
    avaliacao_numerica()
else:
    print("Obrigada por participar!")    
    

