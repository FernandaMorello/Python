def salvar_carro(marca, modelo, ano, cor):
   print(f"Carro salvo: {marca} {modelo}, Ano: {ano}, Cor: {cor}")
   
salvar_carro("Toyota", "Corolla", 2020, "Prata")


def calcular_area_retangulo(largura, altura):
   area = largura * altura
   return area  
resultado = calcular_area_retangulo(5, 10)
print(f"Área do retângulo: {resultado}")


def saudacao(nome="Visitante"):
   return f"Olá, {nome}!"   
mensagem = saudacao("Carlos")
print(mensagem)

#Args e Kwargs
def listar_itens(*itens):
   for item in itens:
       print(f"- {item}")   
listar_itens("Maçã", "Banana", "Laranja")

def criar_perfil(**informacoes):
   perfil = {}
   for chave, valor in informacoes.items():
       perfil[chave] = valor
   return perfil
usuario = criar_perfil(nome="Ana", idade=25, cidade="Rio de Janeiro")
print(usuario)