# 64_star_pattern_2.py

rows = 30

print("----------------")
for r in range(1, rows+1):
    # printing a row with columns
    for c in range(1, r+1):
        print('* ', end='')
    print()
print("----------------")

"""
r   c
1   1
2   1
    2
3   1
    2
    3
4   1
    2
    3
    4
5   1
    2
    3
    4
    5
^^^^^^^^^^^^^^^^^^^^^^
O/p

*
**
***
****
*****
------------------

"""
