# Criando dicionarios em Python
pessoa = {"nome": "João",
"idade": 30,
"cidade": "São Paulo"}
print(pessoa)

# Acessando valores
print(pessoa["nome"])
print(pessoa.get("idade"))
print(pessoa.get("profissão", "Não especificado"))  # Retorna valor padrão se a chave não existir

# Adicionando ou atualizando valores
pessoa["profissão"] = "Engenheiro"
print(pessoa)
pessoa["idade"] = 31
print(pessoa)

# Removendo valores
del pessoa["cidade"]
print(pessoa)
removed_value = pessoa.pop("profissão", "Chave não encontrada")
print(removed_value)
print(pessoa)

# Iterando sobre dicionários
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")
    
# Verificando existência de chave
if "nome" in pessoa:
    print("A chave 'nome' existe no dicionário.")


contatos = {
    "Alice": {"telefone": "1234-5678", "email": "alice@email.com"},
    "Bob": {"telefone": "9876-5432", "email": "bob@email.com"},
    "Charlie": {"telefone": "5555-6666", "email": "charlie@email.com"},
    "Diana": {"telefone": "1111-2222", "email": "diana@email.com"}
}

#Acessando informações de contatos

contatos["Alice"]["telefone"] 
print(contatos["Alice"]["telefone"])