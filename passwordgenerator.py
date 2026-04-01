import random
import string

length = int(input("Enter desired password length: "))
print("Include in Password:")
use_letters = input("Letters?(y/n): ").lower()
use_numbers = input("Numbers? (y/n):").lower()
use_symbols = input("Special Characters?(y/n):").lower()

characters = ""
if use_letters == 'y':
    characters += string.ascii_letters
if use_numbers == 'y':
    characters+= string.digits
if use_symbols == 'y':
    characters+=string.punctuation
if characters=='':
    print("Error!You must select at least one character type.")
else:
    password=""
    for i in range(length):
        password += random.choice(characters)
    
    print("\nGenerated Password:",password)