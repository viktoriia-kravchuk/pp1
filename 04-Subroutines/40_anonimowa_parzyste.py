x=lambda a: a%2==0 #funkcja aninimowa zwracająca prawdę gdy liczba jest parzysta
tab=[1,2,3,4,5,6,7,8]
parzyste=filter(x,tab) #funkcja filter która wykorzystuje funkcje anonimową i filtruje tablicę 
print("Liczby parzyste z tablicy to: ") #rezultat
for i in parzyste:
    print(i,end=" ")