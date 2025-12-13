valores = [10, 25, 30, 45, 50, 65, 70, 85, 90]

# Lista de valores pares
pares = [valor for valor in valores if valor % 2 == 0]
print(pares)  
 
 # Lista de valores elevados ao quadrado se maiores que 60
quadrados = [valor ** 2 for valor in valores if valor > 60]
print(quadrados)

# Filtragem de valores em uma única linha usando list comprehension