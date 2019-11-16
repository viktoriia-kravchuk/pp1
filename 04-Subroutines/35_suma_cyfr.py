def sumaCyfr(a):
    if(a>0):
        return a%10 + int(sumaCyfr(a/10))
    return 0
liczba=int(input("Podaj liczbę:"))   
print(f"Suma cyfr liczby wynosi: {sumaCyfr(liczba)}") 
