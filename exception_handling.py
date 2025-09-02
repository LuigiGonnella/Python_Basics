def function():
    try:
        #inp = input('Enter a number: ')
        #return 1 + inp
    #except Exception as e:
       # print(e)
    #else:
        print('ciao') #non printa mai, entra qui solo se non entra in try ed except, si usa se facciamo except di eccezioni specifiche, non di tutte come in questo caso
    finally:
        print('This always prints')

function()

#UNPACKING

def func(a, b, c, d):
    return a + b + c + d

lst = [1, 2, 3, 4]

print(func(*lst)) #unpack lists with *

a = range(2,7)
print(*a) #unpack ranges with *

dict = {'name':'Asabeneh', 'country':'Finland', 'city':'Helsinki', 'age':250}

def print_full_info(name, country, city, age):
    print(f'{name} lives in {country} in {city} and is {age} old')

print_full_info(**dict) #unpack dictionaries with **

#PACKING, is the opposite

def func(*lst):
    return sum(lst)

a, b, c, d = 1, 2, 3, 4

print(func(a, b, c, d))

#SPREADING

positives_big = [100, 99, 90, 60]
positives_little = [30, 20, 10, 3]

lst = [*positives_big, 40, 38, *positives_little, -1, -2, -3, ]
print(lst)
