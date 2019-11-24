def fib(n):
    a,b = 0,1 #pierwszy i drugi wyraz 0 i 1
    for i in range(n-1): #petla ktora oblicza n-ty wyraz ciagu
        a,b = b,a+b # a=b b=a+b
    return a # zwracana wartosc n-ty wyrazu
for j in range(20):
    print(fib(j+1),end=" ") #petla wyswietlajaca 20 pierwszych wyrazow 