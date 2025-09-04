import numpy as np

#!BASICS
#numpy arrays can be of n>= dimensions and each dimension is an axe (matrix n x n has 2 axis of length n). They are called ndarray.

#!ATTRIBUTES of ndarray
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

#!CREATE MATRIXES
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

#!BASIC OPERATIONS
a = np.array([10, 20 ,30, 40])
b = np.arange(4)

c = a - b #difference of every eleemnt in the same position

d = a ** 2 #power of every element

e = 10 * np.sin(a) #operations to every element

f = a < 20 #array of True/False corresponding to the result of the operation for every element

product_elementwise = a * c #!is NOT matrix product, but the product element for element
matrix_product = a @ b #!matrix product (rows * columns)
matrix_product_2 = a.dot(b) #!matrix product (rows * columns)

#!MODIFYING THE EXISTING ARRAY
a += 2 #and so on for +, -, *, / ecc...

#operations between matrix follows an automatic UPCASTING

#!ARRAY METHODS
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

#!UNIVERSAL FUNCTIONS
#they operate elementwise and produce an array as a result

A = np.arange(12).reshape(4, 3)

exp_matr = np.exp(A) #calcola e^el per ogni el (elemento)

sqrt_matr = np.sqrt(A) #radice

B = np.array([2., -1., 4.])

C = np.add(A, B) #somma come con operatore +

#!INDEXING, SLICING, ITERATING
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
#!ITERATING
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

a_flattered = a.ravel() #transformed in a 1d array

#!TRASPOSTA
a_transposed = a.T
print(a_transposed)

#!RESIZE
a = np.arange(4).reshape(2,2) #vista dopo l'arange, non un array vero e proprio, a non possiede i dati
a = a.copy() #ora possiede i dati
a.resize((3,3)) #reshape don't modify the array, just change the positions returning a new view on the array and if the reshap is not possible it raises an error
                    #!RESIZE instead, change the array itself and if there aren't eough eleemnets, it fills the voids with zeros or random numbers

#!RESHAPE with NOT ALL DIMENSIONS
b = a.reshape(3, -1) #where there is a -1 in reshape, the number of that dimension is automatically calculated

#!STACKING
random_array = np.floor(10 * np.random.random((2, 3))) #array casuale
random_array2 = np.floor(10 * np.random.random((2, 3))) #array casuale

stacked_vertical = np.vstack((a, b)) #uno sotto l'altro
stacked_horizontal = np.hstack((a,b)) #uno a fianco all'altro

a = np.array([4., 2.])
b = np.array([3., 8.])

column_stacked = np.column_stack((a, b)) #for 2D is equivalent to hstack, for 1D first transforms the array in a acolumn and then stack them together
# --> [[4., 3.],
     #[2., 8.]]

stacked_horizontal = np.hstack((a,b)) #uno a fianco all'altro
# --> [4., 2., 3., 8.]

#!TRANSFORMING 1D ARRAYS
from numpy import newaxis
a = np.array([1, 2, 3])
from_row_to_column = a[:, newaxis]


#!STACKING ALONG ONE AXIS
a = np.arange(9).reshape(3,3)
one_row = np.r_[a.ravel(), 0, 4]
print(one_row)

#!SPLITTING ARRAY
a = np.floor(10 * np.random.random((3, 3)))
print(a)

np.hsplit(a, 3) #splits a into 3 along horizontal axis, vsplit does it along vertical one
np.hsplit(a, (1,2)) #splits a after first (first split) and second (second split) columns

#!COPIES AND VIEWS

#NO COPY
a = np.array([1, 2, 3, 4])
b = a #b and a are two names for the same array, not a copy at all

def f(x):
    print(id(x))

print(id(a))
f(a) #same as above --> no copy

#VIEW
a = np.arange(9) # [0  1  2  3  4  5  6  7  8]
b = a.reshape(3, 3) #now b is a VIEW of the array generated by arange (a)

print(a is b) # --> False

b = a.view() #explicit view
print(b.base is a) #True --> base refers to the owner of data
b.flags.owndata # --> Flase

b[0] = 10 #a's data change
print(a) # [10  1  2  3  4  5  6  7  8]

#slicing an array returns a copy aswell
a = np.arange(9).reshape(3,3)
b = a[:, 2] #last column
print(b)
b[:] = 10 #all b's data equal to 10, it's a view of b, and changes b's data
print(b)

#!DEEP COPY
a = np.floor(10 * np.random.random((3, 3)))
b = a.copy() #exact copy of a,b n now owns this data, aswell as a, no view at all just an exact deep copy

#after copy we can release the original array if we don't need it anymore, so we release memory


#!INDEXING AND ARRAYS OF INDECES
a =  np.arange(12) ** 2 #array of squares of the first 12 numbers
i = np.array([2, 4, 6, 8]) #array of indices
b = a[i] #a's elements in everi index indicated by i

c = np.array([[2, 4],
             [6, 8]])
d = a[c] #same shape of c, but same values as b

#an example can be a palette of colors and an image refering to that colors

palette = np.array([[0, 0, 0],         # black
                    [255, 0, 0],       # red
                    [0, 255, 0],       # green
                    [0, 0, 255],       # blue
                    [255, 255, 255]])  # white
image = np.array([[0, 1, 2, 0],  # each value corresponds to a color in the palette
                  [0, 3, 4, 0]])

palette[image] #takes value from palette in indexes indicated by image, and creates two array inside
#array([[[  0,   0,   0],
 #       [255,   0,   0],
  #      [  0, 255,   0],
   #     [  0,   0, 255]],
#
 #      [[  0,   0,   0],
  #      [  0,   0, 255],
   #     [255, 255, 255],
    #    [  0,   0,   0]]])

#INDEXES IN MORE THAN ONE DIMENSION
a = np.arange(12).reshape(3, 4)
i = np.array([[0, 1],  # indices for the first dim of `a`
              [1, 2]])
j = np.array([[2, 1],  # indices for the second dim
              [3, 3]])

b = a[i,j] #takes the element (0,2) of a and puts it in (0,0) of b and so on...

b = a[:, j] ##every element in the column specified by j is inserted in every row of b, in the column specified by the j'index
#array([[[ 2,  1],
 #       [ 3,  3]], --> first row of a, elements from column specified by j (so 2,1,3,3)
#
 #      [[ 6,  5], --> second row of a
  #      [ 7,  7]],
#
 #      [[10,  9], --> third row of a
  #      [11, 11]]])

#EQUIVALENCES
a[i, j] 
#is the same of
a[(i, j)]
#but id s different from
#a[[i, j]] #this will take all elemnts from the rows specified in i and j

#!FIND MAXIMUMS
time = np.linspace(20, 145, 5) #5 elements
data = np.sin(np.arange(20)).reshape(4, 5)

#INDEX(row) OF MAXIMUM FOR EVERY COLUMN
ind = data.argmax(axis=0)

time_max = time[ind] #time corresponding to the max (simulation)
data_max = data[ind, range(data.shape[1])] #data.shape[1] is the number of columns (5), ind is the row in which there is the maximum for the corresponfing column (in order 0, 1, 2 eccc...)
#or data.max(axis=0) takes the maximum for every column 
np.all(data_max == data.max(axis=0)) #se vogliamo solo un valore True/False usiamo np.all, se vogliamo una matrice di booleani facciamo uguaglianza semplice

#ARRAY AS A TARGET INDEX
a = np.floor(10 * np.random.random((5,5)))
a[[[2,3],[3,3]]] += 1 #takes all elements in row 2 and 3 (3 three times, but the operation will only be performed once) and add 1 to display in the same form of i and j

#!BOOLEAN INDEXING
a = np.arange(12).reshape(3, 4)
b = a < 4 #boolean array of the same form of a
c = a[b] #array 1D with the elements taken from a, in the positions corresponfing to True in b

#ESAMPLE OF BOOLEAN INDEXING APPLICATION (display mandelbrot set)
import matplotlib.pyplot as plt
def mandelbrot(h, w, maxit=20, r=2):
    """Returns an image of the Mandelbrot fractal of size (h,w)."""
    x = np.linspace(-2.5, 1.5, 4*h+1)
    y = np.linspace(-1.5, 1.5, 3*w+1)
    A, B = np.meshgrid(x, y)
    C = A + B*1j
    z = np.zeros_like(C)
    divtime = maxit + np.zeros(z.shape, dtype=int)
    for i in range(maxit):
        z = z**2 + C
        diverge = abs(z) > r                    # who is diverging
        div_now = diverge & (divtime == maxit)  # who is diverging now
        divtime[div_now] = i                    # note when
        z[diverge] = r                          # avoid diverging too much
    return divtime
plt.clf()
plt.imshow(mandelbrot(400, 400))
plt.show()

#!THE ix_() FUNCTION
#it is useful to calculate operations for every possible combinations of elements inside the arrays
#normal operations between arrays are elementwise, so for each element in the SAME position
#but now we want to perform these operations for every couple of elements (if we have two arrays), not only the couples defined by the elements in the same indexes

a = np.array([2, 3, 4, 5])
b = np.array([8, 5, 4])
c = np.array([5, 4, 6, 8 ,3])

ax, bx, cx = np.ix_(a, b, c) #transform each element in an array 2D, so each array will be 3D
print(ax.shape, bx.shape, cx.shape) # --> (4, 1, 1) (1, 3, 1) (1, 1, 5)

result = ax + bx * cx #not elementwise, but for each triplet
print(result)

#!STRUCTURED ARRAYS

x = np.array([('Rex', 9, 81.0), ('Fido', 3, 40.0)], dtype=[('name', 'U10'), ('age', 'i4'), ('weight', 'f4')])
#accessing an entry
x[0]

#accessing all elements of a single field
x['age']

#SPECIFYING DTYPES of arrays

#1 list of tuples
np.dtype([('x', 'f4'), ('y', np.float32), ('z', 'f4', (2, 2))])

#2 string of comma-separated dtype specifiations
np.dtype('i8, f4, S3') #fieldname would be default, so f0, f1, f2 and so on

#dictionary of field parameters arrays
np.dtype({'names': ['col1', 'col2'], 'formats': ['i4', 'f4']}) # ‘offsets’, ‘itemsize’, ‘aligned’ and ‘titles’ are optional

#!HISTOGRAMS
# Build a vector of 10000 normal deviates with variance 0.5^2 and mean 2
plt.figure(2)
mu, sigma = 2, 0.5
v = np.random.normal(mu, sigma, 10000)
#build a normalized histogram with 50 bins and plots automatically
plt.hist(v, bins=50, density=True)

# Compute the histogram but we have to plot manually
(n, bins) = np.histogram(v, bins=50, density=True)  # NumPy version (no plot)
plt.plot(.5 * (bins[1:] + bins[:-1]), n)
plt.show()