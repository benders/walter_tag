# Write your code here :-)

import random

def cow(eyes = 'oo'):
    cow = '''       \\   ,__,
        \\  (@@)____
           (__)    )\\
              ||--|| *
'''
    return cow.replace('@@',eyes,1)

def walterize(word):
    return "Walter is " + word

def get_adjective():
    lines = False
    with open("adjectives.txt") as f:
        lines = f.readlines()
    return random.choice(lines)
