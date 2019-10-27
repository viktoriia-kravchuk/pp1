a=int(input("Podaj lizbę: "))
binarny_n=""
binarny_odwrocony=""
import math
while a!=0:
    if a%2==0:
        binarny_n+='0'
    else:
        binarny_n+='1'
    a=math.floor(a/2)
l=len(binarny_n)-1
for i in range(l,-1,-1):
    binarny_odwrocony+=binarny_n[i]
print(binarny_odwrocony)