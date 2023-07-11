pista, pessoas, alunos = input().split()

pista = int(pista)
pessoas = int(pessoas)
alunos = int(alunos)

v = pessoas * pista

if alunos + 1 <= v:
    print("S")
else:
    print("N")