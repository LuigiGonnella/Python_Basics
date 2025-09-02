#we already seen lambda functions and list_comprehension

#list_comprehension
def calculate_sum_of_first_even(n):
    even = [i for i in range(n) if i%2==0] #list of even numbers
    tot = sum(even)
    print(tot)

calculate_sum_of_first_even(10)

#lambda function 
x = lambda a, b, c, d: a + b + c + d
print(x(1, 2, 3, 4))

#inside another function
def sum_elements(a, b):
    return lambda x: x + a + b
#we need a thrid argument when we call the function
print(sum_elements(1, 2)(3)) #in separate brackets

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

def func(lst):
    ret = []
    for el in lst:
        ret.append(' '.join([el[0][0], el[0][1]]))
    print(ret)

func(names)