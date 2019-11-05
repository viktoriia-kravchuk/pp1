def jestImie(imie,imiona):
    print("Imiona: ",end="")
    for i in imiona:
        print (i, end=" ")
    print(f"\nImie: {imie}")    
    print("Rezultat: ",end="")    
    if imie in imiona:
        print("imię zawarte jest w wykazie imion")    
    else:
         print("imię nie jest zawarte w wykazie imion") 
tab=["Janek","Ania","Wojtek","Zosia"]              
jestImie("Wojtek",tab)   
