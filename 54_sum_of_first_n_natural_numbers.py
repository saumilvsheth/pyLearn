# 54_sum_of_first_n_natural_numbers.py

n = 5
sum = 0
for i in range(1, n+1):
    sum = sum + i

print(f"Sum of first {n} Natural numbers = {sum}")

"""
Iteration   i   sum 
---------------------
                0
1           1   0 + 1 = 1
2           2   1 + 2 = 3
3           3   3 + 3 = 6
4           4   6 + 4 = 10
5           5   10 + 5 = 15
"""
