portas = int(input())

nivelpersonagem = 1

c = 0
d = 0

for i in range(portas):

    desafio, nivel = input().split()
    nivel = int(nivel)

    if desafio == "t":
        nivelpersonagem = nivelpersonagem + 1
    
    elif desafio == "m":
        
        a = "Combate iniciado"

        if nivelpersonagem >= nivel:
            
            nivelpersonagem = nivelpersonagem + 1
            b = "VITORIA"
            
        else:
            b = "Derrota! Fim da aventura"
            
    else:
        
        nivelpersonagem = nivelpersonagem - nivel

 
print(a)
print(b)

if nivelpersonagem == 5:
    print("Aventura concluida")
    
else:
    print("\n")
    