tablica=[15,8,31,47,2,19]
suma=0
l=0
for i in tablica:
    if i%2!=0:
        suma+=i
        l+=1
srednia=suma/l
print(f"Średnia arytmetyczna wszystkich liczb nieparzystych wynosi: {srednia}")