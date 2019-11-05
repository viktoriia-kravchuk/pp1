def wystepuje(liczba,tablica):
    print(f"Liczba: {liczba}",end=" ")
    print("\nTablica:", end=" ")
    for i in tablica:
        print(i, end=" ")
    if liczba in tablica:
        print("\nRezultat: Podana liczba występuje w tablicy")    
    else:
        print("\nRezultat: Podana liczba nie występuje w tablicy")      
    
tab=[15,38,7,23,14]
l=23
wystepuje(l,tab)
