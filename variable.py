import math;

first_name, last_name, full_name, country, city, age, year, is_married, is_true, is_light_on = 'Jhon', 'Doe', 'Jhon Doe', 'USA', 'Los Angeles', 23, 2025, False, True, True

print(first_name + ' of type ' + str(type(last_name))) # it's the same of
print(f"{first_name} of type {type(first_name)}") #this
print(f"my first name: {first_name}, has {len(first_name)} letters")

# match len(first_name) : --> lo posso usare solo quando ci sono valori fissi ad esempio '1', '2', ecc...

if len(first_name) < len(last_name): #i blocchi nei rami if, elif, else ecc.. sono determinati dall' indentazione
    print(f"My first name: {first_name} is shorter than my last name: {last_name}")
elif len(first_name) > len(last_name):
    print(f"My first name: {first_name} is longer than my last name: {last_name}")
else:
    print("my first name has the same length of my last name")


num_one = 3
num_two = 4

num_exp = math.pow(num_one, num_two) #math.pow restituisce sempre un float, in alternativa possiamo fare a ** b per fare l'elevazione
print(f"the exponential {num_one}exp{num_two} is equal to {num_exp}")

    
var_reminder = num_two % num_one
print(f"the modulus division between the numbers {num_two} and {num_one} is equal to {var_reminder}")


floor_division = num_two // num_one #floor division
print(f"the floor division between {num_two} and {num_one} is equal to {floor_division}")

radius = 30
area_of_circle =math.pi*math.pow(radius, 2)
print(f"the area of the circle of radius {radius} is equal to {area_of_circle}")

circum_of_circle = 2*math.pi*radius
print(f"the circumnference of circle of radius {radius} is equal to {circum_of_circle}")

radius_input = input("Please, enter the desired value of the radius: ")
circum_of_circle = 2*math.pi*float(radius_input) #conversione in float da stringa
print(f"the circumnference of the circle of radius: {radius_input} is equal to {circum_of_circle}")

#prendere piu valori in input usando la funzione split()


input_from_user = input('please insert the following informations separated by a white space: first_name last_name full_name country city age, year, is_married, is_true, is_light_on: ')
first_name, last_name, full_name, country, city, age, year, is_married, is_true, is_light_on = input_from_user.split() #vengoono presi in automatico come stringhe, se voglio convertirli in altri valori devo farlo manualmente
print(f"the variables inserted by the user are: first_name: {first_name}, last_name: {last_name}, full_name: {full_name}, country: {country}, city: {city}, age: {age}, year: {year}, is_married? {is_married}, is_true? {is_true}, is_light_on? {is_light_on}")

