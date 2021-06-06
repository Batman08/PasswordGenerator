import random
import string

UPPERCASE_LETTERS = string.ascii_uppercase
LOWERCASE_LETTERS = string.ascii_lowercase
NUMBERS = string.digits
SYMBOLS = string.punctuation

upper_case = True
lower_case = True
numbers = True
symbols = True

characters_to_use = ""

if upper_case:
    characters_to_use += UPPERCASE_LETTERS
if lower_case:
    characters_to_use += LOWERCASE_LETTERS
if numbers:
    characters_to_use += NUMBERS
if symbols:
    characters_to_use += SYMBOLS

pass_length = 20
amount_of_passwords = 5

for x in range(amount_of_passwords):
    password ="".join(random.sample(characters_to_use, pass_length))
    print(password)