slowa=["niedostateczny","mierny","dostateczny","dobry","bardzo dobry","celujący"]
ocena=int(input("Podaj ocenę: "))
if ocena<1 or ocena>6:
    print("Podaj poprawną ocenę")
else:
    print (f"Ocena słownie: {slowa[ocena-1]}")