import string
import random

def type_random_letter():
    characters = string.ascii_lowercase + ' '
    return characters[random.randrange(len(characters))]

def build_string(target):
    generated_string = ''
    position = 0

    i = 0
    while position != len(target):

        current_character = type_random_letter()
        if target[position] == current_character:
            generated_string += current_character
            position += 1
            print("ADDED CORRECT LETTER TO STRING. {characters} TO COMPLETION".format(characters = len(target) - position))
            print("THE CURRENT STRING IS: {str}".format(str = generated_string))
            print("CURRENT ITERATION:{i}".format(i = i))
        i += 1

build_string('methinks it is like a weasel sads adsa dsa deas dsad sad sa dsa dsadsada saaaarnjfuwhfn sdnfkjldsnf  kjd      ')



