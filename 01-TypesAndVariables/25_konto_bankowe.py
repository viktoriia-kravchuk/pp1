nr_rachunku=input("Podaj nr rachunku bankowego: ")
if len(nr_rachunku)!=26:
    print("Długość nr rachunku bankowego wynosi 26, wprowadź ponownie")
elif nr_rachunku.isdigit():
    print("Nr rachunku: ",nr_rachunku[0:2],nr_rachunku[2:6],nr_rachunku[6:10],
          nr_rachunku[10:14],nr_rachunku[14:18],nr_rachunku[18:22],nr_rachunku[22:26])
else:
    print("Wprowadź tylko cyfry")    