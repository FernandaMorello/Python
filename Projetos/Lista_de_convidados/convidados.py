
nomes = []


while True:
   menu = input(""" 
    1- Adicionar nome
    2- Remover nome
    3- Listar nomes
    4- Buscar nome
    5- Limpar a lista
    6- Sair

    Escolha uma opção: """)
   if menu == "1":
       nome = input("Digite o nome a ser adicionado: ")
       nomes.append(nome.title())
       print(f"{nome} adicionado à lista.")
       
   elif menu == "2":
       nome = input("Digite o nome a ser removido: ") 
       nome = nome.title()
       if nome not in nomes:
           print("Nome não encontrado!")
       else:
           print(f"Nome removido {nome}") 
           nome = nomes.remove(nome)
          
   elif menu == "3":
       print(nomes)
       
   elif menu == "4":
       nome = input("Digite um nome: ")
       nome = nome.title()
       if nome in nomes:
           print(f"{nome}, foi encontrado")
       else:
           print("Nome não encontrado")
                   
   elif menu == "5":
       confirmacao_limpeza = input("Tem certeza que deseja limpar a lista? (s/n) ")
       if confirmacao_limpeza == "s":
        nomes = nomes.clear()   
       
   elif menu == "6":
        break        
   
              