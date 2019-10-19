#Zmierzanie się z komputerem
#Komputer rzuca kostkę
import random
rzut_komputera=random.randrange(1,7,1)
#Użytkownik próbuje odgadnąć
l_uzytkownik=int(input("Podaj ile oczek kostki wyrzucił komputer: "))
#Sprawdzenie liczby wpisanej przez użytkownika
if(l_uzytkownik>6 or l_uzytkownik<1):
    print("Podałeś błędną wartość. Wprowadź liczbę od 1 do 6")
#Rezultat True/False
else:
    print("Komputer wyrzucił: {} ". format(rzut_komputera))
    print("Zgadłeś:",rzut_komputera==l_uzytkownik)  