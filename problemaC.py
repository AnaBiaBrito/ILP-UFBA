pessoas = int(input())

identificador = list(map(int, input().split()))

repetidos = [x for x in identificador if identificador.count(x) > 1]

if len(repetidos) > 0:
    print (repetidos[0])

else:
    print("-1")