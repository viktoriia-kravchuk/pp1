limit=int(input("Podaj limit prędkości(km/h): "))
predkosc=int(input("Podaj prędkość pojazdu(km/h): "))
p=predkosc-limit
if p>10:
    mandat=(p-10)*15+(10*5)
else:
    mandat=p*5
print(f"Mandat(zł): {mandat}")    