#Cadastrar livros
def Cadastrar_livro(livros):
    while True:
        Titulo =  input('Digite o título do livro:') 
        Autor = input('Digite o autor do livro:')
        try:
           Ano = input('Digite o ano de publicação:')
        except ValueError as e: 
            print(e)
        livros.append({'Titulo':Titulo, 'Autor':Autor, 'Ano de publicação':Ano})
        break
    print('Livro cadastrado com sucesso!')
    return livros 


def lista_livro(livros):
    for dicenario in livros: 
        print("Livros Cadastrados:")
        print('_ _ _ _ _ _ _ _ _ _ _ _ _')
        print(f'Titulo:{dicenario["Titulo"]}\nAutor:{dicenario["Autor"]}\nAno:{dicenario["Ano de publicação"]}\n')

def pesquisa_titulo(livros, mostra=0):
    Titulo = input('Titulo:')
    for i,livro in enumerate(livros):
        if livro['Titulo'] == Titulo:
            if mostra:
               print(f"Titulo:{livro['Titulo']}\nAutor:{livro['Autor']}\nAno de publicação:{livro['Ano de publicação']}")
            return i
    return None

def pesquisa_autor(livros):
    Autor = input('Autor:')   
    livros_encontrado = [] 
    for i, livro in enumerate(livros):
        if livro['Autor'] == Autor:
            livros_encontrado.append(i)
            print()
            print(f"Titulo:{livro['Titulo']}\nAutor:{livro['Autor']}\nAno de publicação:{livro['Ano de publicação']}")
            print('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _')
    return livros_encontrado

def remover_livro(livros):
    opcoes = int(input('Opcoes Titulo[1], Autor[2]:'))
    if opcoes == 1:
        i = pesquisa_titulo(livros)  
        if i is not None:
            print(f"Titulo livros: {livros[i]['Titulo']}, Autor: {livros[i]['Autor']}")
            del livros[i]
            print(f'Removido com sucesso!')
        
    if opcoes == 2: 
        indice = pesquisa_autor(livros)
        for i in sorted(indice, reverse=True): 
            print(i)
            del livros[i]
            print('Autor deletado com sucesso!')
        
def perguta():
    print("""
O que você deseja fazer?
1 - Cadastrar um livro
2 - Listar todos os livros
3 - Pesquisar um livro
4 - Remover um livro
5 - Sair
          """)

def main():
    livros = []
    while True:
        perguta()
        try:
            resposta = int(input('Digite o número da opção desejada:'))
            if resposta == 1: 
                Cadastrar_livro(livros)
            elif resposta == 2:
                lista_livro(livros)
            elif resposta == 3:         
                if pesquisa_titulo(livros, 1) is None:
                   pesquisa_autor(livros)
                    
            elif resposta == 4: 
                remover_livro(livros)
            elif resposta == 5:
                break
        except ValueError as e:
            print(e)
                        
if __name__ == "__main__":
    main()               
