# 62_prime_number.py
# Program to check if a number is prime or not

num = int(input("Enter a number: "))
isPrime = True

# prime numbers are greater than 1
if num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            isPrime = False
            break

    if isPrime:
        print(num, "is a prime number")
    else:
        print(num, "is not a prime number")
        print(i, "times", num//i, "is", num)

# if input number is less than
# or equal to 1, it is not prime
else:
    print(num, "is not a prime number")
