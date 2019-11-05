def podatek(dochod):
    if dochod>5000:
        kwota=int((5000*0.17)+((dochod-5000)*0.32))
    else:
        kwota=int(dochod*0.17)
    return kwota        
zl=int(input("Podaj dochód: "))
print(f"Podatek należny: {podatek(zl)} zł")
