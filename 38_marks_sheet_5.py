# 38_marks_sheet_5.py
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

status = ""
if(m_1 < 35):
    status = "FAIL"
elif(m_2 < 35):
    status = "FAIL"
elif(m_3 < 35):
    status = "FAIL"
else:
    status = "PASS"


print("---- Report ----")
print(f"Name     : {name}")
print(f"Maths    : {m_1}")
print(f"Physics  : {m_2}")
print(f"Chemistry: {m_3}")
print("---------------------------------------")

if (
        m_1 < 0
        or m_1 > 100
        or m_2 < 0
        or m_2 > 100
        or m_3 < 0
        or m_3 > 100):
    print("Wrong Entry/Entries, Please try again.")
else:
    print(f"Total    : {total}")
    print(f"Percent  : {percent}")
    print(f"Grade    : {grade}")
    print(f"Status   : {status}")
print("=========================================")
