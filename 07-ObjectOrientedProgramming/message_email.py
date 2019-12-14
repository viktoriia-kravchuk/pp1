from message import Message
class Email(Message):
    def __init__(self,sender_adress,receiver_adress,topic,message):
        self.sender=sender_adress
        self.receiver=receiver_adress
        self.topic=topic
        super().set_message(message)
    def send(self):
        print(f"Wysyłanie emaila...\nOd:{self.sender}\nDo:{self.receiver}\nTemat:{self.topic}\nTreść:{self.message}")    

