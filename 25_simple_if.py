# 25_simple_if.py
name = input("enter your name : ")
message = "Hello friend!"

if(name != ""):
    message = f'Hello {name}!'

print(message)

# ---- Another approach ----
# if(name != ""):
#     print(f'Hello {name}!')
# else:
#     print('Hello friend!')
