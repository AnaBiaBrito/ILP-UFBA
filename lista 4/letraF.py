N = int(input()) 
amigos = []
for _ in range(N):
    nome, peso = input().split()
    peso = int(peso)
    amigos.append((nome, peso))

C = int(input())

peso_total = sum(peso for _, peso in amigos)

if peso_total <= C:
    print("Vamos todos encontrar a montanha!")
else:
    print("Vamos virar almoço de aranhas gigantes!")