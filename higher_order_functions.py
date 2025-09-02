#we already seen functions that calls other functions, but we can also see CLOSURES

def add_three():
    three = 3
    def add(n):
        return n + three
    return add

closure = add_three() #closure

print(closure(2)) # --> 5

#DECORATORS: they are likej wrappers useful to add functionalities to an already existing object

#NORMAL
def decorator(function):
    def wrapper():
        param = function()
        param_upper = param.upper()
        return param_upper
    return wrapper

def greetings():
    return 'Hello, Word!'

up = decorator(greetings)
print(up())

#WITH DECORATOR
def decorator(function):
    def wrapper():
        param = function()
        param_upper = param.upper()
        return param_upper
    return wrapper



@decorator
def greetings():
    return 'Hello, Word!'

up = greetings()
print(up)

#IMPORTANT HIGHER ORDER FUNCTIONS MAP, FILTER, REDUCE
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
countries_upper = list(map(lambda x: x.upper(), countries))
print(countries_upper)

from loops.data import data
countries_over_10mill = list(filter(lambda x: x['population']>1000000000 ,data))
print(countries_over_10mill)

numbers_str = ['1', '2', '3', '4', '5']  # iterable

from functools import reduce
def add_two(a, b):
    return int(a) + int(b) 

tot = reduce(add_two, numbers_str)
print(tot)

#ENUMERATE
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

for index, country in enumerate(countries):
    print(f'the country {country} is placed at the index {index} of the array')


#ZIP --> associa in parallelo elementi di due array
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
population = ['0', '1', '2', '3', '4', '5']

for country, index in zip(countries, population):
    print(f'the country {country} is placed at the index {index} of the array')


