# 09_string_interpolation.py
a = 15
b = 2
sum = a + b

print(f'Method 1: {a} + {b} = {sum}')
print("Method 2:", a, " + ", b, " = ", sum)
print("Method 3:" + str(a) + " + " + str(b) + " = " + str(sum))

'''
Output in multi line comments
Method 1: 15 + 2 = 17
Method 2: 15  +  2  =  17
Method 3:15 + 2 = 17
'''
# More at https://www.programiz.com/python-programming/string-interpolation
