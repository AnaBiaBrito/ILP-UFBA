missoes, xp = map(int, input().split())
xpiyoda, xpiluke, xpiahsoka = map(int, input().split())

xptotalyoda = missoes * xp + xpiyoda 
xptotaluke = missoes * xp + xpiluke
xptotalahsoka = missoes * xp + xpiahsoka

xptotalyoda = str(xptotalyoda)
xptotaluke = str(xptotaluke)
xptotalahsoka = str(xptotalahsoka)

print("Yoda " + xptotalyoda)
print("Luke " + xptotaluke)
print("Ahsoka " + xptotalahsoka)
