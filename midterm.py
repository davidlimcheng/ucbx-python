#   6/18/2018 - Midterm
#   Python for Data Analysis and Scientific Computing
#   COMPSCI X433.3 - 005
#   David Lim Cheng (X017427)
#   davidlimcheng@gmail.com

import numpy as np
import matplotlib.pyplot as plt

# create an array A with 12 elements beginning from number 5, containing consecutive odd numbers
A = np.array([n for n in range(5, 29) if n % 2 != 0], dtype=np.float64)


# compute the simple moving average of an array (SMA), using an adjustable window using a function
# the function calculating the SMA of the array must take two input arguments
# the array (A) and a window width with default value 2
def simple_moving_average(array, window=2):
    print('The original array is: {}\n'.format(array))
    simple_moving_average = []
    current_moving_average = []
    for i in range(0, len(array) - (window - 1)):
        print('Current window width: {}'.format(window))
        simple_moving_average.append(np.mean(array[i:i + window]))
        current_moving_average.append(np.mean(simple_moving_average))
        print('The SMA result is: {}'.format(simple_moving_average))
        print('The CMA of this SMA result is: {}'.format(current_moving_average))
        print('\n')
    print('---------------------------------')
    return simple_moving_average


# make two function calls to the SMA
B = simple_moving_average(A)
C = simple_moving_average(A, window=4)

# plot the sin functions for arrays B and C, specifying different color, lindwidth, linestyle, label, and figure names
# show the grid and legend
plt.figure(figsize=(6, 6), dpi=120)
B_sin = np.sin(B)
C_sin = np.sin(C)

plt.subplot(2, 1, 1)
plt.plot(B, B_sin, color='blue', linewidth=1.5, linestyle='--', label='B_sin')
plt.legend(loc='best')
plt.grid()
plt.title('sin of B')

plt.subplot(2, 1, 2)
plt.plot(C, C_sin, color='red', linewidth=2.0, linestyle=':', label='C_sin')
plt.legend(loc='best')
plt.grid()
plt.title('sin of C')

plt.show()