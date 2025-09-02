from statistics import * # importing all the statistics modules
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))       # ~22.9
print(median(ages))     # 23
print(mode(ages))       # 20
print(stdev(ages))      # ~2.3

import math
print(math.pi)           # 3.141592653589793, pi constant
print(math.sqrt(2))      # 1.4142135623730951, square root
print(math.pow(2, 3))    # 8.0, exponential function
print(math.floor(9.81))  # 9, rounding to the lowest
print(math.ceil(9.81))   # 10, rounding to the highest
print(math.log10(100))   # 2, logarithm with 10 as base

#or
from math import pi as PI, sqrt, pow, floor, ceil, log10
print(PI)                 # 3.141592653589793
print(sqrt(2))            # 1.4142135623730951
print(pow(2, 3))          # 8.0
print(floor(9.81))        # 9
print(ceil(9.81))         # 10
print(math.log10(100))    # 2

#or
from math import *
print(pi)                 # 3.141592653589793
print(sqrt(2))            # 1.4142135623730951
print(pow(2, 3))          # 8.0
print(floor(9.81))        # 9
print(ceil(9.81))         # 10
print(math.log10(100))    # 2

import string
print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)        # 0123456789
print(string.punctuation)   # "#$%&'()*+,-./:;<=>?@[\]^_`{|}~!

from random import random, randint, choice
print(random())   # it doesn't take any arguments; it returns a value between 0 and 0.9999
print(randint(5, 20)) # it returns a random integer number between [5, 20] inclusive

def random_user_id(n):
    letters = string.ascii_letters
    digits = string.digits
    pool = letters + digits
    code = ''.join(choice(pool) for _ in range(n))
    #code2 = ''
    #for i in range (6):
   #     code2 += choice(pool)
   # print(f'one example is {code1} and another is {code2}')
    return code


def user_id_gen_by_user():
    number_of_chars = input('Please enter the length of the code: ')
    number_of_codes = input('Please enter the number of the codes to generate: ')

    for _ in range(int(number_of_codes)):
        print(random_user_id(int(number_of_chars)))

user_id_gen_by_user()

def unique_codes(n):
    set_to_return = set()
    while len(set_to_return) < n:
        set_to_return.add(randint(0,9))
    return list(set_to_return)

print(unique_codes(7))
