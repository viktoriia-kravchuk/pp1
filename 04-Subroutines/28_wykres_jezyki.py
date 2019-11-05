def rysujWykres(jezyki,wartosc):
    l=len(jezyki)
    for i in range(l):
        str=jezyki[i]
        print(f"{str.rjust(10)}: {'#'*wartosc[i]}")
tab=["Java","Python","JavaScript","C++","C#","Ruby","Perl","PHP","C","Android"]
liczby=[61,47,37,32,26,18,14,14,9,7]
rysujWykres(tab,liczby)