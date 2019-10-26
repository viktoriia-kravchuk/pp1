pesel=input("Podaj PESEL: ")
p_rok=int(pesel[0:2])
p_miesiac=int(pesel[2:4])
if p_miesiac>=0 and p_miesiac<=12:
    rok_urodzenia=1900+p_rok
elif p_miesiac>80 and p_miesiac<=92:
    rok_urodzenia=1800+p_rok    
elif p_miesiac>20 and p_miesiac<=32:
    rok_urodzenia=2000+p_rok
elif p_miesiac>40 and p_miesiac<=52:
    rok_urodzenia=2100+p_rok
elif p_miesiac>60 and p_miesiac<=72:
    rok_urodzenia=2200+p_rok
if int(pesel[9])%2==0:
    plec="kobieta"
else:
    plec="mężczyzna"
wiek=2019-rok_urodzenia    
print(f"Płeć: {plec}\nWiek: {wiek}")     
    

