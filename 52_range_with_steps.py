# 52_range_with_steps.py
n = 10
print("Starting at 0\nStep: 2")
for i in range(0, n, 2):
    print(i)

print("Starting at 1\nStep: 2")
for i in range(1, n, 2):
    print(i)

print("Starting at 5\nStep: 2")
for i in range(5, n, 2):
    print(i)

"""[output]
Starting at 0
Step: 2
0
2
4
6
8
Starting at 1
Step: 2
1
3
5
7
9
Starting at 5
Step: 2
5
7
9
"""
