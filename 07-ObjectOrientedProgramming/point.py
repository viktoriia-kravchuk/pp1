from math import sqrt
class Point():
    def __init__(self, x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'P({self.x},{self.y})'
    def __eq__(self,other):
        if self.x==other.x and self.y==other.y:
            return "Odległość między punktami wynosi 0"
        else:
            return f"Odległość między punktami wynosi {sqrt((other.x-self.x)**2+(other.y-self.y)**2)}"


