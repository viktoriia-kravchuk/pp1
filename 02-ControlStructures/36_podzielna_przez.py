i=7
while i>=7:
    if i%2==1 and i%3==1 and i%4==1 and i%5==1 and i%6==1:
        print (f"Najmniejsza liczba podzielna przez 7 która przy dzieleniu prze 2,3,4,5,6 daje resztę 1: {i}")
        break
    else:
        i+=7