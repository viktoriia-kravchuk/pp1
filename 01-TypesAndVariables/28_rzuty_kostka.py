#Losowe rzuty kostką
#Losujemy 3 razy liczbę od 1 do 6
import random
a=random.randrange(1,7)
b=random.randrange(1,7)
c=random.randrange(1,7)
#Obliczamy sumę wylosowanych liczb
s=a+b+c
#Wyświetlamy sumę i rezultaty losowania
print("Pierwszy rzut: {}, drugi rzut: {}, trzeci rzut: {}. Ich suma wynosi: {}". format(a,b,c,s))