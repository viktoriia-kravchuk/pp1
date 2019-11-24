import QuadraticEquation as rownanie
tab=rownanie.czytajWspolczynniki()
print(f"Równanie kwadratowe postaci : {int(tab[0])}x2+{int(tab[1])}x+{int(tab[2])}=0")
rownanie.wyswietlPierwiastki(tab)
