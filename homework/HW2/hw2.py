#   Python for Data Analysis and Scientific Computing
#   COMPSCI X433.3 - 005
#   David Lim Cheng (X017427)

import numpy as np

print("\nPython for Data Analysis and Scientific Computing\nCOMPSCI X433.3 - 005\nDavid Cheng\n")

# Create matrix A with size (3,5) containing random numbers
A = np.matrix(np.random.random((3,5)))
print('Create matrix A with size (3,5) containing random numbers:')
print(A)
print('\n')

# Find the size and length of A
A_size = A.size
A_length = len(A)
print('Find the size and length of A:')
print("Size of A: {}".format(A_size))
print("Length of A: {}".format(A_length))
print('\n')

# Resize (crop/slice) matrix A to size (3,4)
A = np.resize(A, (3,4))
print('Resize (crop/slice) matrix A to size (3,4):')
print(A)
print('\n')

# Find the transpose of matrix A and assign it to B
B = A.T
print('Find the transpose of matrix A and assign it to B:')
print(B)
print('\n')

# Find the minimum value in column 1 of matrix B
B_min = min(B[:, 1])
print('Find the minimum value in column 1 of matrix B:')
print(B_min)
print('\n')

# Find the minimum and maximum values for the entire matrix A
A_min = A.min()
A_max = A.max()
print('Find the minimum and maximum values for the entire matrix A:')
print("Maximum of A: {}".format(A_max))
print("Minimum of A: {}".format(A_min))
print('\n')

# Create vector X (an array) with 4 random numbers
X = np.random.random(4)
print('Create vector X (an array) with 4 random numbers:')
print(X)
print('\n')

# Create a function and pass vector X and matrix A in it
# In the new function multiply vector X with matrix A and assign the result to D
def my_function(vector_x, vector_a):
    D = X*A
    print('Create a function and pass vector X and matrix A in it')
    print('In the new function multiply vector X with matrix A and assign the result to D')
    print("D:")
    print(D)
    print('\n')
    return D

D = my_function(X, A)

# Create a complex number Z with absolute and real parts != 0
Z = np.complex(1,3)
print('Create a complex number Z with absolute and real parts != 0:')
print("Z: {}".format(Z))
print('\n')

# Show its real and imaginary parts as well as its absolute value
print('Show its real and imaginary parts as well as its absolute value:')
print("Z real: {}".format(Z.real))
print("Z imaginary: {}".format(Z.imag))
print("Z absolute: {}".format(np.absolute(Z)))
print('\n')

# Multiply result D with the absolute value of Z and record it to C
C = D * np.absolute(Z)
print('Multiply result D with the absolute value of Z and record it to C:')
print(C)
print('\n')

# Convert matrix B from a matrix to a string and overwrite B
B = str(B)
print('Convert matrix B from a matrix to a string and overwrite B:')
print(B)
print("Type of B: {}".format(type(B)))
print('\n')

# Display a text on the screen: '<Your Name> is done with HW2'
name = 'David Cheng'
print('Display a text on the screen: \'<Your Name> is done with HW2\'')
print("{} is done with HW2".format(name))
print('\n')