# Write your code here :-)

import random

def cowsay(text):
    border = " 1234567890123456789012345678901234567890 "
    cow = '''       \\   ,__,
        \\  (oo)____
           (__)    )\\
              ||--|| *
'''
    result = ""
#    result += border + "\n"
#    result += "| " + "WALTER" + " |" + "\n"
#    result += border + "\n"
    result += cow
    return result

def cow():
    cow = '''       \\   ,__,
        \\  (oo)____
           (__)    )\\
              ||--|| *
'''
    return cow

def walterize():
    return "Walter is " + get_adjective()

def get_adjective():
    lines = False
    with open("adjectives.txt") as f:
        lines = f.readlines()
    return random.choice(lines)
