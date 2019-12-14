class Student():
    university="UEK Kraków"
    album_nr=100000
    def __init__(self,name,surname,field_of_study):
        self.name=name
        self.surname=surname.upper()
        self.field=field_of_study
        Student.album_nr+=1
        self.album_nr=Student.album_nr
    def __str__(self):
        return(f"{self.name} {self.surname} ({self.album_nr}), {self.field}, {Student.university}")
student1=Student("Wacław","Potocki","Informatyka stosowana")  
student2=Student("Jan","Kowalski","Informatyka stosowana") 
student3=Student("Tadeusz","Potocki","Informatyka stosowana")   
print(student1) 
print(student2) 
print(student3)    

