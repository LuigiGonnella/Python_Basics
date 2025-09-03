import numpy as np

#BASICS
#numpy arrays can be of n>= dimensions and each dimension is an axe (matrix n x n has 2 axis of length n). They are called ndarray.

#ATTRIBUTES of ndarray
a = np.arange(15).reshape(3, 5) #arange forma un array di 15 elementi da 0 a 14 e  reshape trasforma quest'array in una matrice 3x5
print(a) #printing array

a.shape #(3, 5)
a.ndim # 2
a.dtype.name #'int64'
a.itemsize #8, ovvero 8 byte occupati da ogni elemento della matrice
a.size #15
type(a) #<class 'numpy.ndarray'>
b = np.array([1, 2, 3, 4]) #creazione array numpy
print(b) # [1, 2, 3, 4]
type(b) #<class 'numpy.ndarray'>

#CREATE MATRIXES
matrix = np.array([(1, 2, 3, 4), (5, 6, 7, 8)]) #matrix 2x4, each parameter is a row
print(matrix)
#specifying types of elements in the matrix
complex_matrix = np.array([(1, 2), (1, 4)], dtype='complex')
print(complex_matrix) #[[1.+0.j 2.+0.j]
                      # [1.+0.j 4.+0.j]]

#create zero_matrix
zero_matrix = np.zeros((4, 4)) #4x4 full of zeros, default is float64
print(zero_matrix)

#create one_matrix
one_matrix = np.ones((4, 4), dtype=np.int16) #4x4 full of ones of int16
print(one_matrix)

#create random content in matrix (depend on state of memory in that moment)
random_matrix = np.empty((4, 4))
print(random_matrix)

#create random matrix with np.random
random_matrix = np.random.rand(2, 4)
print(random_matrix)

#generate values with fixed interval 
t = np.arange(0, 10, 0.2) #but the number of generated values can be unpredictable due to floating point number created
t1 = np.linspace(0, 10, 50) #50 numbers with the same distance between 0 and 10

#PRINTOPTIONS
big_matrix = np.arange(10000).reshape(100, 100)
print(big_matrix) #does not print entire matrix

import sys 
np.set_printoptions(threshold=sys.maxsize) 
#!print(big_matrix) prints entrie matrix

#BASIC OPERATIONS
a = np.array([10, 20 ,30, 40])
b = np.arange(4)

c = a - b #difference of every eleemnt in the same position

d = a ** 2 #power of every element

e = 10 * np.sin(a) #operations to every element

f = a < 20 #array of True/False corresponding to the result of the operation for every element

product_elementwise = a * c #!is NOT matrix product, but the product element for element
matrix_product = a @ b #!matrix product (rows * columns)
matrix_product_2 = a.dot(b) #!matrix product (rows * columns)

#MODIFYING THE EXISTING ARRAY
a += 2 #and so on for +, -, *, / ecc...

#operations between matrix follows an automatic UPCASTING

#ARRAY METHODS
a = np.arange(16).reshape(4,4)
print(a)
sum_of_elements = a.sum() #consider all elements
min_element = a.min()
max_element = a.max()

sum_first_row  = a.sum(axis=0) #sum each column to obtain the sum of the each column as an array
print(sum_first_row)

min_of_each_row = a.min(axis=1) #min of each row as a numpy array

cumulative_sum = a.cumsum(axis=1) #cumulative sum along each row, in the last column we will obtain the sum of the corresponfing row
print(cumulative_sum)

#UNIVERSAL FUNCTIONS
#they operate elementwise and produce an array as a result

A = np.arange(12).reshape(4, 3)

exp_matr = np.exp(A) #calcola e^el per ogni el (elemento)

sqrt_matr = np.sqrt(A) #radice

B = np.array([2., -1., 4.])

C = np.add(A, B) #somma come con operatore +

#INDEXING, SLICING, ITERATING
#MONODIMENSIONAL
a = np.arange(10)
el = a[2] #take element in index 2, because a has 1 dimension
els = a[2:5] #like normal lists

a[0:8:2] = 0 #like normal lists, from 0 to 8 with step 2, we put 0
print(a)

a[::-1] #reversed

for el in a:
    print(el**(2/3.)) #normal, float operation

#MULTIDIMENSIONAL

def f(x, y):
    return 10 * x + y

b = np.fromfunction(f, (5, 4), dtype=int) #each element in position (i, j) becomes (10*i)+j, so the element in poisition (0,0) will become 1, in position (1,3) 13 and so on
print(b)

el = b[2,3] #el in position (2,3)

els = b[0:5, 1] #takes all second column (each element --> 0:5, from column 1)

els = b[:, 1] #equivalent

els = b[1:3, :] #from row 1 to 3 of each column (all rows 1 and 3)

#if we obmit an axe, its default value is :

first_row = b[0] #last_row is b[-1]
first_column = b[..., 0] #this operator is very useful when we have a lot of dimension instead of writing ':' for each of them
#'...' can also be present between more values

a = np.arange(1000000).reshape(10, 10, 10, 10, 10, 10) #6 dimensions
first = a[0, ...] #or only a[0]
third_something = a[4, ..., 5, :] #first and before_last


c = np.array([[[  0,  1,  2],  # a 3D array (two stacked 2D arrays)
               [ 10, 12, 13]], #in position c[0] we have the first 2d matrix, and in position c[1] we have the second, the other two dimension s are the normal dimensions of the matrixes
              [[100, 101, 102],
               [110, 112, 113]]])
c.shape # --> (2, 2, 3)
print(c[1, ...])  # same as c[1, :, :] or c[1], takes all the second matrix
print(c[..., 2])  # same as c[:, :, 2], for both matrixes, for all the rows (entire column), takes the third column [[2  13]
                                                                                                                   #[102 113]]
print('***********************************************\n\n')
#ITERATING
a = np.arange(4).reshape(2,2) # 2D
for row in a:
    print(row)

b = np.arange(27).reshape(3,3,3) # 3D, 3 matrix 3x3
for matrix2d in b:
    print(matrix2d)         
 #[[0 1 2]
# [3 4 5]
# [6 7 8]]
#[[ 9 10 11]
# [12 13 14]
# [15 16 17]]
#[[18 19 20]
# [21 22 23]
# [24 25 26]]                                                                                        

for el in b.flat: #takes every element like a list
    print(el)
#0
#1
#2
#...
#26