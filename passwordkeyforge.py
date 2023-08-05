import itertools
import string

print("<<----- Types of Password Method ----->>")
print("""
    1. Default (contains only charcters both UPPER-CASE and lower-case)
    2. Lower-Case only
    3. Upper-Case only 
    4. Numbers (Use for OTP/PIN)
    5. ALL-IN (contains everthing Characters/Numbers,Special characters)
""")
askpswd = input("Enter your choice: ")

if askpswd == "1" or "Default" or int(askpswd) == 1:
    characters = string.ascii_letters
elif askpswd == "2" or "Lower-Case" or int(askpswd) ==2:
    characters = string.ascii_lowercase
elif askpswd == "2" or "Lower-Case" or int(askpswd) ==2:
    characters = string.ascii_lowercase
elif askpswd == "2" or "Lower-Case" or int(askpswd) ==2:
    characters = string.ascii_lowercase


try:
    length = int(input("Enter number of characters needed in password: "))
    for combination in itertools.combinations(characters, length):
        print(combination)
except ValueError:
    print("<<---- Enter a numerical value to execute file ---->>")