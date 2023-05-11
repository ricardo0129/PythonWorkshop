#1
def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    
    return fibonacci(n-1) + fibonacci(n-2)

def factorial(n):
    if n == 0:
        return 1
    
    return n * factorial(n-1)

#2
fibs = []
for i in range(15):
    fibs.append(fibonacci(i))

#3
fact = []
for i in range(15):
    fact.append(factorial(i))

#4
for i in range(15):
    if fibs[i] > fact[i]:
        print("Fibonacci > Factorial")
    elif fibs[i] < fact[i]:
        print("Fibonacci < Factorial")
    else:
        print("They are equal")
