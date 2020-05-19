# 07_integer_identifiers.py
a = 10
b = 20
c = a + b

print(a, b, c)  # 10 20 30
print(a + b)  # 30

# TypeError: can only concatenate str (not "int") to str
# print("a = " + a)

print("a = ", a)  # a = 10
print("b = ", b)  # b = 20
print("c = ", c)  # c = 30
