suma_parzyste=0
suma_niep=0
for i in range(1,51):
    if i%2==0:
        suma_parzyste+=i
    else:
        suma_niep+=i
print(f"Suma liczb parzystych z przedziału <1,50> wynosi: {suma_parzyste}, suma liczb nieparzystych: {suma_niep}")        