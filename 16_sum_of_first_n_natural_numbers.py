# 16_sum_of_first_n_natural_numbers.py
# Formulae explanations: https://brilliant.org/wiki/sum-of-n-n2-or-n3/
# sum = (n * (n+1)) / 2
print("---- Sum of first n natural numbers ----")
n = int(input("Enter n: "))
sum = (n * (n+1)) // 2
print(f"Sum: {sum}")

'''
$ python 16_sum_of_first_n_natural_numbers.py
---- Sum of first n natural numbers ----
Enter n: 5
Sum: 15
 $ python 16_sum_of_first_n_natural_numbers.py
---- Sum of first n natural numbers ----
Enter n: 10
Sum: 55
'''
