try:
    pesel=input("Wprowadź numer PESEL składający się z 11 cyfr")
    int(pesel)
    assert len(pesel)==11, "Podany numer PESEL nie ma 11 cyfr"
    print(pesel)
except ValueError:
    print("Podany numer PESEL zawiera inne niż cyfry znaki")    