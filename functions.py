#define and call a function

#def sum(a,b):
  #  return a+b

# print(sum(4,9)) #order counts

def printName(firstName ,lastName):
    print(f'my full name is {firstName} {lastName}')

printName(lastName = 'Gonnella', firstName = 'Luigi') #order does not count, the name of the parameter makes the difference

#default parameters (if not passed)

# def sum(b, a=3): #dafault arguments always at the end
#    return a+b

# print(sum(7)) # --> 10

#arbitrary number of arguments
def sumArb(*nums):
    total = 0
    for num in nums:
        total += num
    else:
        print(f'the total of the arguments is: {total}')
    
sumArb(1,2,3)

#or

def sumArb2(first, *nums):
    total = first
    print(f'the first argument is {first}')
    for num in nums:
        total += num
    else:
        print(f'the total of the arguments is: {total}')
    
sumArb2(1,2,3)

#functions as an argument

# def sumArb3(f, a, b):
  #  sum = f(a, b)
  #  print(f'the sum between {a} and {b} is equal to {sum}')

# sumArb3(sum, 1, 2)# --> 3

def sum_of_even(ran):
    total = 0
    for i in range(0, ran, 2):
        total += i
    else:
        print(f'the sum of the even numbers in the range of {ran} si equal to {total}')

sum_of_even(10)

def statistics(*lists):
    
    for lst in lists:
        total = 0
        max_count = 0
        mode = -1
        max_el = float('-inf')
        min_el = float('inf')
        total = sum(lst)
        mean = total/len(lst)
        print(f'the mean of the list {lst} is equal to {mean}')
        print(f'the median of the list {lst} is {lst[len(lst)//2]}')
        for el in lst:
            if (el > max_el):
                max_el = el
            if (el < min_el):
                min_el = el
            count = lst.count(el)
            if (count > max_count):
                max_count = count
                mode = el
        print(f'the mode of the list {lst} is {mode}')
        print(f'the range of the list {lst} is {max_el-min_el}')
        #or
        print(f'the range of the list {lst} is {max(lst)-min(lst)}')
        variance = sum((x-mean)**2 for x in lst) / len(lst)
        print(f'the variance of the list {lst} is {variance}')
        dev_st = variance ** 0.5
        print(f'the standard deviation of the list {lst} is {dev_st}')
    

statistics([1, 2, 3, 4, 5], [2, 4, 6, 8, 10])

from loops.data import data #loops.data is a module, while math (for example) is a BUILT-IN module


def the_most_spoken_languages(n):
    languages = []
    for dict in data:
        for language in dict['languages']:
            languages.append(language)
    languages.sort()
    stat = []
    i=1
    while i<len(languages):
        count = 1
        while  i<len(languages) and languages[i] == languages[i-1] :
            count +=1
            i+=1
        stat.append({'language': languages[i-1], 'count': count})
        i+=1
    stat.sort(key=lambda x: x['count'], reverse=True)
    for el in stat[0:n]:
        print(el['language'])

the_most_spoken_languages(10)

#def the_most_spoken_languages(n):
#    language_count = {}
 #   for country in data:
  #      for language in country['languages']:
   #         language_count[language] = language_count.get(language, 0) + 1
    # Ordina per frequenza decrescente
    #sorted_languages = sorted(language_count.items(), key=lambda x: x[1], reverse=True)
    #for lang, count in sorted_languages[:n]:
     #   print(lang)


def the_most_populated_countries(n):
    populations = {}
    for country in data:
        populations[country['name']] = country['population'] 
    sorted_populations = sorted(populations.items(), key=lambda x: x[1], reverse=True) #or we could add tuple/dictionaries to a list with name/population as key/value and then call  listy.sort(lambda x: x['population'])
    for name, population in sorted_populations[0:n]:
        print(name)

the_most_populated_countries(20)
        


    



