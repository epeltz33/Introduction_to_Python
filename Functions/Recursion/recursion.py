def factorial(n: object) -> object:
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)



print(factorial(12))
