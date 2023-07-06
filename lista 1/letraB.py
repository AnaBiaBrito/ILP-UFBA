peso, velocidade = input().split()

peso = int(peso)
velocidade = int(velocidade)

energia = int(peso * (velocidade ** 2))

print(energia)