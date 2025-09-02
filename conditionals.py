# a = input('Insert a number: ')
# b = input('Insert a second number: ')

# if (a > b):
#     print(f'{a} is greater than {b}')
# elif (b > a):
#     print(f'{b} is greater than {a}')
# else:
#     print(f'{a} and {b} are equals')


# fruits = ['banana', 'orange', 'mango', 'lemon']
# fruit = input('Insert a fruit: ')

# if (fruit in fruits):
#     print(f'{fruit} is already in th elist')
# else:
#     fruits.append(fruit)
#     print(f'{fruit} successfully added to the list, now the updated list is: {fruits}')



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

count = 0
if ('skills' in person):
    print(person['skills'][len(person['skills'])//2])

if ('skills' in person and 'Python' in person['skills']):
    print(person['skills'])

if ('skills' in person and ({'JavaScript', 'React'}==(set((person['skills']))))):
    print('He is a frontend developer')
    count+=1

if ('skills' in person and ({'Node', 'MongoDB', 'Python'}.issubset(set((person['skills']))))):
    print('He is a backend developer')
    count+=1

if ('skills' in person and ({'React', 'Node', 'MongoDB'}.issubset(set((person['skills']))))):
    print('He is a fullstack developer')
    count+=1

if (count==0):
    print('He is undefined')

if ('is_married' in person and person['is_married']==True and 'country' in person and person['country']=='Finland'):
    print(f'{person['first_name']} lives in {person['country']}. {('He is married.') if person['is_married']==True else 'He is not married.'}')