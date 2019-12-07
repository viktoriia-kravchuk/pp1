class plane():
    def __init__(self,number):
        self.number=number
        self.in_flight=False
        self.height=0
    def show_info(self):
        print(f"Tu {self.number}, moja wysokość lotu to {self.height}m")    
    def start(self, start_height):
        if start_height<1000 or start_height>2000:
            print("Nieprawidłowa wysokość startu")
        else:
            self.height+=start_height
            self.in_flight=True
    def change_height(self,height):
        if self.in_flight:
            if height in range(300,11001):
                self.height=height
            elif height<300:
                print("Zbyt niska wysokość lotu")  
            else:
                print("Zbyt duża wysokość lotu")     
    def landing(self):
        if self.height>=500:
            print("Zmniejsz wysokość lotu dla lądowania") 
            return False
        else:
            self.height=0
            self.in_flight=False
            print("Ladowanie powiodło się")   
samolot=plane("LOT881")    
samolot.start(1500) 
samolot.show_info()   
samolot.change_height(8900)                     
samolot.show_info()
samolot.change_height(200)
samolot.show_info()
samolot.landing()
samolot.show_info()