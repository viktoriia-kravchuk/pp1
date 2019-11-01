file=open("numbers.txt","r")
parzyste=open("evennumbers.txt","a")
for i in file:
    if int(i)%2==0:
        parzyste.write(i)
file.close()
parzyste.close()