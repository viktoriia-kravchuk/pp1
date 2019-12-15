from math import pi
class Area():
    @staticmethod
    def circle(r):
        print(f"Pole koła o promieniu {r} wynosi {round(pi*(r**2),2)}")
    @staticmethod    
    def triangle(a,h):
        print(f"Pole trójkąta o podstawie {a} i wysokości {h} wynosi {0.5*a*h}")
    @staticmethod    
    def rectangle(a,b):
        print(f"Pole prostokąta o bokach {a} i {b} wynosi {a*b}")
Area.circle(3)
Area.triangle(6,2)     
Area.rectangle(4,7)   
   