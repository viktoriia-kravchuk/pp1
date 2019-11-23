import math
x=3.7
y=4
sqrtX=math.sqrt(x)
powXY=math.pow(x,y)
sqrtXY=math.pow(x,1/y)
pole_kola_y=math.pi*(y**2)
silnia_y=math.factorial(y)
najwieksza_x=math.floor(x)
print(f"1. Pierwiastek kwadratowy z {x} wynosi {sqrtX}")
print(f"2. {x} do potęgi {y} wynosi {powXY}")
print(f"3. Pierwistek z {x}  {y} stopnia wynosi {sqrtXY}")
print(f"4. Pole koła o promieniu {y} wynosi {pole_kola_y}")
print(f"5. Silnia z {y} wynosi {silnia_y}")
print(f"6. Największa możliwa liczba całkowita mniejsza lub równa {x} wynosi {najwieksza_x}")