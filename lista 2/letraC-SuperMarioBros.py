starc, megam, koopa = map(int, input().split())

starctotal = 30 - starc
megamtotal = 6 - megam
koopatotal = 3 - koopa

if starc < 30:
    print (starctotal, megamtotal, koopatotal)
    
if starc == 30:
    print ("PROXIMO MUNDO")