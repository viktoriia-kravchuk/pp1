a=int(input("Podaj a: "))
b=int(input("Podaj b: "))
c=int(input("Podaj c: "))
delta=(b**2)-(4*a*c)
if delta>0:
    import math
    pierwiastek_delta=math.sqrt(delta)
    x1=(-b-pierwiastek_delta)/(2*a)
    x2=(-b+pierwiastek_delta)/(2*a)
    print(f"Pierwiastki równania to x1={x1}, x2={x2}")
elif delta==0:
    x1=-b/(2*a)
    print(f"Pierwiastek równania to x1={x1}")
else:
    print("Brak pierwiastków ")