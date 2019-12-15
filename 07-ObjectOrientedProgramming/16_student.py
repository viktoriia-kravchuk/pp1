class Student():
    def __init__(self,name,surname,album_nr):
        self.name=name
        self.surname=surname
        self.nr=album_nr
    def __str__(self):
        return f"{self.name} {self.surname} {self.nr}"
    def __eq__(self,other):
        return self.nr==other.nr
    def __lt__(self,other):
        return self.nr<=other.nr
studenci=[Student("Anna","Tomaszewska",141820),Student("Wojciech","Zbych",201003),Student("Maja","Kowalska",153202),Student("Marek","Migiel",138600)]
for s in studenci:
    print(s)       
studenci=sorted(studenci)
print()   
for s in studenci:
    print(s)  
       


