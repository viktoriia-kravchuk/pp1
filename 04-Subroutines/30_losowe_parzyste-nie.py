import random
def liczba():
    x=random.randrange(1,51)
    return x
p=0
n=0    
for i in range(1000):
    if liczba()%2==0:
        p+=1
    else:
        n+=1
procent_parzyte=p/10
procent_nieparzyste=n/10
print(f"Dla 1000 liczb losowych z przedziału <1,50>:\nLiczby parzyte: {procent_parzyte}%\nLiczby nieparzyste: {procent_nieparzyste}%")            
    