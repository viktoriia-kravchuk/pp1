dni_tygodnia=['Poniedziałek',"Wtorek","Środa","Czwartek","Piątek","Sobota","Niedziela"]
dzien=input("Podaj numer dnia tygodnia ")
try:
    dzien=int(dzien)
except ValueError:
    print("Niepoprawne dane")  
    exit()
assert dzien in range(1,8), "Podaj liczbę z zakresu od 1 do 7"
print(dni_tygodnia[int(dzien)-1])                

