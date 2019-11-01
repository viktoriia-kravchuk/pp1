tab=[]
file=open("numbersinrows.txt","r")
for i in file:
    x=i.split(",")
    tab+=x
file.close()
l=len(tab)
suma=0
for i in tab:
    suma+=int(i)
print(f"W pliku znajduje się {l} liczb, a ich suma wynosi {suma}")    
    
    
    
    