# 109_max_number_in_a_list.py
import math

my_list = [
    34, 5, 77, 87, 556, 99, 98, 347, 33, 232
]

max = -math.inf

for num in my_list:
    if(num > max):
        max = num

print('Max = ', max)
