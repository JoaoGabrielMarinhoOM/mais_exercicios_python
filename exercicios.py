# exercicio1
n1 = float(int(input("Digite um número: ")))

n2 = float(int(input("Digite outro número: ")))

if n1 > n2:
    print(f'{n1}')
else:
    print(f'{n2}')

# exercicio2
print("Para você entrar tem que ser maior de idade")

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

#exercicio3
print("para saber se você pode dirigir um carro, tenho q saber seu nome e sua idade")

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você pode dirigir, ja é maior de idade")
else:
    print("Nem sair da escola você saiu e ja quer dirigir? Vai estudar fedelho")

#exercicio4
print("Escreva as 4 notas do alunato a baixo:")

n1 = float(int(input("Digite a primeira nota: ")))
n2 = float(int(input("Digite a segunda nota: ")))
n3 = float(int(input("Digite a terceira nota: ")))
n4 = float(int(input("Digite a quarta nota: ")))

media = ((n1 + n2 + n3 + n4) / 2)



if media >= 7:
    print("Alunato aprovado!")
else:
    print("Alunato reprovado!")

#exercicio5
numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print(f'O número {numero} é par!')
else:
    print(f'O número {numero} é impar!')

#exercicio6
print("Escreva o salário do seu funcionário para aplicar o aumento")

salario = float(int(input("Digite o salário do funciorário: ")))

salario_aumento1 = salario + 150.00

salario_aumento2 = salario + 225.00

if salario > 1500.00:
    print(f'{salario_aumento1}')
else:
    print(f'{salario_aumento2}')

#exercicio7
numeros = []  # a lista está vazia pois ela será preenchida
qtd_numeros = int(input("Digite a quantidade de números que deseja informar: "))

for n in range(qtd_numeros):
    num = int(input("Digite um número: "))
    numeros.append(num)  # esse ".append" serve para adicionar no final um elemento que não estava no começo da lista.

maior = max(numeros)
menor = min(numeros)

print("O maior número é:", maior)
print("O menor número é:", menor)

#exercicio8
palavra = input("Digite uma palávra: ")

if palavra == palavra[::-1]:  # esse "[::-1]" significa que ele vai ler a string de forma inversa, de tras pra frente.
    print(f'A palávra {palavra} é um palíndromo!')
else:
    print(f'A palávra {palavra} não é um palíndromo.')

#exercicio9
numero = int(input("Digite um número: "))
print(f' Tabuada do {numero}: ')
for n in range(1, 11):
    resultado = numero * n
    print(f'{numero} x {n} = {resultado}')

#exercicio10
# pede ao usuário que digite uma lista de nomes separados por vírgulas
nomes = input("Digite uma lista de nomes separados por vírgulas: ")

# converte a string em uma lista de nomes
lista_nomes = nomes.split(",")  # "split" converte uma string em uma lista

# cria uma nova lista sem nomes duplicados
lista_sem_duplicatas = list(set(lista_nomes))  # o "set" e´para criar um conjunto de nomes sem duplicata

# exibe a lista final sem nomes duplicados
print("Lista sem nomes duplicados:", lista_sem_duplicatas)
