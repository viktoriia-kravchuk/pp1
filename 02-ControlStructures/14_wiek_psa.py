wiek=int(input("Podaj wiek psa w ludzkich latach: "))
type(wiek)
if wiek>2:
    wiek_psi_lata=int((2*10.5)+((wiek-2)*4))
else:
    wiek_psi_lata=int(wiek*10.5)
print(f"Wiek psa w psich latach to {wiek_psi_lata} lat")    