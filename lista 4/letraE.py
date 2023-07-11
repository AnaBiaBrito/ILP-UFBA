fases = int(input())

fasetipo = input().split()

fasetipo = list(map(int, fasetipo))

vida = int(input())


for i in fasetipo:
    if 0 == fasetipo:
        continue
    elif 1 == fasetipo:
        vida = 100
    else:
        vida = vida-i

    if vida <= 0:
        print("You Died")
        break
        
        
if vida > 0:
    print("Yes, you can")