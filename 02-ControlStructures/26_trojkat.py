w=10 #wysokosc
s=6 #szerokosc
for j in range(w):
    if(j<s):
        print(j*"* ")
    else:
        print((w-j)*"* ")
