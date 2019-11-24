import re
file=open("land.txt","r")
cyfry=[]
for l in file:
    cyfry+=re.findall(r"\d",l)
suma=0
for i in cyfry:
    suma+=int(i)
print(f"Suma cyfr w pliku wynosi {suma}")    
file.close()

