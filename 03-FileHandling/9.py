with open("NoEducation.txt","r") as file:
    n=1  
    for line in file:
        print(n,line,end="")
        n+=1
file.close()
