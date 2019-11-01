file=open("students.txt", "r")
for i in file:
    x=i.split(",")
    if (x[2]).isdigit():
        if int(x[2])<30:
            print (f"{x[0]} {x[1]} {x[4]}", end=" ")
file.close()    
