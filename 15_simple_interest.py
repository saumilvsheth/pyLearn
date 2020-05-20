# 15_simple_interest.py
#si = (p*n*r)/100

print("----Simple Interest----")
p = input("Principle       :")
n = input("Number of months:")
r = input("Rate of interest:")

p = int(p)
n = int(n)
r = int(r)

si = (p * n * r) // 100

print(f'Simple Interest   : {si}')

'''
----Simple Interest----
Principle       :100000
Number of months:12
Rate of interest:3
Simple Interest   : 36000
'''
