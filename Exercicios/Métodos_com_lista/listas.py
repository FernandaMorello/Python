lista = [3, "Python", [30,20,10]]

# Adicionando um elemento ao final da lista
lista.append(99)
print(lista) #[3, "Python", [30,20,10], 99


# Removendo o último elemento da lista
lista.pop()
print(lista) #[3, "Python", [30,20,10]]

# Removendo um elemento específico da lista
lista.remove("Python")
print(lista) #[3, [30,20,10]]

# Limpando todos os elementos da lista
print(lista) #[3, "Python", [30,20,10]]
lista.clear()
print(lista) #[]

# Copiando uma lista
l2 = lista.copy()
print(l2) #[]

cores = ["vermelho", "verde", "azul", "amarelo", "verde"]

# Contando quantas vezes um elemento aparece na lista
print(cores.count("verde")) #2

# Encontrando o índice de um elemento
print(cores.index("azul")) #2


# Encontrando o índice de um elemento a partir de uma posição específica
print(cores.index("verde", 2)) #4
# Juntando duas listas extend()
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista1.extend(lista2)
print(lista1) #[1, 2, 3, 4, 5, 6]

# Invertendo a ordem dos elementos na lista
lista1.reverse()
print(lista1) #[6, 5, 4, 3, 2, 1]

# Ordenando os elementos da lista
lista1.sort()
print(lista1) #[1, 2, 3, 4, 5, 6]

# Ordenando os elementos da lista em ordem decrescente
lista1.sort(reverse=True)
print(lista1) #[6, 5, 4, 3, 2, 1]

# Obtendo o tamanho da lista
print(len(lista1)) #6

