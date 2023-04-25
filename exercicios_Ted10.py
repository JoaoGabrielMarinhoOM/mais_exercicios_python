# exercicio1
vetor = []

for i in range(20):
    numero = int(input(f"Digite o {i+1}º número: "))
    vetor.append(numero)

print("Números em ordem inversa:")
for numero in reversed(vetor):
    print(numero)

# exercicio2
vetor = []

for i in range(10):
    numero = int(input(f"Digite o {i+1}º número: "))
    vetor.append(numero)

repetidos = set()
posicoes = {}
for i, numero in enumerate(vetor):
    if numero in posicoes:
        posicoes[numero].append(i)
        repetidos.add(numero)
    else:
        posicoes[numero] = [i]

if repetidos:
    print("Números repetidos encontrados:")
    for numero in repetidos:
        print(f"O número {numero} está nas posições {posicoes[numero]}")
else:
    print("Não há números repetidos no vetor.")
