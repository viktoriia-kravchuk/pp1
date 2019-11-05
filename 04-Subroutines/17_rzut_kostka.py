import random
def rzutKostka():
    x=random.randrange(1,7)
    return x
suma=0    
print("Wyrzucone oczka: ",end=" ")
for i in range(3):
    k=rzutKostka()
    print(k,end=" ")
    suma+=k
print(f"\nSuma oczek: {suma}",end=" ")    


