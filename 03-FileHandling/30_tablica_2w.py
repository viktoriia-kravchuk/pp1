tab=[['Marek','Zelnik','zelnik@sed.pl'],['Ewa','Maj','maje@wp.pl'],['Piotr','Wyga','wygap@gop.pl']]
file=open("tablica.csv","a")
l=len(tab)
file.write("Imie,Nazwisko,Email,\n")
for i in range(l):
    x=tab[i]
    l2=len(x)
    for k in range(l2):
        t=tab[i][k]
        file.write(f"{t},")
    file.write("\n")      
file.close()