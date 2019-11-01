tab=[]
with open("numbers.txt","r") as file:
    for liczba in file:
        tab.append(int(liczba))
file.close()
tab.sort()
for i in tab:
    print(i,end=" ")

        
    