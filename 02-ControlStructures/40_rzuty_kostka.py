import random
jeden=0
dwa=0
trzy=0
cztery=0
piec=0
szesc=0
for i in range(100):
    a=random.randrange(1,7)
    if a==1:
        jeden+=1
    elif a==2:
        dwa+=1
    elif a==3:
        trzy+=1
    elif a==4:
        cztery+=1
    elif a==5:
        piec+=1
    else:
        szesc+=1
print(f"Szóstka: {szesc}\nPiątka: {piec}\nCzwórka: {cztery}\nTrójka: {trzy}\nDwójka: {dwa}\nJedynka: {jeden}")        