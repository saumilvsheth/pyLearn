# 84_factorial_function.py


def printFactorial(n):
    # Factorial Logic starts.
    factorial = 1

    i = n
    while(i > 0):
        factorial = factorial * i
        i = i - 1

    print(f"{n}! = {factorial}")
    # Factorial Logic ends.


# Execution starts here
limit = 5
n = 1
while(n <= limit):
    printFactorial(n)
    n += 1
