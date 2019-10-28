with open("numbers.txt","r") as file:
    suma=0 
    for liczba in file:
        suma+=int(liczba)
print(f"Suma wynosi: {suma}")         
file.close()      