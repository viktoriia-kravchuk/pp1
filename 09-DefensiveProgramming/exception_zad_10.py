try:
    file=open("NoEducation.txt","r")
    print(file.read())
    file.close()
except IOError:
    print("IO error, brak pliku o podanej nazwie lub nie można odczytać danych z pliku")
  
