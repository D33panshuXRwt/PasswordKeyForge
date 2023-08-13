import itertools
import string

def print_clear_ascii_art():
    clear_ascii_art = """
 ______                                    ___              ___
 |  __ \\                                  | | |            / __|                    
 | |__) |_ _ ___ _____      _____  _ __ __| | | _____ _   _| |_ ___  _ __ __ _  ___ 
 |  ___/ _` / __/ __\\ \\ /\\ / / _ \\| '__/ _` | |/ / _ \\ | | |  _/ _ \\| '__/ _` |/ _ \\
 | |  | (_| \\__ \\__ \\\\ V  V / (_) | | | (_| | | <  __/ |_| | || (_) | | | (_| |  __/
 |_|   \\__,_|___/___/ \\_/\\_/ \\___/|_|  \\__,_|_|\\_\\___|\\__, |_| \\___/|_|  \\__, |\\___|
                                                       __/ |              __/ |     
                                                      |___/              |___/      
    """
    print(clear_ascii_art)

print_clear_ascii_art()
    

print("<<----- Types of Password Methods ----->>")
print("""
    1. Default (contains both UPPER-CASE and lower-case characters)
    2. Lower-Case only
    3. Upper-Case only 
    4. Numbers (Use for OTP/PIN)
    5. ALL-IN (contains all Characters/Numbers, Special characters)
    6. Custom
""")

def get_character_set(choice):
    if choice == 1:
        return string.ascii_letters
    elif choice == 2:
        return string.ascii_lowercase
    elif choice == 3:
        return string.ascii_uppercase
    elif choice == 4:
        return string.digits
    elif choice == 5:
        return string.printable
    elif choice == 6:
        characters = input("Enter your favorable characters: ")
        return characters
    else:
        print("Choose a Valid Option")
        return None

def generate_passwords(characters, length):
    passwords = []
    for combination in itertools.product(characters, repeat=length):
        passwd = ''.join(combination)
        passwords.append(passwd)
    return passwords

try:
    askpswd = int(input("Enter your choice: "))
    
    characters = get_character_set(askpswd)
    
    while characters is None:
        askpswd = int(input("Enter your choice: "))
        characters = get_character_set(askpswd)
        
    length = int(input("Enter the number of characters needed in the password: "))
    passwords = generate_passwords(characters, length)
    
    filename = input("Enter file name to save passwords: ")
    with open(filename, "w") as f:
        for passwd in passwords:
            f.write(passwd + "\n")
    
    print("Total passwords generated:", len(passwords))
    print("Passwords saved in", filename)

except ValueError:
    print("<<---- Enter a numerical value to execute the file ---->>")
except Exception as e:
    print("An error occurred:", e)
 
