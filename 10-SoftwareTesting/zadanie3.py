
class Prostokat():
    def __init__(self,a,b):
        self.x=a
        self.y=b
    def __add__(self,other):
        pole1=self.x*self.y
        pole2=other.x*other.y
        return pole1+pole2
