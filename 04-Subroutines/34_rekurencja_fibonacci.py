def fib(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    if n>2:
        return fib(n-1)+fib(n-2)
for i in range(1,21):
    print(fib(i),end=" ")      

