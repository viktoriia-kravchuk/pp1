class Message():
    def __init__(self):
        self.message = ''
    def set_message(self,message):
        self.message = message
        self.message=self.message.capitalize()
        self.message+=' BYE'
       