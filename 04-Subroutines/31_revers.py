import math
def reverse(tab):
    l=len(tab)
    s=int(math.sqrt(l))+1 #odwracamy do srodka(czyli pierwiastka)
    for i in range(s):
        x=tab[i]
        tab[i]=tab[l-i-1]
        tab[l-i-1]=x
    return tab        
tablica=[2, 5, 4, 1, 8, 7, 4, 0, 9]
print(f"Tablica :{tablica}")
print(f"Odwrócona tablica: {reverse(tablica)}")