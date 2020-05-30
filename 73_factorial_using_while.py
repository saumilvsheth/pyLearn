# 73_factorial_using_while.py

n = 5
factorial = 1

i = n
while(i > 0):
    factorial = factorial * i
    i = i - 1

print(f"{n}! = {factorial}")
