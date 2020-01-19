class Pracownik:
    def __init__(self, osoba, staz_pracy, wynagrodzenie):
        self.osoba = osoba
        assert type(osoba)==str, "Imie i nazwisko osoby musi być napisem"
        self.staz_pracy = staz_pracy
        assert type(staz_pracy)==int or type(staz_pracy)==float, "Staż pracy nie jest liczbą" 
        assert staz_pracy>=0,"Staż pracy nie może być mniejszy od 0"
        self.wynagrodzenie = wynagrodzenie
        assert type(wynagrodzenie)==int or type(wynagrodzenie)==float, "Wynagrodzenie nie jest liczbą" 
        assert wynagrodzenie>=0,"Wynagrodzenie nie może być mniejsze od 0"
    def oblicz_dodatek(self):
        if self.staz_pracy>5:
            procent=self.staz_pracy-5
            if procent>20:
                procent=20
            nadwyzka=round(self.wynagrodzenie*(procent*0.01),2)
            return nadwyzka
        else:
            return 0
    def __str__(self):
        return f"Pracownik: {self.osoba}\nStaż pracy: {self.staz_pracy}\nDodatek stażowy: {self.oblicz_dodatek()} zł\nŁączne wynagrodzenie: {round(self.wynagrodzenie+self.oblicz_dodatek(),2)} zł"   
pracownik=Pracownik("Jan Kowalski",10,1000)                  
print(pracownik)