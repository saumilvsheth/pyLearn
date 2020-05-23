# 33_logical_and.py
print("---- Max of three numbers using logical and ----")
a = int(input("Enter first number : "))
b = int(input("Enter second number: "))
c = int(input("Enter third number : "))

if(a > b and a > c):
    print(f"Max: {a}")
elif(b > a and b > c):
    print(f"Max: {b}")
else:
    print(f"Max: {c}")
