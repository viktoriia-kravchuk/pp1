try:
    netto=10
    if netto<=0:
        raise ValueError("Cena netto powinna być liczbą dodatnią większa od 0")
    else:
        brutto=round(float(netto)*1.23,2)
        print("Cena brutto wynosi: {:.2f} zł".format(brutto))
except TypeError:
    print("Cena netto musi być liczbą")
except ValueError:
    print("Cena netto powinna być liczbą dodatnią większa od 0")    

