segundos = int(input())

horas = segundos // 3600
segundos %= 3600
minutos = segundos // 60
segundos %= 60

print("{:01d}h {:01d}m {:01d}s".format(horas, minutos, segundos))
