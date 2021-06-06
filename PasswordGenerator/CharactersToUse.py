import random
import string

class CharactersToUse(object):

    def check_characters_use(LOWERCASE_LETTERS, NUMBERS, SYMBOLS, UPPERCASE_LETTERS, lower_case, numbers, symbols, upper_case, characters_to_use):
        if upper_case:
            characters_to_use += UPPERCASE_LETTERS
        if lower_case:
            characters_to_use += LOWERCASE_LETTERS
        if numbers:
            characters_to_use += NUMBERS
        if symbols:
            characters_to_use += SYMBOLS
        return characters_to_use