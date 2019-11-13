def zakres(n,x,y):
    if n>=x and n<=y:
        return True
    elif n>=y and n<=x:
        return True
    else:
        return False 
a=int(input("Podaj liczbę: "))
b=int(input("Podaj granicę zakresu: ")) 
c=int(input("Podaj granicę zakresu: "))
print(zakres(a,b,c))               