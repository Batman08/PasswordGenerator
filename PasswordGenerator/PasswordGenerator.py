import random
import string
import GeneratePasswords as gp
import CharactersToUse as ctu

UPPERCASE_LETTERS = string.ascii_uppercase
LOWERCASE_LETTERS = string.ascii_lowercase
NUMBERS = string.digits
SYMBOLS = string.punctuation

upper_case = True
lower_case = True
numbers = True
symbols = True

characters_to_use = ""


characters_to_use = ctu.CharactersToUse.check_characters_use(LOWERCASE_LETTERS, NUMBERS, SYMBOLS, UPPERCASE_LETTERS, lower_case, numbers, symbols, upper_case, characters_to_use)

gp.GeneratePasswords.CreatePassword(characters_to_use)