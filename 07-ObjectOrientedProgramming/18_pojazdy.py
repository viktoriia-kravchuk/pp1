class Vehicle():
    def __init__(self,brand,registration_nr):
        self.brand=brand
        self.registration_nr=registration_nr
        self.mileage=0
        self.rented=False
    def rent(self):
        self.rented=True
    def return_c(self):
        self.rented=False    
    def change_mileage(self,km):
        self.mileage+=km  
    def __str__(self):
        return f"Marka pojazdu: {self.brand}\nNumer rejestracyjny pojazdu: {self.registration_nr}\nPrzebieg: {self.mileage}\nJest wypożyczony: {self.rented}" 
class Car(Vehicle):
    def __init__(self,brand,registration_nr,seats):
        self.seats=seats
        super().__init__(brand,registration_nr)
    def __str__(self):
        return f"Marka pojazdu: {self.brand}\nNumer rejestracyjny pojazdu: {self.registration_nr}\nPrzebieg: {self.mileage}\nJest wypożyczony: {self.rented}\nLiczba miejsc: {self.seats}"                 
class Truck(Vehicle):
    def __init__(self,brand,registration_nr,capacity):
        self.capacity=capacity
        super().__init__(brand,registration_nr)
    def __str__(self):
         return f"Marka pojazdu: {self.brand}\nNumer rejestracyjny pojazdu: {self.registration_nr}\nPrzebieg: {self.mileage}\nJest wypożyczony: {self.rented}\nŁadowność w tonach: {self.capacity}"                 
class Rental():
    def __init__(self):
        self.name="Rental"
        self.cars=[]
    def add_vehicle(self,car):
        self.cars.append(car) 
    def list_car(self):
        print(f"Nazwa: {self.name}")
        i=1
        for car in self.cars:
            print(f"{i}.{car}")    
            i+=1
    def list_available_cars(self):
        i=1
        for car in self.cars:
            if car.rented==False:
               print(f"{i}.{car}")    
               i+=1  
    def list_rented_cars(self):
        i=1
        for car in self.cars:
            if car.rented:
               print(f"{i}.{car}")    
               i+=1  
    def rent_registration_nr(self,registration_nr):
        for car in self.cars:
            if car.registration_nr==registration_nr:
                if car.rented==False:
                    car.rent()   
                    break
    def return_registration_nr(self,registration_nr,km):
        for car in self.cars:
            if car.registration_nr==registration_nr:
                if car.rented:
                    car.return_c()   
                    car.change_mileage(km)
                    break
rental = Rental()
c1=Car("Mazda", "KM1267W",5)
c2=Car("BMW", "PL098T12",4)
c3=Car("KIA", "LK1234",5)
d1=Truck("Volkswagen","QW12345",5)
d2=Truck("DAF","QP12345",12)
rental.add_vehicle(c1)
rental.add_vehicle(c2)
rental.add_vehicle(c3)
rental.add_vehicle(d1)
rental.add_vehicle(d2)
rental.list_car()   
rental.list_available_cars()
c1.rent()
rental.return_registration_nr("KM1267W",950)
c2.rent()
rental.list_rented_cars()
rental.list_available_cars()
