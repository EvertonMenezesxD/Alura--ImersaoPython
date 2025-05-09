menu_principal = """
[Menu Principal] Escolha uma das seguintes opções:
1 - Categorias
2 - Editoras
3 - Autores
4 - Livros
0 - Sair do programa
"""

menu_categoria = """
[Categorias] Escolha uma das seguintes opções:
1 - Listar toda as categorias
2 - Adicionar nova categoria
3 - Excluir categoria
4 - Ver categoria por Id
0 - Voltar ao menu anterior
"""

menu_editora = """
[Editoras] Escolha uma das seguintes opções:
1 - Listar todas as editoras
2 - Adicionar nova editora
3 - Excluir editora
4 - Ver editora por Id
0 - Voltar ao menu anterior
"""

menu_autor = """
[Autores] Escolha uma das seguintes opções:
1 - Listar todos os autores
2 - Adicionar novo autor
3 - Excluir autor
4 - Ver autor por Id
5 - Editar autor
0 - Voltar ao menu anterior
"""

menu_livro = """
[Livros] Escolha uma das seguintes opções:
1 - Listar todos os livros
2 - Adicionar novo livro
3 - Excluir livro
4 - Ver livro por Id
0 - Voltar ao menu anterior
"""
# Inicializando a tabela de autores
tabela_autores = []
# Inicializando a tabela de editoras
tabela_editoras = []
# Inicializando a tabela de categorias
tabela_categorias = []
# Inicializando a tabela de livros
tabela_livros = []
while True:
    print(menu_principal)
    op = input('Digite a opção: ')

    if op == '0':
        break
    elif op == '1':
        print(menu_categoria)
        input('\nDigite <ENTER> para continuar...\n')
    elif op == '2': # else if
        print(menu_editora)
        input('\nDigite <ENTER> para continuar...\n')
    elif op == '3':
        while True:
            print(menu_autor)
            opcao_autor = input('Digite a opção: ')
            if opcao_autor == '0':
                break
            elif opcao_autor == '1':
                if tabela_autores == []:
                    print('Nenhum autor cadastrado!')
                    input('\nDigite <ENTER> para continuar...\n')
                print('ID |Nome | E-mail | Telefone | Biografia')
                for index, autor in enumerate(tabela_autores):
                    print(f'{index + 1} | {autor[0]} | {autor[1]} | {autor[2]} | {autor[3]}')
            elif opcao_autor == '2':
                nome_autor = input('Digite o nome do autor: ')
                telefone_autor = input('Digite o telefone do autor: ')
                bio_autor = input('Digite a biografia do autor: ')
                email_autor = input('Digite o e-mail do autor: ')
                novo_autor = {
                    'nome': nome_autor,
                    'email': email_autor,
                    'telefone': telefone_autor,
                    'biografia': bio_autor
                }
            elif opcao_autor == '3':
                if tabela_autores == []:
                    print('Nenhum autor cadastrado!')
                    input('\nDigite <ENTER> para continuar...\n')
                else:
                    id_autor = int(input('Digite o ID do autor a ser excluído: '))
                    tabela_autores.pop(id_autor - 1)
                    print(f'Autor com ID {id_autor} excluído com sucesso!')
                    input('\nDigite <ENTER> para continuar...\n')
            elif opcao_autor == '4':
                if tabela_autores == []:
                    print('Nenhum autor cadastrado!')
                    input('\nDigite <ENTER> para continuar...\n')
                else:
                    id_autor = int(input('Digite o ID do autor a ser exibido: '))
                    if id_autor > len(tabela_autores):
                        print('ID inválido!')
                    else:
                        print('ID |Nome | E-mail | Telefone | Biografia')
                        print(f'{tabela_autores[id_autor][0]} | {tabela_autores[id_autor - 1][1]} | {tabela_autores[id_autor - 1][2]} | {tabela_autores[id_autor - 1][3]}')
                        input('\nDigite <ENTER> para continuar...\n')
            elif opcao_autor == '5':
                if tabela_autores == []:
                    print('Nenhum autor cadastrado!')
                    input('\nDigite <ENTER> para continuar...\n')
                else:
                    id_autor = int(input('Digite o ID do autor a ser editado: '))
                    if id_autor > len(tabela_autores):
                        print('ID inválido!')
                    else:
                        nome_autor = input('Digite o novo nome do autor: ')
                        telefone_autor = input('Digite o novo telefone do autor: ')
                        bio_autor = input('Digite a nova biografia do autor: ')
                        email_autor = input('Digite o novo e-mail do autor: ')
                        tabela_autores[id_autor - 1][0] = nome_autor
                        tabela_autores[id_autor - 1][1] = email_autor
                        tabela_autores[id_autor - 1][2] = telefone_autor
                        tabela_autores[id_autor - 1][3] = bio_autor
                        print(f'Autor com ID {id_autor} editado com sucesso!')
                        input('\nDigite <ENTER> para continuar...\n')
            else:
                print('Opção inválida!')
    elif op == '4':
        print(menu_livro)
        input('\nDigite <ENTER> para continuar...\n')
    else:
        print('Opção inválida!')

print('Programa encerrado!')  

