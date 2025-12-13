numero = int(input("Qual tabuada você quer ver? "))
step = int(input("De quanto em quanto você quer ver? "))

for i in range(1, 11, step):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
# Calculadora de Tabuada Simples