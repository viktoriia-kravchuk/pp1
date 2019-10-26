a=int(input("Podaj pierwszą liczbę: "))
b=int(input("Podaj drugą liczbę: "))
c=int(input("Podaj trzecią liczbę: "))
mediana=0
if (b<c and b>a) or (b<a and b>c):
    mediana=b    
elif (c>a and c<b) or (c<a and c>b):
    mediana=c
elif (a>c and c<b) or (a<c and c>b):
    mediana=a
print (f"Mediana wynosi {mediana}")    
    