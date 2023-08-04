import itertools
import string

print("<<----- Enter the type of password want to create ----->>")
print("""
    1. Default (contains only charcters both UPPER-CASE and lower-case)
    2. Lower-Case only
    3. 
    
    2. Numbers (Use for OTP/PIN)
    3. ALL-IN (contains everthing Characters/Numbers,Special characters)
""")





characters = string.ascii_letters

try:
    length = int(input("Enter number of characters needed in password: "))
    for combination in itertools.combinations(characters, length):
        print(combination)
except ValueError:
    print("<<---- Enter a numerical value to execute file ---->>")