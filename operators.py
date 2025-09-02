print('Floating Point Number, PI', 3.14) #altro modo per printare, printa immediatamente alla fine con uno spazio per separarlo dal corpo della print

#complex numbers
complex_mul = (1 + 1j) * (2 + 3j)
print(f"the multiplication between the complex numbers 1 + 1j asnd 2 + 3j is equal to {complex_mul}")

#altri operatori (in, is, not in, is not)
container = 'le stringhe sono contenitori di caratteri in python'
word = 'python'
print(f"la parola {word} si trova nel container {container}?", 'Si' if word in container else 'No') #programmazione condizionale in python

container_numbers = [2, 3, 4, 5, 6, 7]

for num in container_numbers: #in python il for non vuole tonde attorno alla variabile
    print(f"the number evaluated is {num}")

num = 1

if (num not in container_numbers):
    print(f"the number {num} is not in container_numbers: {container_numbers}")

for i in range(1,6): #equivalente in C di for (i=1; i<6 ; i++)
    for j in range(5): #equivalente in C di for(i=0;i<5;i==)
        if (j==0) or (j==2):
            print(i**1, end=' ') # printo 4 numeri corrispndenti a i sulla prima colonna senza andare a capo (end=' ')
        elif (j==1):
            print(i**0, end=' ')
        elif (j==3):
            print(i**2, end=' ')
        elif (j==4):
            print(i**3)
