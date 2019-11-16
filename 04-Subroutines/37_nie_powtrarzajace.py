import re
def niePowtarza(tab):
    tab2=[]
    for i in tab:
        x=re.findall(str(i),str(tab))
        if (len(x)==1):
            tab2.append(i)
    return tab2        
tablica=[1,1,2,3,3,4,5,5,6]
print(f"Nie powtarzające się elementy tablicy: {niePowtarza(tablica)}")