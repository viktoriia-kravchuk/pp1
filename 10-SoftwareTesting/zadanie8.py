class Sala():
    def __init__(self,nazwa,liczba_miejsc):
        self.nazwa=nazwa
        self.liczba_miejsc=liczba_miejsc
class Sale():
    def __init__(self):
        self.sale=[]
    def dodaj(self,sala):
        self.sale.append(sala) 
    def liczba_sal(self):
        return len(self.sale)
    def razem_miejsc(self):
        suma=0
        for sala in self.sale:
            suma+=sala.liczba_miejsc
        return suma
    def liczba_miejsc(self,nazwa):
        for sala in self.sale:
            if nazwa==sala.nazwa:
                return sala.liczba_miejsc
        if nazwa not in self.sale:
            return 0
    def liczba_sal_przedzial(self,od,do):
        ile=0
        for sala in self.sale:
            if od<=sala.liczba_miejsc<=do:
                ile+=1
        return ile



            

