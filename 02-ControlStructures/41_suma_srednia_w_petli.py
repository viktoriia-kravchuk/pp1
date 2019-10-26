suma=0
l=0
a=1
while a!=0:
    a=int(input("Podaj liczbę: "))
    if a!=0:
        suma+=a
        l+=1
srednia=suma/l
print(f"REZULTAT: Liczb={l}, Suma={suma}, Średnia={srednia}")