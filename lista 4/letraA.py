caixas = int(input())

esmeraldas = map(int, input().split())

esmeraldascaos = int(input())

if esmeraldascaos in esmeraldas:
    print(esmeraldascaos)
else:
    print("-1")