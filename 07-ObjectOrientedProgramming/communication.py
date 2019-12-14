from message import Message
from message_sms import SMS
from message_email import Email
message=SMS("789456123","123456789","Informuję, że nasze czwartkowe spotkanie zostało odwołane")
message.send()
email=Email("nowak@onet.pl","kowalski@gmail.com","Spotkanie w czwartek","Informuję, że nasze czwartkowe spotkanie zostało odwołane")
email.send()