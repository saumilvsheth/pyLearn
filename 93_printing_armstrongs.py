# 92_armstrong_number.py
# ---------------------------------------------------------------
# An Armstrong number is a number such that the sum
# of its digits raised to the third power is equal to the number itself.
# For example, 371 is an Armstrong number, since
# 3**3 + 7**3 + 1**3 = 371.
# ---------------------------------------------------------------


def is_armstrong(n):
    num = n
    sum = 0
    while(num > 0):
        rem = num % 10
        sum = sum + (rem**3)
        num = num // 10

    return n == sum


def main():
    print("Armstrong Numbers below 1000")
    for i in range(1000+1):
        if(is_armstrong(i)):
            print(i)


main()
