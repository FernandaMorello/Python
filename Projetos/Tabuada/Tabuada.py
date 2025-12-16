gerou_tabuada = False


def gerar_tabuada(numero, inicio, fim, passo):
    print(f"\nTabuada do {numero}")
    print("-" * 25)

    for i in range(inicio, fim + passo, passo):
        print(f"{numero} x {i} = {numero * i}")


while True:
    if not gerou_tabuada:
        menu = input("""
O que você deseja fazer?
1 - Gerar Tabuada
2 - Sair

Escolha: """)
    else:
        menu = input("""
O que você deseja fazer?
1 - Gerar Outra Tabuada
2 - Sair

Escolha: """)

    if menu == "1":
        numero = int(input("Qual tabuada você quer ver? "))
        inicio_tabuada = int(input("Em que número deverá começar a tabuada? "))
        fim_tabuada = int(input("Em que número deverá terminar a tabuada? "))
        step = int(input("De quanto em quanto você quer ver? "))

        # Validação do passo
        if step == 0:
            print("Erro: o passo não pode ser zero.")
            continue

        # Ajuste automático para intervalo invertido
        if inicio_tabuada > fim_tabuada and step > 0:
            step = -step

        gerar_tabuada(numero, inicio_tabuada, fim_tabuada, step)
        gerou_tabuada = True

    elif menu == "2":
        break

    else:
        print("Opção inválida!")
