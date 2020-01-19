from random import randint
def rzutKostka():
    x=randint(1,7)
    assert x in range(1,7), "Błąd"
    return x
print("Wyrzucone oczka :",rzutKostka())