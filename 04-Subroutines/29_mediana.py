import math
import re
def mediana(tab):
    tab.sort() #sortujemy tablice 
    l=len(tab) #wyznaczany jej dlugosc a nastepnie obliczamy srodkowy indeks tablicy
    srednia=int((l/2)-1)
    if l%2==0:
        mediana=(tab[srednia]+tab[srednia+1])/2 #w zależnosci od tego czy jest parzysta ilosc liczb czy nie, obliczamy wartosc mediany
    else:
        mediana=tab[math.ceil(srednia)]   
    return mediana #zwracamy mediane
def dominanta(tab):
    s=""
    for j in tab:
        s+=str(j)
    max=0
    for i in range(len(s)):
        x=len(re.findall(str(i),s))
        if x>max:
            max=x
            dominanta=i
    return dominanta    
tablica=[2, 3, 5, 2, 9, 8, 1, 3, 9, 1, 1, 4, 7, 7, 1, 4]        
print(f"Mediana wynosi: {mediana(tablica)}")
print(f"Dominanta wynosi: {dominanta(tablica)}")