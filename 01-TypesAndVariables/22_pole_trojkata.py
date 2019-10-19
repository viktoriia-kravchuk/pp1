#Pole trójkąta, wzór Herona
import math
a=int(input("Podaj pierwszy bok trójkąta:" ))
b=int(input("Podaj drugi bok trójkąta:" ))
c=int(input("Podaj trzeci bok trójkąta:" ))
p=0.5*(a+b+c)
pole=math.sqrt(p*(p-a)*(p-b)*(p-c))
print("Dla podanych boków trójkąta {},{},{}, pole wynosi: {}". format(a,b,c,pole))

