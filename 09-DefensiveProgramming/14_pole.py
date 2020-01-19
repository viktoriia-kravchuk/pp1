class Zero(Exception):
    pass
def pole_prostokata(a,b):
    try:
        if a<=0 or b<=0:
            raise Zero
        else:
            return a*b
    except Zero:
        print("Jeden lub dwa boki są mniejsze bądź równe 0")
        exit()
try:
    x=float(input('Podaj pierwszy bok: '))
    y=float(input('Podaj drugi bok: '))
    print(pole_prostokata(x,y))
except ValueError:
    print('Podane wartości muszą być liczbami')
    exit()
