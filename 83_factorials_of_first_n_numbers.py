# 83_factorials_of_first_n_numbers.py

limit = 5

n = 1
while(n <= limit):
    # Factorial Logic starts.
    factorial = 1

    i = n
    while(i > 0):
        factorial = factorial * i
        i = i - 1

    print(f"{n}! = {factorial}")
    # Factorial Logic ends.
    n += 1
