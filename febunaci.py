def fib(n):
    if n==1:
        return 1
    if n==0:
        return 0
    r = fib(n-1)+fib(n-2)
    return r

print(fib(10))
