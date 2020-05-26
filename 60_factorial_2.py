# 59_factorial.py
# 1! = 1
# 2! = 2 * 1
# 3! = 3 * 2 * 1
# 4! = 4 * 3 * 2 * 1
# 5! = 5 * 4 * 3 * 2 * 1

factorial = 1
n = 5
for i in range(n, 0, -1):
    factorial = factorial * i

print(f"{n}! = {factorial}")
"""
Iteration   i       factorial
------------------------------
1
2
3
4
5
"""
