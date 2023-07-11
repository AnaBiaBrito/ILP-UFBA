S, N = map(int, input().split())
pulos = [int(input()) for _ in range(S)]

pedras = [0] * N 

for sapo in range(S):
    posicao = 0
    while posicao < N:
        pedras[posicao] = 1 
        posicao += pulos[sapo]

print(*pedras)