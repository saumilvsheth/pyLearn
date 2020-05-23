# 34_marks_sheet_1.py
print('---- Student Marks Sheet Preparation ----')
print('+++++++++++++++++++++++++++++++++++++++++')

name = input("Name: ")
m_1 = int(input("Marks in Maths    : "))
m_2 = int(input("Marks in Physics  : "))
m_3 = int(input("Marks in Chemistry: "))

total = m_1 + m_2 + m_3
percent = (total / 300) * 100
percent = round(percent, 2)

grade = ""
if (percent < 50):
    grade = "C"
elif (percent < 70):
    grade = "B"
else:
    grade = "A"

print("---- Report ----")
print(f"Name     : {name}")
print(f"Maths    : {m_1}")
print(f"Physics  : {m_2}")
print(f"Chemistry: {m_3}")
print("------------------")
print(f"Total    : {total}")
print(f"Percent  : {percent}")
print(f"Grade    : {grade}")

print("=========================================")
