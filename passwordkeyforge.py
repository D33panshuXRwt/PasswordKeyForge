import itertools
import string

characters = string.ascii_letters
length = int(input("Enter number of characters needed in password: "))


try:
    for combination in itertools.combinations(characters, length):
        print(combination)
except:
    print("<<---- Enter a numerical value to execute file ---->>")