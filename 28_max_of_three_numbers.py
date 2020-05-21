# 28_max_of_three_numbers.py
print("---- Max of three numbers ----")
a = int(input("Enter first number : "))
b = int(input("Enter second number: "))
c = int(input("Enter third number : "))

if(a > b):
    # a is max
    if(a > c):
        print("Max: ", a)
    else:
        print("Max: ", c)
else:
    # b is max
    if(b > c):
        print("Max: ", b)
    else:
        print("Max: ", c)
