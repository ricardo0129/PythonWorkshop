def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

four_factorial = factorial(4)
print(four_factorial)