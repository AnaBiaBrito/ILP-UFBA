sapos, pedras = map(int, input().split())

for i in range(sapos):
    pulo = [int(input())]

pedras = [0] * pedras

for sapo in range(sapos):
    posicao = 0
    while posicao < pedras:
        pedras[posicao] = 1
        posicao = posicao + sapo

print(*pedras)