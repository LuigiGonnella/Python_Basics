# they are accessible in the same way of the strings
list_py =  [1, 2, {
    'country': 'USA',
    'city': 'Los Angeles'
}] #you can have arrays with different type elements

print(f'the last object of the array is {list_py[len(list_py)-1]}') #the indexes work the same way of strings, so also -1 is the last, -2 the second_last and so on...
print(f'the field country of last object of the array is {list_py[len(list_py)-1]['country']}') 

#Unpacking
long_list = [1, 2, 3, 4, 5, 6, 7, 8]
first, second, third, fourth, *others = long_list
print(f'the array of the remaining elemnts is {others}')

first, second, third, fourth, *others, last = long_list
print(f'the array of the remaining elemnts excluding the last is {others}, while the last is {last}')

#step and slices are the sam eof strings
print(f'{long_list[::-1]}') #reverse
print(f'{long_list[::2]}')#take every two

#adding eleemts
initial_list = list()
initial_list.append(1) #adds at the end
print(initial_list)
initial_list.append(3)
initial_list.append(4)
initial_list.append(5)

initial_list.insert(1, 2) #adds at the index
print(initial_list)

#remove item from a list
initial_list.pop() #remove from the last index (like a stack) or the specified one
initial_list.pop(3) #remove from the last index (like a stack) or the specified one

print(initial_list)


initial_list.remove(2) #remove the given element
print(initial_list)

del initial_list[0] #remove from index
print(initial_list)

del initial_list #remove entire list
# print( initial_list) #error

list_to_clear = [1, 2, 3, 4]
list_to_clear.clear()
print(list_to_clear) #[]

#Copying a list
list1 = ['ciao', 'sono', 'luigi']
list2 = list1.copy()
print(list2)

#joining lists
list_negative = [-1, -2 , -3]
zero = [0]
list_positive = [1, 2, 3, 4]
print(list_negative + zero + list_positive) #sum mantain order
list_negative.extend(zero) #in-place, appends lists at the end
list_negative.extend(list_positive)
print(list_negative)

#Counting a given element in the list
print(list_negative.count(0))

#finding index of element in the list
print(list_negative.index(3))

#reverse a list
print(list_negative[::-1]) #doesn't change the list in-place
list_negative.reverse() #changes the list in-place
print(list_negative)

#sorting
list_to_sort = [0,-4,2,-5, 33, -3]
list_to_sort.sort() #in-place, ascending
print(list_to_sort)

list_to_sort.sort(reverse=True) #in-place, descending
print(list_to_sort)

list_ascending = sorted(list_to_sort, reverse=False) #NOT in-place, ascending
print(list_ascending)

list_descending = sorted(list_to_sort, reverse=True) #NOT in-place, ascending
print(list_descending)

print(list_descending * 2) #doubles the content 