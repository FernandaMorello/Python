biblioteca = set()
livros_emprestados = set()

while True:
    menu = input('''
    ===============================      
            Biblioteca
    ===============================

    Aperte a função que deseja executar:

    1- Adicionar um livro
    2- Remover um livro
    3- Emprestar um livro
    4- devolver um livro
    5- Consultar um livro
    6- Ver livros emprestados
    7- Ver livros na biblioteca
    8- Ver todos os livros
    9- Sair
    
    : ''')

    # CADASTRANDO UM LIVRO
    if menu == "1":    
        livro = input("Digite o livro que deseja cadastrar: ")
        biblioteca.add(livro.title())
        print(f"\033[32mLivro: {livro.title()}, adicionado com sucesso :)\033[m")

    # REMOVENDO UM LIVRO        
    elif menu == "2":
        livro = input("Digite o livro que deseja remover: ")
        if livro.title() in biblioteca:
            biblioteca.discard(livro.title())
            print(f"\033[32mLivro: {livro.title()}, removido com sucesso :)\033[m")
        elif livro.title() in livros_emprestados:
            print("\033[31mNão é possível remover livros emprestados\033[m")   
        else:
            print("\033[31mLivro não encontrado :(\033[m")

    # EMPRESTANDO UM LIVRO
    elif menu == "3":
        livro = input("Digite o livro a ser emprestado: ")
        if livro.title() in biblioteca:
            biblioteca.discard(livro.title())
            livros_emprestados.add(livro.title())   
            print(f"\033[32mLivro: {livro.title()}, cadastrado como emprestado com sucesso :)\033[m")
        else:
            print("\033[31mLivro não encontrado :(\033[m")

    # DEVOLVENDO UM LIVRO
    elif menu == "4":
        livro = input("Digite o livro que deseja devolver: ")
        if livro.title() in livros_emprestados:
            livros_emprestados.discard(livro.title())
            biblioteca.add(livro.title())
            print(f"\033[32mLivro: {livro.title()}, devolvido com sucesso :)\033[m")
        else:
            print("\033[31mLivro não encontrado :(\033[m")

    # CONSULTAR UM LIVRO
    elif menu == "5":
        livro = input("Digite o livro que está buscando: ")
        if livro.title() in biblioteca:
            print(f"\033[32mLivro: {livro.title()}, encontra-se na biblioteca\033[m")
        elif livro.title() in livros_emprestados:
            print(f"\033[33mLivro {livro.title()}, encontra-se já emprestado\033[m")
        else:
            print("\033[31mLivro não encontrado :(\033[m")

    # VISUALIZANDO LIVROS EMPRESTADOS
    elif menu == "6":
        print(f"\033[34m{livros_emprestados}\033[m")

    # VISUALIZANDO BIBLIOTECA
    elif menu == "7":
        print(f"\033[33m{biblioteca}\033[m")

    # VISUALIZANDO TODOS OS LIVROS
    elif menu == "8":
        uniao = biblioteca.union(livros_emprestados)
        print(f"\033[35m{uniao}\033[m")

    # SAIR
    elif menu == "9":
        break
