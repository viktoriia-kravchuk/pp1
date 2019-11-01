import re
komunikat="wtorek - 23C, środa - 21C, czwartek 25C "
cyfry=re.findall('\d{2}',komunikat)
suma=0
l=0
for i in cyfry:
    suma+=int(i)
    l+=1
srednia=int(suma/l)
print(f"Średnia prognozowana temperatura {srednia}C")