# 94_strong_number
# Strong Numbers are the numbers whose
# sum of factorial of digits is equal to
# the original number.
# 145 = 1! + 4! + 5!


def factorial(n):
    fact = 1
    i = n
    while (i > 1):
        fact *= i
        i -= 1
    return fact


def is_strong(n):
    num = n
    sum = 0
    while (num > 0):
        rem = num % 10
        sum += factorial(rem)
        num = num // 10
    return n == sum


def main():
    print("Strong numbers")
    print(145, is_strong(145))
    print(245, is_strong(245))


main()
