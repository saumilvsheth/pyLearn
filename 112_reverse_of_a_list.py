# 112_reverse_of_a_list.py
my_list = [
    34, 5, 77, 87, 556, 99, 98, 347, 33, 232
]

rev_list = []

last_index = len(my_list) - 1
for i in range(last_index, -1, -1):
    rev_list.append(my_list[i])

print("Reverse: ", rev_list)
