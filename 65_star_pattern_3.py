# 65_star_pattern_3.py

rows = 5

print("----------------")
for r in range(rows, 0, -1):
    # printing a row with columns
    for c in range(1, r+1):
        print('* ', end='')
    print()
print("----------------")

"""
r   c
5   1
    2
    3
    4
    5
4   1
    2
    3
    4
3   1
    2
    3
2   1
    2
1   1

^^^^^^^^^^^^^^^^^^^^^^
O/p

----------------
* * * * * 
* * * * 
* * * 
* * 
* 
----------------

"""
