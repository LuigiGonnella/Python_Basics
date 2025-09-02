#IMMUTABLES
empty_tuple = tuple()

tuple_with_initial_values = ('ciao', 'mi', 'chiamo', 'luigi')

#Methods

len(tuple_with_initial_values)
tuple_with_initial_values[0] #accessing elemets, same as always
tuple_with_initial_values[-1]
tuple_with_initial_values[1:len(tuple_with_initial_values)]
tuple_with_initial_values[::-1] 
tuple_with_initial_values[-2:] #as always

#converting tuple to list
tuple_to_list = list(tuple_with_initial_values)
print(tuple_to_list)

#operators
if ('ciao' in tuple_with_initial_values): #in
    print('yes we got it!')

print(tuple_with_initial_values + ('evviva', 'siamo qui')) #+

print(tuple_with_initial_values * 2) #*

#NOT VALID: tuple_with_initial_values[2] we cannot take from index

#Deleting tuple entirly
del tuple_with_initial_values