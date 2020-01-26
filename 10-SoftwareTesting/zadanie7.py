class Stos():
    def __init__(self):
        self.stos=[]
        self.karty=['as','krol','dama','walet','10','9','8','7','6','5','4','3','2']
    def wstaw(self,nazwa):
        if nazwa in self.karty:
            self.stos.append(nazwa)
            return self.stos
    def zdejmij(self):
        if self.jest_pusty():
            return None
        else:
            return self.stos.pop()    
    def jest_pusty(self):
        return len(self.stos)==0        