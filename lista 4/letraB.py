def resultado(N, frentes):
    for i in range(ninjas - 1, -1, -1):
        print(f'{i + 1}: {frentes[i]}')

ninjas = int(input())
frentes = list(map(int, input().split()))

resultado(ninjas, frentes)
