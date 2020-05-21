# 23_eligibility_form.py
print("--- Under 18 Athletics enrolment ----")

name = input("Enter name   : ")
age = int(input("Enter age :"))

if(age <= 18):
    print(f'{name} is eligible')
else:
    print(f'{name} is not eligible')

print("--> End of form <--")

'''
$ python 23_eligibility_form.py
--- Under 18 Athletics enrolment ----
Enter name   : Rithu
Enter age :15
Rithu is eligible
--> End of form <--

$ python 23_eligibility_form.py
--- Under 18 Athletics enrolment ----
Enter name   : Raja
Enter age :20
Raja is not eligible
--> End of form <--
'''
