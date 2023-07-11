linhas, colunas = map(int, input().split())

pegos = []

for i in range(linhas):
    pegosnovos = input().split()
    pegosnovos = list(map(int, pegosnovos))
    pegos.append(pegosnovos)

pokemonash = int(input())

quantidade = 0

for linha in pegos:
    quantidade += linha.count(pokemonash)

print("Ash pegou", quantidade, "pokemon")