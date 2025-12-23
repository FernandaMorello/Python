numeros = set([1, 2, 3, 1, 3, 4, 5])
print(numeros)

letras = ["a", "b", "c", "a", "b", "d"]
print(set(letras))

linguagens = {"Python", "Java", "C++", "Python", "JavaScript"}
print(linguagens)
linguagens = list(linguagens)
print(linguagens[0])

# Adicionando elementos
frutas = {"maçã", "banana", "laranja"}
frutas.add("uva")
print(frutas)
frutas.add("banana")  # Não adiciona duplicatas
print(frutas)

# Removendo elementos
frutas.remove("laranja")
print(frutas)
# frutas.remove("abacaxi")  # Isso geraria um erro se o elemento não existir
frutas.discard("abacaxi")  # Não gera erro se o elemento não existir
print(frutas)

# Verificando existência
print("maçã" in frutas)
print("abacaxi" in frutas)

# Operações com conjuntos
conjunto_a = {1, 2, 3, 4}
conjunto_b = {3, 4, 5, 6}
uniao = conjunto_a.union(conjunto_b)
intersecao = conjunto_a.intersection(conjunto_b)
diferenca_conjunto_a = conjunto_a.difference(conjunto_b)
diferenca_conjunto_b = conjunto_b.difference(conjunto_a)
symetric_difference = conjunto_a.symmetric_difference(conjunto_b)

# Exibindo resultados
print("União:", uniao)
print("Interseção:", intersecao)
print("Diferença do conjunto_a:", diferenca_conjunto_a)
print("Diferença do conjunto_b:", diferenca_conjunto_b)
print("Diferença simétrica:", symetric_difference)


# Tamanho do conjunto
print("Tamanho do conjunto_a:", len(conjunto_a))
print("Tamanho do conjunto_b:", len(conjunto_b))    


# Conjuntos pertencem a outros conjuntos
conjunto_c = {1, 2}
print(conjunto_c.issubset(conjunto_a))  # True
print(conjunto_a.issuperset(conjunto_c))  # True
print(conjunto_a.isdisjoint(conjunto_b))  # False
#isdisjoint verifica se não há elementos em comum entre os conjuntos e retorna True se
#não houver elementos em comum e False caso contrário.


# Limpando conjunto
conjunto_a.clear()
print("Conjunto_a após limpar:", conjunto_a)


