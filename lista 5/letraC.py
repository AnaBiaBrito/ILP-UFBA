tamanhoplantacao = int(input())

plantacao = []

for i in range(tamanhoplantacao):
    pesoaboboras = input().split()
    pesoaboboras = list(map(int, pesoaboboras))
    plantacao.append(pesoaboboras)

