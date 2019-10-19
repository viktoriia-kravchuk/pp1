#Obliczanie pola powierzchni i obwodu koła o zadanym promieniu
promien=5
import math
pi=math.pi
pole_kola=pi*(promien**2)
obwod_kola=2*pi*promien
print("Pole koła o promieniu {} wynosi {}. \nObwód koła o promieniu {} wynosi {}". format(promien,pole_kola,promien,obwod_kola))