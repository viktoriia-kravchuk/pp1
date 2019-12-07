import math
class fraction():
    def __init__(self,licznik,mianownik):
        self.counter=licznik
        self.denominator=mianownik
        if self.denominator==0:
            print("Nie można dzielić przez 0")
    def simplify(self):
        nwd=math.gcd(self.counter,self.denominator)  
        if nwd:
            self.counter=int(self.counter/nwd)
            self.denominator=int(self.denominator/nwd)
    def print(self):
        print(self.counter,'/',self.denominator)
ulamek=fraction(12,21) 
print("Ułamek pzed uproszczeniem")  
ulamek.print()
ulamek.simplify()
print("Ułamek po uproszczeniu")
ulamek.print()     
