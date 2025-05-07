nome = input('[Menu Principal] Escolha uma das Opções')
print('1 - Categorias')
print('2 - Editoras')
print('3 - Autores')
print('4 - Livros')
print('0 - Sair do programa')

op = 1

while True:
    op = input('Digite a opção: ')

    if op == '0':
        break
    if op == '1':
        print('Opção escolhida: Categorias')
        input('Digite <ENTER> para continuar...')
    elif op == '2':
        print('Opção escolhida: Editoras')
        input('Digite <ENTER> para continuar...')
    elif op == '3':
        print('Opção escolhida: Autores')
        input('Digite <ENTER> para continuar...')
    elif op == '4':
        print('Opção escolhida: Livros')
        input('Digite <ENTER> para continuar...')
    else:
        print('Opção inválida!')

print('Programa encerrado!')    

