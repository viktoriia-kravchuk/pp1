import math

def czytajWspolczynniki():
    tab=[]
    for i in range(3):
        x=float(input(f"Podaj {i+1} współczynnik: "))
        tab.append(x)
    return tab

def obliczDelte(tab):
    delta=float((tab[1]**2)-(4*tab[0]*tab[2]))
    return delta

def obliczPierwiastki(tab):
    pierwiastki=[]
    if obliczDelte(tab)==0:
        x12=float((-tab[1])/2*tab[0]) 
        pierwiastki.append(x12) 
    elif obliczDelte(tab)>0:
        x1=float(((-tab[1])-math.sqrt(obliczDelte(tab)))/2*tab[0]) 
        x2=float(((-tab[1])+math.sqrt(obliczDelte(tab)))/2*tab[0])   
        pierwiastki.append(x1)
        pierwiastki.append(x2)
    return pierwiastki 

def wyswietlPierwiastki(tab):
    pierwiastki=obliczPierwiastki(tab)
    if(len(pierwiastki)==2):
        print(f"Pierwiastki równania : x1={pierwiastki[0]} x2={pierwiastki[1]}")
    elif len(pierwiastki)==1:
        print(f"Pierwiastek równania : x1={pierwiastki[0]}")
    else:
        print("Równanie nie ma pierwiastków")     

          
