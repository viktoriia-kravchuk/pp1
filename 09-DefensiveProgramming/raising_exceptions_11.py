wiek=250
if type(wiek)!= int:
    raise TypeError('Wiek powinien być liczbą całkowitą!')
if wiek>120 or wiek<0:
    raise ValueError('Wiek nie może być ujemny lub większy od 120!')
print(f'Masz {wiek} lat')