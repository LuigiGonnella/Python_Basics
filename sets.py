first_set = set()

set_with_values = {'first', 'second', 'third'} #a set NON contiene duplicati

len(set_with_values) #find length
if ('fourth' in set_with_values):
    print('Present')
else:
    print('Not present')

#Adding item
set_with_values.add('fourth')
print(set_with_values) #there is NO ORDER in a set, at every run of the program, the order will be different
print(set_with_values) #there is NO ORDER in a set, but in the same run the order is the same

#Adding different items
set_with_values.update(['fifth', 'sixh', 'seventh']) #in no order
print(set_with_values)

#Removing form set
set_with_values.remove('fourth') #rermoves the given element
print(set_with_values) 

element_removed = set_with_values.pop() #removes a random eleemnt and returns it
print(element_removed)
print(set_with_values) 

#Clearing a set
set_with_values.clear() # --> set()

#Deleting set
del set_with_values #--> doesn't exist anymore

#Converting List to Set
lst = ['ciao', 'bella', 'come', 'stai', 'io', 'bene']
st = set(lst)
print(st)

#UNION OF SETS (JOIN)
set1 = {1, 3, 5}
set2 = {'ciao', 'bella', 'come', 'stai'}
set_union = set1.union(set2) #we can merge types as always
print(set_union)

#ADDING INTO A SET
set1.update(set2) #like union but inside set1

#INTERSECTION OF SETS
set1.add('ciao')
set1.update({'aooooooooo'})
intersection_set = set1.intersection(set2)
print(intersection_set)
print(set1)

#findind SUBSET and SUPERSET
#as of now set1 --> {'come', 1, 3, 5, 'aooooooooo', 'bella', 'stai', 'ciao'} is a SUPERSER of set2 --> {'ciao', 'bella', 'come', 'stai'}

print(set1.issuperset(set2)) # --> True

#DIFFERENCE
print(set1.difference(set2)) # --> {1, 3, 5, 'aooooooooo'}
print(set2.difference(set1)) # --> set()

#SYMMETRIC DIFFERENCE --> like difference but makes no difference the order of the operands
print(set1.symmetric_difference(set2)) # --> {1, 3, 5, 'aooooooooo'}
print(set2.symmetric_difference(set1)) # --> {1, 3, 5, 'aooooooooo'}

#DISJOINT SETS --> if there are NO common elements
set1 = {1, 2, 3}
set2 = {2, 5, 6}

print(set1.isdisjoint(set2)) # --> False


set2.remove(2)
print(set1.isdisjoint(set2)) # --> True


#EXERCISES
age = [22, 19, 24, 25, 26, 24, 25, 24] #conta anche i duplicati
set_age = set(age) #NON contiene duplicati

if (len(age) > len(set_age)):
    print('list has a bigger length')
elif (len(age) < len(set_age)):
    print('set has a bigger length')
else:
    print('the lenght of list and set are equal')


# String: text, immutable
# List: ordered, mutable, allows duplicates
# Tuple: ordered, immutable, allows duplicates
# Set: unordered, mutable, no duplicates

string_ex = 'I am a teacher and I love to inspire and teach people'
lst = string_ex.split()
st = set(lst)
print(len(st)) #prints the unique words of the initial sentence