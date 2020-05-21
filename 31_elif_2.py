# 31_elif_2.py
# Else-If ladder
age = int(input("Enter age: "))

if(age <= 2):
    print("Infant")
elif(age <= 12):
    print("Child")
elif(age <= 19):
    print("Teen")
elif(age <= 60):
    print("Adult")
else:
    print("Sr. Citizen")
