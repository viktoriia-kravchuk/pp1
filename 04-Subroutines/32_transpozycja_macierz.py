def transpozycja(macierz):
    print("Macierz po transpozycji:")
    n=len(macierz)
    m=len(macierz[0])
    for i in range(n):
        for j in range(m):
            print(f"{macierz[j][i]}",end=" ")
        print()
tab=[[1,2,0],[0,0,3],[5,1,1]]   
l=len(tab)
print("Macierz przed transpozycją: ")
for i in range(l):
    l1=len(tab[i])
    for j in range(l1):
        print(tab[i][j],end=" ") 
    print()    
transpozycja(tab)