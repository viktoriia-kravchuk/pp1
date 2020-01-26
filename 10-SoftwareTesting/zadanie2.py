class Miasto():
    def __init__(self,nazwa,populacja):
        self.nazwa=nazwa
        self.populacja=populacja
    def __str__(self):
        return f"{self.nazwa},{self.populacja}"   
 