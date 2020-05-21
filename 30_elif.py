# 30_elif.py
# Nested conditional statements

age = int(input("Enter age: "))

if(age <= 2):
    print("Infant")
else:
    if(age <= 12):
        print("Child")
    else:
        if(age <= 19):
            print("Teen")
        else:
            if(age <= 60):
                print("Adult")
            else:
                print("Sr. Citizen")
