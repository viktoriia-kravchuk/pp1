imiona=["Genowefa","Onufry","Celestyna","Alojzy","Pankracy","Teofil"]
max=0
for i in imiona:
    dl=len(i)
    if dl>max:
        max=dl
        imie=i
print(f"najdłuższe imię: {imie}")        
