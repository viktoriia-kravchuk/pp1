import math
import statistics
class Statystyka():
    def __init__(self,zbior_liczb):
        self.set=[]
        self.set+=zbior_liczb
    def add(self):
        number=input("Podaj liczbę: ")
        if '.' in number:
            number=float(number)
        else:
            number=int(number)    
        self.set.append(number)
    def display_set(self):
        for i in self.set:
            print(i,end=" ")    
    def get_max(self):
        return(max(self.set))        
    def get_min(self):
        return(min(self.set))    
    def get_average(self):
        return statistics.mean(self.set)
    def get_median(self):
        return statistics.median(self.set)
    def display_all(self):
        print(f"Największa liczba: {self.get_max()}\nNajmniejsza liczba: {self.get_min()}\n"
              f"Średnia arytmetyczna: {self.get_average()}\nMediana: {self.get_median()}")
zbior=Statystyka([12,37,6,9,17]) 
zbior.display_all()           




