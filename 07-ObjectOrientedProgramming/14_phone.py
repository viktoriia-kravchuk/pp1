class Phone():
    def __init__(self,brand,color,phone_number):
        self.brand=brand
        self.color=color
        self.number=phone_number
        self.on=False
        self.sended_messages=0
    def turn_on(self):
        self.on=True
    def turn_off(self):
        self.on=False
    def send_sms(self,other_number,sms):
        if self.on and len(other_number)>=9:
            print("Wiadomość została wysłana")
            self.sended_messages+=1
        else:
            print("Włącz telefon lub wprowadź poprawny numer telefonu")    
    def __str__(self):
        if self.on:
            kom="włączony"
        else:
            kom="wyłączony"    
        return (f"Telefon marki {self.brand} o numerze {self.number} jest {kom} , wysłano {self.sended_messages} SMS \n")         
tel1=Phone("Samsung","white","123456789")       
tel1.turn_on()
tel1.send_sms("789456123","Hi")
print(tel1) 
tel1.turn_off()
tel1=Phone("Apple","black","789456123")       
tel1.turn_on()
tel1.send_sms("78945","Hi")
print(tel1) 
tel1.turn_off()
            
