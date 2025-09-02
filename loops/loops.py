lst = [0, 3, 5, 1]

while (len(lst) < 8):
    lst.append(1)
    if (lst[2]+lst[3]>4):
        continue #skips one iteration and goes to the next of the while
    print(lst)
    break #exit form entire loop
    
print(lst)

for number in lst: ... #anche per tuple, dizionari (con key)

#RANGE
for i in range(len(lst)): ... # equivalente al for(i=0; i<len(lst); i++)
for i in range(0, len(lst), 1): ... # equivalente al for(i=0; i<len(lst); i++)
for i in range(0, len(lst), 1): ... # equivalente al for(i=0; i<len(lst); i++)


person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

for key, value in person.items():
    print(f'key: {key}, value: {value}')

#PASS, serve per non dare errori se il codice ancora non e completo ma l'abbiamo gia scritto:

for x in range(5):
    pass  # il ciclo non fa nulla

#ELSE in for/while

for x in range(5):
    if x == 3:
        break
else:
    print("Finito senza break!")  # IT'S NOT EXECUTED if there is a break


#EXERCISE
from data import data #importo lista di dizionari {
     #    "name": "Afghanistan",
     #    "capital": "Kabul",
     #    "languages": [
      #       "Pashto",
       #      "Uzbek",
       #      "Turkmen"
       #  ],
       #  "population": 27657145,
       #  "flag": "https://restcountries.eu/data/afg.svg",
     #    "currency": "Afghan afghani"
    # }

total_languages = []

for dict in data:
    if ('languages' in dict):
        total_languages += dict['languages']

print(len(set(total_languages))) #number of languages without duplicates

max = 0
max_language = ''
for language in total_languages:
    count = total_languages.count(language)
    if (count >max):
        max = count
        max_language = language

print(max_language)


data.sort(key=lambda x: x['population'], reverse=True) #lambda function
for dict in data[0:10]:
    print(dict['name'])