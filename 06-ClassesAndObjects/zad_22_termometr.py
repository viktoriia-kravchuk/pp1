import random
class Termometr():
    def __init__(self):
        self.temperature=34.0
        self.is_on=False
    def turn_on(self):
        self.is_on=True
    def turn_off(self):
        self.is_on=False        
    def measure(self):
        self.temperature=round(random.uniform(34.0,42.1),1)
    def show_temperature(self):
        if self.temperature>=37.0:
            print(f"Zmierzona temperatura {self.temperature}C (gorączka)")    
        else:
            print(f"Zmierzona temperatura {self.temperature}C")    
        if self.temperature>=41.0:
            print("Stan zagrożenia życia!!!")    
