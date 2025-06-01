#base = float(input('Digite a sua base para continuar...'))
#altura = float(input('Digite a sua altura para continuar...'))
#area = (base * altura)/2
#print(area)

# Aula - 02 - Exercícios
# Exercício 1
#numeros =[1,2,3,4,5,6,7,8,9,10]
#numeros.reverse()
#for r in numeros:
#  print("Digite o Número",r,r)

#numeros = []
#for i in range(11):
 #   n = input(f'Digite o {i + 1}º valor: ')
 #   numeros.append(n)

#for j in range(9, -1, -1):
 #   print(f't: {j}')


 # Aula - 03 - Exercícios
 # # Exercício 2 
#numero = int(input('Digite um número: '))

#while numero < 1:
 #   int(input('Digite um número positivo'))
#for i in range(1, 11):
 #   resultado = numero * i
  #  print(f'{numero} x {i} = {resultado}')

# Aula - 04 - Exercícios
# Exercício 3
# #Tendo um CPF dentro de uma string no formato '12345678900', 
# desenvolva um programa que imprima o CPF no formato '123.456.789-00'.

cpf = '12345678900'
cpf_formatado = f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'
print(cpf_formatado)