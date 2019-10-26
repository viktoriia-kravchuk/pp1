slowa=["zero","jeden","dwa","trzy","cztery","pięć","sześć","siedem","osiem","dziewięć"]
liczba=input("Podaj liczbę: ")
cyfry_slownie=""
for i in liczba:
    cyfry_slownie+=slowa[int(i)]+" "
print(f"{liczba} - {cyfry_slownie}")    