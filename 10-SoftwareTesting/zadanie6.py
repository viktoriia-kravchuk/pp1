from random import randint
class Macierz():
    def __init__(self,m,n):
        self.x=m
        self.y=n
        self.macierz=[[randint(0,9) for _ in range(self.x)] for _ in range(self.y)] 
    def show_m(self):
        for i in range(len(self.macierz)):
            print(self.macierz[i]) 
        print()       
    def __add__(self,other):
        if self.x==len(other.macierz) and self.y==len(other.macierz[0]):
            macierz_add=Macierz(self.x,self.y)
            for i in range(self.x):
                for j in range(self.y):
                    macierz_add.macierz[i][j]=self.macierz[i][j]+other.macierz[i][j]          
        else:
            macierz_add=[[0 for _ in range(self.x)] for _ in range(self.y)]
            print("Macierzy są róznych rozmiarów") 
            for i in macierz_add:
                print (i)       
        return macierz_add      
                   