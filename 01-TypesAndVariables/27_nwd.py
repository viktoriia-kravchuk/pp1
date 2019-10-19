#Największy wspólny podzielnik
#wczytujemy liczby z klawiatury
a=int(input("Podaj pierwszą liczbę: "))
b=int(input("Podaj drugą liczbę: "))
#obliczanie nwd
import math
c=math.gcd(a,b)
#wysietlanie nwd
print ("Największy wspólny podzielnik dwóch liczb : {} i {} , wynosi {}". format(a,b,c))