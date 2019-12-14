from message import Message 
class SMS(Message):
    def __init__(self,sender,receiver,message):
        self.sender=sender
        self.receiver=receiver
        super().set_message(message)
    def send(self):
        print(f"Wysyłanie SMS...\nOd:{self.sender}\nDo:{self.receiver}\nTreść:{self.message}")   
        

