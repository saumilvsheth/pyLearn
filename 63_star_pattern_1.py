# 63_star_pattern_1.py

rows = 5
columns = 5

print("----------------")
for r in range(rows+1):
    # printing a row with columns
    for c in range(columns+1):
        print('* ', end='')
    print()
print("----------------")
