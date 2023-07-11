jogadores = int(input())
assassinatos = list(map(int, input().split()))

maxassassinatos = max(assassinatos)

contagem = [0] * (maxassassinatos + 1)

for ass in assassinatos:
    contagem[ass] += 1

for i in range(len(contagem)):
    for _ in range(contagem[i]):
        print(i, end=' ')