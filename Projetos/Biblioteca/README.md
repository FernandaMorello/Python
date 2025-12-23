# 📚 Sistema de Biblioteca em Python (Terminal)

Este projeto é um **sistema simples de gerenciamento de biblioteca**, desenvolvido em **Python**, que permite ao usuário **cadastrar, remover, emprestar, devolver e consultar livros** por meio de um **menu interativo no terminal**.

O objetivo do projeto é **praticar lógica de programação**, uso de **estruturas de dados**, **condicionais**, **laços de repetição** e **interação com o usuário**, além de aplicar boas práticas de organização e padronização do código.

---

## 🎯 Funcionalidades

* Menu interativo no terminal
* Cadastro de livros na biblioteca
* Remoção de livros disponíveis
* Empréstimo de livros
* Devolução de livros emprestados
* Consulta da disponibilidade de um livro
* Visualização:

  * Livros emprestados
  * Livros disponíveis na biblioteca
  * Todos os livros cadastrados
* Padronização automática dos nomes dos livros
* Mensagens coloridas no terminal para melhor usabilidade

---

## 🎨 Cores e Significados no Terminal

O sistema utiliza **códigos ANSI** para colorir as mensagens exibidas no terminal, tornando a interação mais clara e intuitiva.

As cores possuem os seguintes significados:

* 🟢 **Verde**
  Indica **ações realizadas com sucesso**, como:

  * Cadastro de livros
  * Remoção de livros
  * Empréstimos realizados
  * Devoluções concluídas

* 🔴 **Vermelho**
  Indica **erros ou ações inválidas**, como:

  * Livro não encontrado
  * Tentativa de remover um livro emprestado
  * Tentativa de devolver um livro inexistente

* 🟡 **Amarelo**
  Utilizada para **avisos e estados informativos**, como:

  * Exibição dos livros disponíveis na biblioteca

* 🔵 **Azul**
  Utilizada para **exibição de informações gerais**, como:

  * Lista de livros emprestados

* 🟣 **Roxo**
  Utilizada para **informações agregadas**, como:

  * Exibição de todos os livros cadastrados (união da biblioteca com os emprestados)

> 📌 As cores são aplicadas por meio de **sequências ANSI**, compatíveis com a maioria dos terminais modernos (VS Code, PyCharm, Linux e macOS).

---

## 🧠 Conceitos praticados

* Estrutura de repetição `while`
* Estrutura condicional `if / elif / else`
* Estrutura de dados `set`
* Operações com conjuntos (`add`, `discard`, `union`)
* Validação de dados
* Organização de menus
* Uso de códigos ANSI para estilização no terminal
* Lógica de movimentação de dados entre conjuntos

---

## 🚀 Como executar

1. Certifique-se de ter o **Python 3** instalado
2. Clone o repositório ou baixe os arquivos
3. Acesse a pasta do projeto
4. Execute o programa com o comando:

```bash
python main.py
```

---

## 📌 Observações

* O sistema funciona **inteiramente no terminal**
* Não utiliza bibliotecas externas
* Os dados são armazenados apenas em memória
* Ao encerrar o programa, as informações são perdidas

---

