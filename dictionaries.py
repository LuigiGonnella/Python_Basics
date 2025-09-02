dict = {}
dict_with_values = {
    'country': 'USA',
    'city': 'LA'
}

len(dict_with_values) #2
print(dict_with_values['country']) #USA and ERROR if doesn't exist

#GET THE VALUE OF A KEY, like dict_with_values[key]
print(dict_with_values.get('country')) #USA and None if doesn't exist

#ADDING elements
dict_with_values['year'] = 2025
print(dict_with_values)

#MODIFIYNG elements
dict_with_values['city'] = 'Philadelphia'
print(dict_with_values)

#CHECK PRESENCE of KEYS
if ('city' in dict_with_values):
    print(f'City is present! and it\'s {dict_with_values['city']}')

#REMOVINGS
dict_with_values.pop('year') #in-place, deletes year (key-value)
print(dict_with_values)

dict_with_values.popitem() #delets the last item (key-value)
print(dict_with_values)

del dict_with_values['country'] #in-place, deletes country (key-value)
print(dict_with_values)

dict_with_values.clear() #dict()
del dict_with_values #deleted

#FORM DICT to LIST of TUPLE (key, value)
dict_with_values = {
    'country': 'USA',
    'city': 'LA',
    'year': 2025, 
    'is_great': True
}

list_of_tuples = dict_with_values.items()
print(list_of_tuples) #not a simple list but a type dict_items([('country', 'USA'), ('city', 'LA'), ('year', 2025), ('is_great', True)])

#LIST OF KEYS
list_of_keys = dict_with_values.keys()
print(list_of_keys) #not a simple list but a type dict_keys(['country', 'city', 'year', 'is_great'])

#LIST OF VALUES
list_of_values = dict_with_values.values()
print(list_of_values) #not a simple list but a type dict_values(['USA', 'LA', 2025, True])

#COPY
dict_with_values.copy()



