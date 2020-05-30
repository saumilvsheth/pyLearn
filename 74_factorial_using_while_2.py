# 74_factorial_using_while_2

n = 5
factorial = 1

i = n
while(i > 1):
    factorial = factorial * i
    print(i, end=" * ")
    i = i - 1

print(f"1 = {factorial}")
