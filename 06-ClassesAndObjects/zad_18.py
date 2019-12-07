from zad_18_kostka import dice
suma=0    
kostka1=kostka2=kostka3=dice()    
for i in range (3):
    tab=[kostka1.return_value(),kostka2.return_value(),kostka3.return_value()]
    print("Wyrzucone oczka: ",end="")
    for i in tab:
        print (i,end=" ")
        suma+=i
    print("\nSuma:",suma)
print(f"Suma wyrzuconych oczek wynosi : {suma}")     