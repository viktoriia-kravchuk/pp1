tab=[]
with open("universities.txt", "r") as file:
    for i in file:
        tab.append(str(i))
file.close()
tab.sort()
f=open("universities.txt").readlines()
c=open("universities.txt","w")
j=0
for l in f:
    c.write(str(l).replace(str(l),tab[j]))
    j+=1
c.close()    
    
    