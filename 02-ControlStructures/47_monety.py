k=int(input("Podaj kwotę w zł: "))
monety=[5,2,1]
i=0
while (k>0):
    if (k>=monety[i]): 
        p=int(k/monety[i]) #ile razy wydac dany nominal
        k=k-(monety[i]*p) #zmniejszanie kwoty o wydany nominal
        print(f"{monety[i]} zl - {p} szt") #wypisz wynik 
    i+=1  #kolejny nominal
    
        
    