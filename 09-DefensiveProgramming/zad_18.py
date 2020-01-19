name=input("Podaj imię ")
assert len(name)>=3 , "Imię ma mniej niż 3 znaki"
surname=input("Podaj nazwisko ")
assert len(surname)>=3, "Nazwisko ma mniej niż 3 znaki"
print(f"{name}, {surname.upper()}")
