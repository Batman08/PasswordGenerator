import random
import string

class GeneratePasswords(object):

    def CreatePassword(characters_to_use):
        pass_length = 20
        amount_of_passwords = 5
        for x in range(amount_of_passwords):
            password ="".join(random.sample(characters_to_use, pass_length))
            print(password)