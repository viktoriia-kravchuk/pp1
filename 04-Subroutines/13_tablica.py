def suma(tab):
    suma=0
    print("Tablica:", end=" ")
    for i in tab:
        print(i, end=" ")
        suma+=int(i)
    return suma
tablica=[4,3,7,1,3]
print(f"\nSuma wartości: {suma(tablica)}")
        