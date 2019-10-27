a=int(input("Podaj pierwszą liczbę :"))
b=int(input("Podaj drugą liczbę :"))
c=int(input("Podaj trzecią liczbę :"))
if a<=b and a<=c:
    min=a
    if b<c:
        sr=b
        max=c
    else:
        sr=c
        max=b
elif b<=a and b<=c:
    min=b
    if a<c:
        sr=a
        max=c
    else:
        sr=c
        max=a
else:
    min=c
    if a<b:
        sr=a
        max=b
    else:
        sr=b
        max=a
print(f"Liczby w kolejności rosnącej: {min},{sr},{max}")        