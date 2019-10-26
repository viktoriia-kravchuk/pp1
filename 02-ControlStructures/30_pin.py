pin='0805'
i=0
while i<3:
    i+=1
    pin_podany=input("Podaj kod PIN: ")
    if pin_podany==pin:
        print("Poprawny kod PIN")
        break
    elif i!=3:
        print("Kod PIN niepoprawny")
    else:
        print("Karta patnicza zostaje zablokowana")