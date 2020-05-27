# 66_star_pattern_4.py

rows = 5

print("----------------")
for r in range(rows+1):
    for c in range(rows - r + 1):
        print(' ', end='')

    for c in range(1, r+1):
        print('*', end='')
    print()
print("----------------")

"""
^^^^^^^^^^^^^^^^^^^^^^
O/p

----------------
        *
      * *
    * * * 
  * * * * 
* * * * *
----------------

"""
