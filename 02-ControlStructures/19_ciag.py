n=int(input("Podaj wartość N: "))
a=1
i=0
ciag=""
for i in range(n):
    ciag+=str(a)+","
    a+=3
print (f"Ciąg arytmetyczny o różnicy 3: {ciag}")  
    