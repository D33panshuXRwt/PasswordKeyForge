import itertools
import string


def print_clear_ascii_art():
    clear_ascii_art = """
_____                                    _ _               __                     
|  __ \\                                  | | |            / _|                    
| |__) |_ _ ___ _____      _____  _ __ __| | | _____ _   _| |_ ___  _ __ __ _  ___ 
|  ___/ _` / __/ __\\ \\ /\\ / / _ \\| '__/ _` | |/ / _ \\ | | |  _/ _ \\| '__/ _` |/ _ \\
| |  | (_| \\__ \\__ \\\\ V  V / (_) | | | (_| | | <  __/ |_| | || (_) | | | (_| |  __/
|_|   \\__,_|___/___/ \\_/\\_/ \\___/|_|  \\__,_|_|\\_\\___|\\__, |_| \\___/|_|  \\__, |\\___|
                                                       __/ |              __/ |     
                                                      |___/              |___/      
"""

    print(clear_ascii_art)

# Call the function to print the ASCII art for "clear"
print_clear_ascii_art()


print("<<----- Types of Password Method ----->>")
print("""
    1. Default (contains only charcters both UPPER-CASE and lower-case)
    2. Lower-Case only
    3. Upper-Case only 
    4. Numbers (Use for OTP/PIN)
    5. ALL-IN (contains everthing Characters/Numbers,Special characters)
""")

# try:

#     askpswd = int(input("Enter your choice: "))

#     if askpswd == 1:
#             characters = string.ascii_letters
#     elif askpswd == 2:
#             characters = string.ascii_lowercase
#     elif askpswd == 3:
#             characters = string.ascii_uppercase
#     elif askpswd == 4:
#             characters = string.digits
#     elif askpswd == 5:
#             characters = string.printable
#     else:
#         print("Choose Valid Option")
    
#     i = 0
#     length = int(input("Enter number of characters needed in password: "))
#     for combination in itertools.combinations(characters, length):
#         print(combination)
#         i=i+1
#     print(i)

# except ValueError:
#     print("<<---- Enter a numerical value to execute file ---->>")


try:
    def quesusr():
        global characters
        askpswd = int(input("Enter your choice: "))

        if askpswd == 1:
            characters = string.ascii_letters
        elif askpswd == 2:
            characters = string.ascii_lowercase
        elif askpswd == 3:
            characters = string.ascii_uppercase
        elif askpswd == 4:
            characters = string.digits
        elif askpswd == 5:
            characters = string.printable
        else:
            if askpswd <= 6:
                print("Choose Valid Option")
                quesusr()

    quesusr()

    i = 0
    length = int(input("Enter number of characters needed in the password: "))
    for combination in itertools.product(characters, repeat=length):  # Use itertools.product for all combinations
        print(''.join(combination))  # Join the characters of the combination
        i += 1
    print(i)

except ValueError:
    print("<<---- Enter a numerical value to execute the file ---->>")