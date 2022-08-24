def factorial(n):
    print(f"I am in function factorial with n = {n}")
    if n == 1:
        print(f"I am returning from function factorial with return 1")
        return 1
    r = n*factorial(n-1)
    print(f"I am returning from function factorial with return {r}")
    return r

print(factorial(996))
