#escapes
# \n: new line
# \t: Tab means(8 spaces)
# \\: Back slash
# \': Single quote (')
# \": Double quote (")

a = 3
b = 4
print(f'the sum between {a} and {b} is equal to {a+b}')

#unpack lists and strings
word = 'ciao'
letter1, letter2, letter3, letter4 = word #unpack string into variables
print(letter1+letter2+letter3+letter4) #prints ciao

#indexing and slices
list_of_numbers = [0, 1, 2, 3 , 4, 5, 6, 79]
last = list_of_numbers[-1]
second_last = list_of_numbers[-2]
slice_of_numbers = list_of_numbers[3:5] #da 3 (incluso) a 5 (escluso), quindi prendo il numero ad indice 3 e quello ad indice 4
slice_until_the_end = list_of_numbers[1:] #esclude solo il primo (ad indice 0)
print(f'original list: {list_of_numbers}, last number: {last}, second last nmumber {second_last} and slice of numbers: {slice_of_numbers}, excluding the first; {slice_until_the_end}')

#reverse a string
oaic = word[::-1]
print(f'{word} in reverse is equal to {oaic}')

#hop in lists and strings
taking_every_two = list_of_numbers[0:len(list_of_numbers):2] #dall'inizo alla fine prendo ogni 2
print(f'taking every 2 numbers of {list_of_numbers} yopu obtain: {taking_every_two}')

#STRING METHODS TO REMEMBER
Cap = word.capitalize() #converts first character into capital letter
Coun = word.count('o', 0, len(word)) #counts how many times tehri is a substring, optionally with start and end index parameters
ends = word.endswith('d') #tells if the list ends with a certain subarray
starts = word.startswith('wo') #tells if the list starts with a certain subarray
tab_word = 'ciao\tuso\ti\ttab'
expands = tab_word.expandtabs(10) #converts tabs into 8 white spaces ora <parameter> white spaces
first_occurence = word.find('wo') #finds the first index of the first occurence of the subarray given as a parameter (if not returns -1)
last_occurence = word.rfind('wo') #finds the first index of the last occurence of the subarray given as a parameter (if not returns -1)
index = word.index('ci') #like find but you can specify start and end indexes if you want and, if not found, return valeError instead of -1
last_index = word.rindex('ci') #like rfind but with options for start and end indexes and return valueError if occurence not found

#isalnum(), isalpha(), isdecimal() --> 0-9, isdigit() --> valid number, isnumeric() --> extends isdigit() (accept for eexample 1/2), 
#isidentifier() (check if a string is a valid identifier in python --> tab_word --> OK, tab-word --> NOT OK)
#islower(), isupper() --> check if all the alphabetic characters are lowercase
not_joined = ['ciao', 'mi', 'chiamo', 'Luigi']
joined = ' '.join(not_joined) #metto il sepoaratore all'inizio e chiamo il metodo su di esso
print(f"{joined}")
stripped = joined.strip('ciao ') #elimina la sottostringa passata come parametro ALL'INIZO E ALLA FINME DELLA STRINGA su cui chiamiamo il metodo
print(stripped)

replaced = joined.replace('ciao', 'bella') #replace the first parameter in the string with the second paramter
print(replaced)
#split() splits the string with the given separator

titled = joined.title() #converts every start character of every word into capital letter
print(titled) 

swapped_case = word.swapcase() #converts every character into the opposite case (lower --> upper, upper --> lower)
print(swapped_case)

print('\\ / //'*2) #doubles the content