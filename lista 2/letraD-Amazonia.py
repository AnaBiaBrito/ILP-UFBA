destino1, destino2 = map(int, input().split())
loc1, loc2 = map(int, input().split())

if destino1 == loc1 and destino2 == loc2:
    print("Soltar pacote")
    
else:
    print("Nao soltar pacote")